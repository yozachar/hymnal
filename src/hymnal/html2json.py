"""Transform HTML to JSON."""

# standard
from dataclasses import asdict
from pathlib import Path
from json import dump

# external
from bs4 import BeautifulSoup

# local
from hymnal.sketch import Hymn, Verse


def _html_song_parser(hymn_file: Path):
    """Parse songs from reveal.js HTML files."""
    with open(file=hymn_file, mode="rt", encoding="utf-8") as html_file:
        html_content = html_file.read()
    soup = BeautifulSoup(html_content, "lxml")
    hymn = Hymn()
    if hymn_number_tag := soup.select_one("h1.hymn-no"):
        hymn.number = int(hymn_number_tag.text)
    hymn.starts = (
        "refrain"
        if '<section id="refrain" class="start-here">' in html_content
        else "verse-1"
    )
    for each_verse in soup.select('section[id^="verse-"]'):
        verse_number = (
            int(verse_number_tag.text.rstrip("."))
            if (verse_number_tag := each_verse.select_one("p.verse-no"))
            else -1
        )
        lines = [line_tag.text.strip() for line_tag in each_verse.select("h3")]
        lines.extend([line_tag.text.strip() for line_tag in each_verse.select("h4")])
        hymn.verses.append(Verse(number=verse_number, lines=lines))
    if (refrain_tag := soup.select_one('section[id^="refrain"]')) and (
        refrain := refrain_tag.select("em")
    ):
        hymn.refrain = [line_tag.text.strip() for line_tag in refrain]
    hymn.verses.sort(key=lambda verses: verses.number)
    return hymn


def h2j_transform(source: Path, destination: Path):
    """Convert HTML to JSON."""
    for idx in range(1, 1632):
        hymn_path = source / f"{str(idx).zfill(4)}.html"
        if not hymn_path.exists() or not hymn_path.is_file():
            continue
        with open(
            file=destination / f"{str(idx).zfill(4)}.json",
            mode="wt",
            encoding="utf-8",
        ) as json_file:
            dump(
                obj=asdict(_html_song_parser(hymn_path)),
                fp=json_file,
                ensure_ascii=False,
            )
