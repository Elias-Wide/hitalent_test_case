from src.models.departments import DepartmentsORM
from src.repositories.base import SQLAlchemyRepository


class DepartmentsRepo(SQLAlchemyRepository):
    """
    Repository for managing Department records.

    Inherits core CRUD operations and implements custom recursive
    Common Table Expressions (CTE) for tree traversal.
    """

    model = DepartmentsORM
