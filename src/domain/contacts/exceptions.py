# domain/contacts/exceptions.py
class DomainException(Exception):
    """Base class for all domain violations."""


class ContactExistException(DomainException):
    """Base class for all domain violations."""
