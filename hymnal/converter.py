"""
# Converter : HTML <--> JSON
"""
# -*- coding: utf-8 -*-

# standard
from dataclasses import dataclass, field, asdict
from json import dump, load
from pathlib import Path
from typing import List

# external
from jinja2 import Environment, PackageLoader, select_autoescape
from bs4 import BeautifulSoup


@dataclass
class Stanza:
    """
    Store hymn stanza
    """

    stanza_number: int = -1
    lines: List[str] = field(default_factory=list[str])


@dataclass
class Hymn:
    """
    Store hymn
    """

    hymn_number: int = -1
    starts_on: str = ""
    chorus: List[str] = field(default_factory=list[str])
    stanzas: List[Stanza] = field(default_factory=list[Stanza])


def _html_song_parser(hymn_file: Path) -> Hymn:
    """Parse songs from reveal.js HTML files"""
    with open(file=hymn_file, mode="rt", encoding="utf-8") as _html_file:
        _html_content = _html_file.read()

    _soup = BeautifulSoup(_html_content, "lxml")

    hymn = Hymn()

    if _hyn := _soup.select_one("h1.hymn-no"):
        hymn.hymn_number = int(_hyn.text)

    hymn.starts_on = (
        "stanza-1"
        if '<section id="stanza-1" class="s-hymn">' in _html_content
        else "chorus"
    )

    for _stanza_section in _soup.select('section[id^="stanza-"]'):
        _stanza_number = (
            int(_szn.text.rstrip("."))
            if (_szn := _stanza_section.select_one("p.stanza-no"))
            else -1
        )
        _lines = [line.text.strip() for line in _stanza_section.select("h3")]
        _lines.extend([line.text.strip() for line in _stanza_section.select("h4")])
        hymn.stanzas.append(Stanza(stanza_number=_stanza_number, lines=_lines))
    if (chorus_section := _soup.select_one('section[id^="chorus"]')) and (
        _verses := chorus_section.select("em")
    ):
        hymn.chorus = [line.text.strip() for line in _verses]

    hymn.stanzas.sort(key=lambda stz: stz.stanza_number)
    return hymn


def html_to_json():
    """Convert HTML to JSON"""
    for idx in range(1, 2001):
        hymn_path = ag_hymnal_html / f"{str(idx).zfill(4)}.html"
        if not hymn_path.exists() or not hymn_path.is_file():
            continue
        with open(
            file=ag_hymnal_json / f"{str(idx).zfill(4)}.json",
            mode="wt",
            encoding="utf-8",
        ) as ag_f:
            dump(obj=asdict(_html_song_parser(hymn_path)), fp=ag_f, ensure_ascii=False)


############################## JSON-HTML ##############################


def _json_song_reader(hn_f: Path):
    """Parse songs from JSON files"""
    with open(file=hn_f, mode="rb") as ag_f:
        return load(ag_f)


def json_to_html():
    """Convert JSON to HTML"""

    hymn_path = ag_hymnal_json / "0206.json"  # SAC
    # hymn_path = ag_hymnal_json / "1114.json" # SASWC
    # hymn_path = ag_hymnal_json / "0366.json"  # SASNC

    hymn = Hymn(**_json_song_reader(hymn_path))

    jj_env = Environment(
        loader=PackageLoader("converter"),
        autoescape=select_autoescape(),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    if hymn.chorus:
        chorus = hymn.chorus
        ss_tag, se_tag = "<h3><em>", "</em></h3>"
        if hymn.starts_on == "chorus":
            template_file = "sac.html.j2"
            stz_list = hymn.stanzas
            stanza_1 = None
        else:
            template_file = "saswc.html.j2"
            stz_list = hymn.stanzas[1:]
            stanza_1 = hymn.stanzas[0]
    else:
        ss_tag, se_tag = "<h3>", "</h3>"
        chorus = None
        template_file = "sasnc.html.j2"
        stz_list = hymn.stanzas[1:]
        stanza_1 = hymn.stanzas[0]

    print(
        jj_env.get_template(template_file).render(
            hymn_number=hymn.hymn_number,
            # main section
            stanza_list=stz_list,
            ms_tag="<h3>",
            me_tag="</h3>",
            # side section
            chorus=chorus,
            ss_tag=ss_tag,
            se_tag=se_tag,
            # other
            stanza_1=stanza_1,
        )
    )


pgm_root = Path(__file__).parent.parent
ag_hymnal_html = pgm_root / "static/hymnal/ag"
ag_hymnal_json = pgm_root / "generator/ag/json"
ag_hymnal_json.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    # html_to_json()
    # ref: https://github.com/pallets/jinja/issues/1239#issuecomment-645231227
    json_to_html()
