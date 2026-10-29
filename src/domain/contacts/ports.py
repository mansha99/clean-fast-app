# domain/interfaces.py
from abc import ABC, abstractmethod

from domain.contacts.entities import Contact


class ContactRepositoryPort(ABC):
    @abstractmethod
    async def find_by_mobile(self, mobile: str) -> Contact | None:
        pass

    @abstractmethod
    async def save(self, contact: Contact) -> Contact:
        pass

    @abstractmethod
    async def list_all(self) -> list[Contact]:
        pass
