# infrastructure/contacts/repositories.py

from collections.abc import AsyncGenerator

from fastapi import Depends
from sqlmodel import select

# from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel.ext.asyncio.session import AsyncSession

from domain.contacts.entities import Contact
from domain.contacts.ports import ContactRepositoryPort
from infrastructure.contacts.models import ContactModel
from infrastructure.shared.database import get_session


class SqlModelContactRepository(ContactRepositoryPort):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def find_by_mobile(self, mobile: str) -> Contact | None:
        statement = select(ContactModel).where(ContactModel.mobile == mobile)
        results = await self.session.exec(statement)
        db_contact = results.first()
        if not db_contact:
            return None

        # Map DB model back to Pure Domain Entity
        return Contact(
            id=db_contact.id,
            mobile=db_contact.mobile,
            name=db_contact.name,
        )

    async def save(self, contact: Contact) -> Contact:
        db_contact = ContactModel(mobile=contact.mobile, name=contact.name)
        self.session.add(db_contact)
        await self.session.commit()
        await self.session.refresh(db_contact)
        contact.id = db_contact.id
        return contact

    async def list_all(self) -> list[Contact]:
        statement = select(ContactModel)
        result = await self.session.exec(statement)
        return result.all()


async def get_async_contact_repo(session: AsyncSession = Depends(get_session)) -> AsyncGenerator[ContactRepositoryPort, None]:
        yield SqlModelContactRepository(session)
        