from typing import List
from src.models.employees import EmployeesORM
from src.repositories.base import SQLAlchemyRepository

class EmployeesRepository(
    SQLAlchemyRepository[EmployeesORM, SEmployees]
):
    """
    Repository for managing Employee records.

    Inherits core CRUD operations and implements batch filtering
    utilities to support decoupled department-employee operations.
    """

    model = EmployeesORM
