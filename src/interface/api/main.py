from fastapi import FastAPI

from interface.api.v1 import contacts

app = FastAPI(title="Clean Architecture API")

# Registering the contacts router into the main application
app.include_router(contacts.router, prefix="/api/v1/contacts", tags=["Contacts"])