# infrastructure/models.py
from sqlmodel import Field, SQLModel


class ContactModel(SQLModel, table=True):
    __tablename__ = "contacts"
    id: int | None = Field(default=None, primary_key=True)
    mobile: str = Field(unique=True, index=True)
    name: str
