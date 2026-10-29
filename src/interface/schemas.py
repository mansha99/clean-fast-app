

from pydantic import BaseModel, Field

from domain.contacts.entities import Contact


class SaveContactRequest(BaseModel):
    mobile: str = Field(..., min_length=10, pattern=r"^[1-9]{1}[0-9]{9}$")
    name: str = Field(..., min_length=3)


