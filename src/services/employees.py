from typing import List, Optional

from src.schemas.employees import EmployeeSchema
from src.services.base import BaseService


class EmployeesService(BaseService):
    """
    Service layer responsible for managing employee business logic.

    All business checks and transaction control via DBManager
    are encapsulated within this layer.
    """

    async def add_employee(self, employee_data: EmployeeSchema) -> int:
        """
        Hire a new employee into a specific department.

        Validates the target department existence before creation.

        Args:
            employee_data: Pydantic schema containing employee details.

        Returns:
            int: The unique identifier of the newly created employee.
        """
        pass

    async def get_all_employees(self) -> List[EmployeeSchema]:
        """
        Retrieve a list of all active employees in the company.

        Returns:
            List[EmployeeSchema]: A list of all validated records.
        """
        pass

    async def get_employee_by_id(
        self, employee_id: int
    ) -> Optional[EmployeeSchema]:
        """
        Find a specific employee by their unique identifier.

        Args:
            employee_id: The ID of the employee to look up.

        Returns:
            Optional[EmployeeSchema]: Validated record or None.
        """
        pass

    async def delete_employee(self, employee_id: int) -> None:
        """
        Terminate an employee's contract and remove their record.

        Args:
            employee_id: The ID of the employee to delete.
        """
        pass

    async def change_department(
        self, employee_id: int, new_department_id: int
    ) -> None:
        """
        Transfer an employee to a different department.

        Validates the employee and target department before updating.

        Args:
            employee_id: The ID of the employee being moved.
            new_department_id: The destination department ID.
        """
        pass
