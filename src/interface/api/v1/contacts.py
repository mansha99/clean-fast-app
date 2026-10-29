# api/routes.py

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi import APIRouter, Depends, status
from application.contacts.create_contact_use_case import CreateContactUseCase
from application.contacts.list_contacts_use_case import ListContactsUseCase
from domain.contacts.exceptions import ContactExistException
from interface.dependencies import (
    get_create_contact_use_case,
    get_list_contacts_use_case,
)
from interface.schemas import SaveContactRequest

router = APIRouter()


@router.post("")
async def save(
    payload: SaveContactRequest,
    create_use_case: CreateContactUseCase = Depends(get_create_contact_use_case),
    list_contacts_use_case: ListContactsUseCase = Depends(get_list_contacts_use_case),
) :
    try:
        await create_use_case.execute(payload.mobile, payload.name)
        return await list_contacts_use_case.execute()
    except ContactExistException as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e)
        )


@router.get("")
async def list_all(
    list_contacts_use_case: ListContactsUseCase = Depends(get_list_contacts_use_case),
):
    return await list_contacts_use_case.execute()
