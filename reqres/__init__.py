from dataclasses import dataclass
from typing import List


@dataclass
class User:
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


@dataclass
class Page:
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[User]


@dataclass
class NewUser:
    createdAt: str
    id: str
    job: str
    name: str
