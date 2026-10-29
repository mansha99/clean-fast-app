# use_cases/authenticate_contact.py

from domain.contacts.entities import Contact
from domain.contacts.ports import ContactRepositoryPort


class ListContactsUseCase:
    def __init__(self, contact_repo: ContactRepositoryPort):
        self.contact_repo = contact_repo

    async def execute(self) -> list[Contact]:
        return await self.contact_repo.list_all()
