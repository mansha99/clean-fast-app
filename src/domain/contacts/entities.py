# domain/entities.py
from dataclasses import dataclass


@dataclass
class Contact:
    id: str | None
    name: str
    mobile: str

