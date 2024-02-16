"""Transform JSON to HTML."""

# standard
from logging import DEBUG, INFO, debug, getLogger
from pathlib import Path
from json import load

# external
from jinja2 import Environment, PackageLoader, select_autoescape

# local
from hymnal.sketch import Hymn


def _json_song_parser(hymn_path: Path, hymnal_name: str):
    """Parse songs from JSON files."""
    with open(file=hymn_path, mode="rb") as json_file:
        hymn = Hymn(**load(json_file))
    if hymn.number == -1:
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
    song_template = (
        (
            "start-at-refrain-without-verses.html.j2"
            if not hymn.verses
            else "start-at-refrain.html.j2"
        )
        if hymn.starts == "refrain"
        else (
            "start-at-verse-without-refrain.html.j2"
            if not hymn.refrain
            else "start-at-verse-with-refrain.html.j2"
        )
    )
    # .render(**kwargs) ignores keys not found in template
    return cathedral.get_template(song_template).render(
        hymn_number=hymn.number,
        hymnal_name=hymnal_name,
        relative_path="..",
        start_tag="<h3>",
        first_verse=hymn.verses[0] if hymn.verses else None,
        verses=hymn.verses if hymn.starts == "refrain" else hymn.verses[1:],
        end_tag="</h3>",
        start_ref_tag="<h3><em>",
        refrain=hymn.refrain,
        end_ref_tag="</em></h3>",
    )


def j2h_transform(source: Path, destination: Path, hymnal_name: str):
    """Convert JSON to HTML."""
    getLogger().setLevel(DEBUG)
    for idx in range(1, 1632):  # NOTE: this is not cool!
        file_name = str(idx).zfill(4)
        hymn_path = source / f"{file_name}.json"
        if not hymn_path.exists() or not hymn_path.is_file():
            continue
        with open(
            file=destination / f"{file_name}.html",
            mode="wt",
            encoding="utf-8",
        ) as html_file:
            html_file.write(_json_song_parser(hymn_path, hymnal_name))
        print(f"Created file {file_name}.html", end="\r")
    debug(" file generation complete\n")
    getLogger().setLevel(INFO)
