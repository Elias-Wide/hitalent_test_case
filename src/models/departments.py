from datetime import datetime, date
from typing import List, Optional
from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship




class DepartmentsORM(Base):
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
    __tablename__ = "departments"
    __table_args__ = (
        UniqueConstraint(
            "name",
            "parent_id",
            name="uq_department_name_by_parent",
        ),
    )

    name: Mapped[str] = mapped_column(
        String(NAME_MAX_LEN),
        nullable=False,
    )
    parent_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("departments.id", ondelete="CASCADE"), 
        nullable=True
    )
    
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), 
        nullable=False
    )

    parent: Mapped[Optional["Department"]] = relationship(
        "Department", 
        remote_side=[id], 
        back_populates="sub_departments"
    )
    
    sub_departments: Mapped[List["Department"]] = relationship(
        "Department", 
        back_populates="parent"
    )
    
    employees: Mapped[List["Employee"]] = relationship(
        "Employee", 
        back_populates="department", 
        cascade="all, delete-orphan"
    )
