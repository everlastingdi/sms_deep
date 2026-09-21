"""Opportunity data model."""

from dataclasses import asdict, dataclass, field

STATUSES = ("open", "watching", "done")


@dataclass
class Opportunity:
    name: str
    chain: str = ""
    category: str = ""
    link: str = ""
    status: str = "open"
    notes: list = field(default_factory=list)
    created: str = ""
    updated: str = ""

    def __post_init__(self):
        if not self.name:
            raise ValueError("name is required")
        if self.status not in STATUSES:
            raise ValueError(f"invalid status: {self.status}")

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
