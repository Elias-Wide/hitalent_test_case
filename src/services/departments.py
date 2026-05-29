from typing import List, Optional
from src.schemas.departments import (
    SDepartments,
    SDepartmentsTreeResponse,
)
from src.services.base import BaseService


class DepartmentsService(BaseService):
    """
    Service layer responsible for managing department business logic.

    Handles hierarchical tree operations, anti-cyclical cycle
    validations, and cascade deletion verifications.
    """

    async def create_department(
        self, department_data: SDepartments
    ) -> int:
        """
        Create a new organizational department.

        Ensures unique constraints for names under the same parent.

        Args:
            department_data: Validated department creation attributes.

        Returns:
            int: The unique identifier of the created department.
        """
        pass

    async def get_all_departments(self) -> List[SDepartments]:
        """
        Retrieve a flat list of all active departments.

        Returns:
            List[DepartmentSchema]: A list of all validated records.
        """
        pass

    async def get_department_by_id(
        self, department_id: int
    ) -> Optional[SDepartments]:
        """
        Find a specific department by its unique identifier.

        Args:
            department_id: The ID of the department to look up.

        Returns:
            Optional[DepartmentSchema]: Validated record or None.
        """
        pass

    async def get_department_tree(
        self, department_id: int, depth: int = 1
    ) -> SDepartmentsTreeResponse:
        """
        Fetch a recursive sub-tree starting from the target department.

        Limits the lookup depth between 1 and 5 using DB-level CTE.

        Args:
            department_id: Root node ID of the requested hierarchy.
            depth: Level of nesting to fetch downwards (defaults to 1).

        Returns:
            DepartmentTreeResponse: Hierarchical tree Pydantic schema.
        """
        pass

    async def move_department(
        self, department_id: int, new_parent_id: Optional[int]
    ) -> None:
        """
        Relocate a department to a new parent node in the tree.

        Performs strict recursive validation to prevent any cyclical
        dependencies (e.g., preventing a parent from becoming a child
        of its own sub-department).

        Args:
            department_id: The ID of the department being moved.
            new_parent_id: Target parent department ID or None for root.
        """
        pass

    async def delete_department(self, department_id: int) -> None:
        """
        Remove a department record along with its whole branch.

        Triggers a cascade delete for all sub-departments and
        associated employees via DB rules.

        Args:
            department_id: The ID of the department to delete.
        """
        pass
