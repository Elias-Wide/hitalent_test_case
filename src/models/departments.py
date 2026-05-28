from datetime import datetime
from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import ForeignKey, String, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.constants.departments import DEPARTMENTS
from src.db.database import Model

if TYPE_CHECKING:
    from src.models.employees import EmployeesORM


class DepartmentsORM(Model):
    """
    Represent an organizational department.

    Supports a self-referential hierarchical tree structure.
    Deleting a parent department triggers a cascade delete for
    all sub-departments and associated employees.

    Attributes:
        id (int): Unique identifier and primary key.
        name (str): The name of the department.
        parent_id (int, optional): Foreign key pointing to the
            parent department's ID. None for top-level root.
        created_at (datetime): Automatically generated timestamp
            indicating when the department record was created.
        parent (Department, optional): Relationship to the parent
            department object.
        sub_departments (list[Department]): Relationship to all
            child departments nested under this department.
        employees (list[Employee]): Relationship to all employees
            assigned to this specific department.
    """

    __tablename__ = 'departments'
    __table_args__ = (
        UniqueConstraint(
            'name',
            'parent_id',
            name='uq_department_name_by_parent',
        ),
    )

    name: Mapped[str] = mapped_column(
        String(length=DEPARTMENTS.NAME_MAX_LEN),
        nullable=False,
    )
    parent_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey('departments.id', ondelete='CASCADE'), nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), nullable=False
    )

    parent: Mapped[Optional['DepartmentsORM']] = relationship(
        'departments', remote_side=[id], back_populates='children'
    )

    children: Mapped[List['DepartmentsORM']] = relationship(
        'departments', back_populates='parent'
    )

    employees: Mapped[List['EmployeesORM']] = relationship(
        'employees', back_populates='department', cascade='all, delete-orphan'
    )
