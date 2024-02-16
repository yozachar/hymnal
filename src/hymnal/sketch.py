"""Blueprint of a hymn structure."""

# standard
from dataclasses import dataclass, field


@dataclass
class Verse:
    """Verse."""

    number: int = -1
    lines: list[str] = field(default_factory=list[str])


@dataclass
class Hymn:
    """Hymn."""

    number: int = -1
    writer: str = ""
    starts: str = ""
    refrain: list[str] = field(default_factory=list[str])
    verses: list[Verse] = field(default_factory=list[Verse])
