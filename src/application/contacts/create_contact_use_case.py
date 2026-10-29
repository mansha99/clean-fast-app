# use_cases/authenticate_contact.py
from domain.contacts.entities import Contact
from domain.contacts.exceptions import ContactExistException
from domain.contacts.ports import ContactRepositoryPort


class CreateContactUseCase:
    def __init__(self, contact_repo: ContactRepositoryPort):
        self.contact_repo = contact_repo

    async def execute(self, mobile: str, name: str) -> str:
        if await self.contact_repo.find_by_mobile(mobile=mobile) is not None:
            raise ContactExistException(f"Contact {mobile} already exist")
        record = Contact(mobile=mobile, name=name, id=0)
        return await self.contact_repo.save(record)
