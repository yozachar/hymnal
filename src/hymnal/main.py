"""Hymnal Generator."""

# standard
from dataclasses import dataclass, field
from json import load
from shutil import copytree
from pathlib import Path
from typing import List
from os import getenv

# # standard dev
# from dataclasses import asdict
# from json import dump

# external
from jinja2 import Environment, PackageLoader, select_autoescape

# # external dev
# from bs4 import BeautifulSoup


@dataclass
class Verse:
    """Verse."""

    number: int = -1
    lines: List[str] = field(default_factory=list[str])


@dataclass
class Hymn:
    """Hymn."""

    number: int = -1
    writer: str = ""
    starts: str = ""
    refrain: List[str] = field(default_factory=list[str])
    verses: List[Verse] = field(default_factory=list[Verse])


############################## HTML->JSON ##############################


# def _html_song_parser(hymn_file: Path):
#     """Parse songs from reveal.js HTML files."""
#     with open(file=hymn_file, mode="rt", encoding="utf-8") as html_file:
#         html_content = html_file.read()
#     soup = BeautifulSoup(html_content, "lxml")
#     hymn = Hymn()
#     if hymn_number_tag := soup.select_one("h1.hymn-no"):
#         hymn.number = int(hymn_number_tag.text)
#     hymn.starts = (
#         "refrain"
#         if '<section id="refrain" class="start-here">' in html_content
#         else "verse-1"
#     )
#     for each_verse in soup.select('section[id^="verse-"]'):
#         verse_number = (
#             int(verse_number_tag.text.rstrip("."))
#             if (verse_number_tag := each_verse.select_one("p.verse-no"))
#             else -1
#         )
#         lines = [line_tag.text.strip() for line_tag in each_verse.select("h3")]
#         lines.extend([line_tag.text.strip() for line_tag in each_verse.select("h4")])
#         hymn.verses.append(Verse(number=verse_number, lines=lines))
#     if (refrain_tag := soup.select_one('section[id^="refrain"]')) and (
#         refrain := refrain_tag.select("em")
#     ):
#         hymn.refrain = [line_tag.text.strip() for line_tag in refrain]
#     hymn.verses.sort(key=lambda verses: verses.number)
#     return hymn


# def html_to_json(source: Path, destination: Path):
#     """Convert HTML to JSON."""
#     for idx in range(1, 2001):
#         hymn_path = source / f"{str(idx).zfill(4)}.html"
#         if not hymn_path.exists() or not hymn_path.is_file():
#             continue
#         with open(
#             file=destination / f"{str(idx).zfill(4)}.json",
#             mode="wt",
#             encoding="utf-8",
#         ) as json_file:
#             dump(
#                 obj=asdict(_html_song_parser(hymn_path)),
#                 fp=json_file,
#                 ensure_ascii=False,
#             )


############################## JSON->HTML ##############################


def _json_song_parser(hymn_path: Path, hymnal_name: str):
    """Parse songs from JSON files."""
    with open(file=hymn_path, mode="rb") as json_file:
        hymn = Hymn(**load(json_file))
    if hymn.number == -1 or len(hymn.verses) < 1:
        return (
            "<html>"
            + "<head><title>BAD FILE</title></head>"
            + f"<body><p>Bad File Error: {hymn_path}</p><body>"
            + "</html>"
        )
    cathedral = Environment(
        loader=PackageLoader("main"),
        autoescape=select_autoescape(),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    common_args = {
        "hymnal": hymnal_name,
        "hymn_number": hymn.number,
        "start_tag": "<h3>",
        "end_tag": "</h3>",
        "relative_path": "..",
    }
    if not hymn.refrain:
        return cathedral.get_template("start-at-verse-without-refrain.html.j2").render(
            # main section
            verses=hymn.verses[1:],
            # side section
            first_verse=hymn.verses[0],
            # common
            **common_args,
        )
    if hymn.starts == "refrain":
        return cathedral.get_template("start-at-refrain.html.j2").render(
            # main section
            verses=hymn.verses,
            # side section
            refrain=hymn.refrain,
            start_ref_tag="<h3><em>",
            end_ref_tag="</em></h3>",
            # common
            **common_args,
        )
    return cathedral.get_template("start-at-verse-with-refrain.html.j2").render(
        # main section
        first_verse=hymn.verses[0],
        verses=hymn.verses[1:],
        # side section
        refrain=hymn.refrain,
        start_ref_tag="<h3><em>",
        end_ref_tag="<h3><em>",
        # common
        **common_args,
    )


def json_to_html(source: Path, destination: Path, hymnal_name: str):
    """Convert JSON to HTML."""
    for idx in range(1, 2001):
        hymn_path = source / f"{str(idx).zfill(4)}.json"
        if not hymn_path.exists() or not hymn_path.is_file():
            continue
        with open(
            file=destination / f"{str(idx).zfill(4)}.html",
            mode="wt",
            encoding="utf-8",
        ) as html_file:
            html_file.write(_json_song_parser(hymn_path, hymnal_name))


def genesis(program_root: Path, slug: str, hymnal_name: str):
    base = "dist/" if getenv("CI", "false") == "true" else "dist/hymnal/"
    # temporary_source_hymnal_html = program_root / f"hymnal/temp/{slug}/html"
    hymnal_json = program_root / f"hymnal/{slug}"
    # hymnal_json.mkdir(parents=True, exist_ok=True)
    output_hymnal_html = program_root / f"{base}{slug}"
    output_hymnal_html.mkdir(parents=True, exist_ok=True)
    # html_to_json(temporary_source_hymnal_html, hymnal_json)
    json_to_html(hymnal_json, output_hymnal_html, hymnal_name)
    for asset_dirs in ("styles", "fonts"):
        # $ ln -rs $(pwd)/hymnal/assets/styles $(pwd)/hymnal/{slug}/styles
        copytree(
            src=program_root / f"hymnal/{slug}/{asset_dirs}",
            dst=program_root / f"{base}{slug}/{asset_dirs}",
            dirs_exist_ok=True,
        )
    (program_root / f"{base}lib/reveal.js").mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    source_root = Path(__file__).parent.parent.parent
    for slug, hymnal_name in {
        "ag": "Athmeeya Geethangal",
        # "yth": "Youth Program",
        # "cnv": "Convention",
    }.items():
        genesis(source_root, slug, hymnal_name)


# reason for using __name__ == '__main__'
# ref: https://github.com/pallets/jinja/issues/1239#issuecomment-645231227
