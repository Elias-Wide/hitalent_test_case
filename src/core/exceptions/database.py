from src.core.exceptions.base import AppError


class DatabaseError(AppError):
    """Base exception for all database layer operations."""

    msg = 'Database operation failed.'


class DBUniqueViolationError(DatabaseError):
    """Raised when a unique constraint or index is violated."""

    msg = 'Database record already exists.'


class DBIntegrityError(DatabaseError):
    """Raised when foreign key or check constraints fail."""

    msg = 'Database integrity constraint violated.'


class DBOperationError(DatabaseError):
    """Raised for connection timeouts or internal query failures."""

    msg = 'Internal database execution error.'
