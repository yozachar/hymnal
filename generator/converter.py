"""
# Converter : HTML <---> JSON
"""
# -*- coding: utf-8 -*-

# standard
from dataclasses import dataclass, field
from typing import List
from pprint import pprint

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


with open(file="generator/type3.html", mode="rt", encoding="utf-8") as html_file:
    html_content = html_file.read()

soup = BeautifulSoup(html_content, "lxml")

hymn_no = int(hyn.text) if (hyn := soup.select_one("h1.hymn-no")) else -1

hymn = Hymn(hymn_number=hymn_no)

for stanza_section in soup.select('section[id^="stanza-"]'):
    stanza_number = (
        int(szn.text.rstrip("."))
        if (szn := stanza_section.select_one("p.stanza-no"))
        else -1
    )
    lines = [line.text for line in stanza_section.select("h3")]
    hymn.stanzas.append(Stanza(stanza_number=stanza_number, lines=lines))

if chorus_section := soup.select_one('section[id^="chorus"]'):
    hymn.chorus = [line.text for line in chorus_section.select("h3")]

pprint(hymn)
