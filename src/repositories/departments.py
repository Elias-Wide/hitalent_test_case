from src.models.departments import DepartmentsORM
from src.repositories.base import SQLAlchemyRepository
from src.schemas.departments import SDepartmentsCreate


class DepartmentsRepo(SQLAlchemyRepository):
    """
    Repository for managing Department records.

    Inherits core CRUD operations and implements custom recursive
    Common Table Expressions (CTE) for tree traversal.
    """

    model = DepartmentsORM

    async def add_one(
        self, department_data: SDepartmentsCreate
    ) -> DepartmentsORM:
        """
        Add a new department to the database.

        Args:
            department_data: Validated data for creating a department.

        Returns:
            DepartmentsORM: The created department record.
        """
        obj = await super().add_one(department_data)
        await self.session.commit()
        return obj
