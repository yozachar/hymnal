"""
# Converter : HTML <---> JSON
"""
# -*- coding: utf-8 -*-

# standard
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import List
from json import dump

# external
from bs4 import BeautifulSoup


@dataclass
class Stanza:
    """
    Store hymn stanza
    """

    stanza_number: int
    lines: List[str] = field(default_factory=list[str])


@dataclass
class Hymn:
    """
    Store hymn
    """

    hymn_number: int
    chorus: List[str] = field(default_factory=list[str])
    stanzas: List[Stanza] = field(default_factory=list[Stanza])


def song_parser(hymn_file: Path) -> Hymn:
    """
    Parse songs from reveal.js HTML files
    """

    with open(file=hymn_file, mode="rt", encoding="utf-8") as _html_file:
        _html_content = _html_file.read()

    _soup = BeautifulSoup(_html_content, "lxml")
    _hymn_no = int(_hyn.text) if (_hyn := _soup.select_one("h1.hymn-no")) else -1
    hymn = Hymn(hymn_number=_hymn_no)

    for _stanza_section in _soup.select('section[id^="stanza-"]'):
        _stanza_number = (
            int(_szn.text.rstrip("."))
            if (_szn := _stanza_section.select_one("p.stanza-no"))
            else -1
        )
        _lines = [line.text.strip() for line in _stanza_section.select("h3")]
        hymn.stanzas.append(Stanza(stanza_number=_stanza_number, lines=_lines))

    if (chorus_section := _soup.select_one('section[id^="chorus"]')) and (
        _verses := chorus_section.select("em")
    ):
        hymn.chorus = [line.text.strip() for line in _verses]

    return hymn


ag_hymnal_dir = Path(__file__).parent.parent / "static/hymnal/ag"
ag_hymnal_op = Path(__file__).parent / "out"

for idx in range(1, 2001):
    hymn_path = ag_hymnal_dir / f"{str(idx).zfill(4)}.html"
    if hymn_path.exists() and hymn_path.is_file():
        with open(
            file=ag_hymnal_op / f"{str(idx).zfill(4)}.json", mode="wt", encoding="utf-8"
        ) as ag_f:
            dump(obj=asdict(song_parser(hymn_path)), fp=ag_f, ensure_ascii=False)

# pprint(song_parser(ag_hymnal_dir / "0142.html"))
