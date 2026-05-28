from datetime import datetime, date
from typing import List, Optional
from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship



class Employee(Base):
    """
    Represent a company employee.

    Each employee is strictly linked to a specific department.
    The database enforces a RESTRICT constraint, preventing the
    deletion of a department if it contains active employees.

    Attributes:
        department_id (int): Foreign key linking the employee
            to their assigned department.
        full_name (str): Full name of the employee.
        position (str): Job title or position within the company.
        hired_at (date, optional): Date when the employee was
            officially hired.
        created_at (datetime): Automatically generated timestamp
            indicating when the employee record was created.
        department (Department): Relationship to the department
            object this employee belongs to.
    """

    full_name: Mapped[str] = mapped_column(nullable=False)
    position: Mapped[str] = mapped_column(nullable=False)
    hired_at: Mapped[Optional[date]] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), 
        nullable=False
    )

    department: Mapped["Department"] = relationship(
        "Department", 
        back_populates="employees"
    )
