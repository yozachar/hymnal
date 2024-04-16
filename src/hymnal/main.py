"""Hymnal Generator."""

# standard
from shutil import copytree
from subprocess import run
from pathlib import Path

# local
from hymnal.json2html import j2h_transform

# from hymnal.html2json import h2j_transform


def transform(program_root: Path, slug: str, hymnal_name: str):
    base = "static"
    # temporary_source_hymnal_html = program_root / f"hymnal/temp/{slug}/html"
    hymnal_json = program_root / f"hymnal/{slug}"
    # hymnal_json.mkdir(parents=True, exist_ok=True)
    output_hymnal_html = program_root / f"{base}/{slug}"
    output_hymnal_html.mkdir(parents=True, exist_ok=True)
    # h2j_transform(temporary_source_hymnal_html, hymnal_json)
    j2h_transform(hymnal_json, output_hymnal_html, hymnal_name)
    for asset_dirs in ("styles", "fonts"):
        # $ ln -rs $(pwd)/hymnal/assets/styles $(pwd)/hymnal/{slug}/styles
        copytree(
            src=program_root / f"hymnal/{slug}/{asset_dirs}",
            dst=program_root / f"{base}/{slug}/{asset_dirs}",
            dirs_exist_ok=True,
        )
    presenter_lib = program_root / f"{base}/lib/reveal.js"
    presenter_lib.mkdir(parents=True, exist_ok=True)
    if any(presenter_lib.iterdir()):
        run(
            [
                "git",
                "-C",
                presenter_lib,
                "pull",
                "https://github.com/hakimel/reveal.js.git",
            ]
        )
    else:
        run(
            [
                "git",
                "clone",
                "--depth",
                "1",
                "https://github.com/hakimel/reveal.js.git",
                presenter_lib,
            ]
        )


if __name__ == "__main__":
    source_root = Path(__file__).parent.parent.parent
    for slug, hymnal_name in {
        "ag": "ആത്മീയ ഗീതങ്ങൾ",
        # "other": "Other",
        # "yth": "Youth Program",
        # "cnv": "Convention",
    }.items():
        transform(source_root, slug, hymnal_name)


# reason for using __name__ == '__main__'
# ref: https://github.com/pallets/jinja/issues/1239#issuecomment-645231227
