from src.models.employees import EmployeesORM
from src.repositories.base import SQLAlchemyRepository
from src.schemas.employees import SEmployeesBase


class EmployeesRepository(SQLAlchemyRepository[EmployeesORM, SEmployeesBase]):
    """
    Repository for managing Employee records.

    Inherits core CRUD operations and implements batch filtering
    utilities to support decoupled department-employee operations.
    """

    model = EmployeesORM
