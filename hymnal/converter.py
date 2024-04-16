"""
# Converter : HTML <--> JSON
"""
# -*- coding: utf-8 -*-

# standard
from dataclasses import dataclass, field, asdict
from json import dump, load
from shutil import copytree
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


def _html_song_parser(hymn_file: Path):
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


def html_to_json(source: Path, destination: Path):
    """Convert HTML to JSON"""
    for idx in range(1, 2001):
        hymn_path = source / f"{str(idx).zfill(4)}.html"
        if not hymn_path.exists() or not hymn_path.is_file():
            continue
        with open(
            file=destination / f"{str(idx).zfill(4)}.json",
            mode="wt",
            encoding="utf-8",
        ) as ag_f:
            dump(obj=asdict(_html_song_parser(hymn_path)), fp=ag_f, ensure_ascii=False)


############################## JSON-HTML ##############################


def _json_song_parser(hymn_path: Path):
    """Parse songs from JSON files"""
    with open(file=hymn_path, mode="rb") as ag_f:
        hymn = Hymn(**load(ag_f))

    jj_env = Environment(
        loader=PackageLoader("converter"),
        autoescape=select_autoescape(),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    if hymn.hymn_number == -1 or len(hymn.stanzas) < 1:
        return f"<html>\n<title>BAD FILE</title>\n<body>\n<p>{hymn_path}</p>\n<body>\n</html>"

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

    return jj_env.get_template(template_file).render(
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
        rel_path="..",
    )


def json_to_html(source: Path, destination: Path):
    """Convert JSON to HTML"""
    for idx in range(1, 2001):
        hymn_path = source / f"{str(idx).zfill(4)}.json"
        if not hymn_path.exists() or not hymn_path.is_file():
            continue
        with open(
            file=destination / f"{str(idx).zfill(4)}.html",
            mode="wt",
            encoding="utf-8",
        ) as ag_f:
            ag_f.write(_json_song_parser(hymn_path))


pgm_root = Path(__file__).parent.parent
# temporary_source_ag_hymnal_html = pgm_root / "hymnal/temp/ag/html"
ag_hymnal_json = pgm_root / "hymnal/ag"
# ag_hymnal_json.mkdir(parents=True, exist_ok=True)
output_ag_hymnal_html = pgm_root / "dist/ag"
output_ag_hymnal_html.mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":
    # html_to_json(temporary_source_ag_hymnal_html, ag_hymnal_json)
    json_to_html(ag_hymnal_json, output_ag_hymnal_html)
    copytree(
        src=pgm_root / "hymnal/ag/styles",
        dst=pgm_root / "dist/ag/styles",
        dirs_exist_ok=True,
    )
    copytree(
        src=pgm_root / "hymnal/ag/fonts",
        dst=pgm_root / "dist/ag/fonts",
        dirs_exist_ok=True,
    )
    (pgm_root / "dist/lib/reveal.js").mkdir(parents=True, exist_ok=True)

# reason for using __name__ == '__main__'
# ref: https://github.com/pallets/jinja/issues/1239#issuecomment-645231227
