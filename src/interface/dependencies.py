# interface/dependencies.py
from fastapi import Depends

from application.contacts.create_contact_use_case import CreateContactUseCase
from application.contacts.list_contacts_use_case import ListContactsUseCase
from infrastructure.contacts.repositories import SqlModelContactRepository, get_async_contact_repo


def get_create_contact_use_case(
    repo: SqlModelContactRepository = Depends(get_async_contact_repo),
) -> CreateContactUseCase:
    return CreateContactUseCase(contact_repo=repo)

def get_list_contacts_use_case(
    repo: SqlModelContactRepository = Depends(get_async_contact_repo),
) -> ListContactsUseCase:
    return ListContactsUseCase(contact_repo=repo)
