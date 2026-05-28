from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class SEmployeesBase(BaseModel):
    """Base schema with shared employee attributes."""

    full_name: str = Field(
        ..., description="Full name of the employee", min_length=1
    )
    position: str = Field(
        ..., description="Job title or position", min_length=1
    )
    hired_at: Optional[date] = Field(None, description="Official hire date")
    department_id: int = Field(
        ..., description="FK for the department", gt=0
    )


class SEmployeesCreate(EmployeeBase):
    """Schema for validating data on employee creation."""

    pass


class SEmployeesResponse(EmployeeBase):
    """Schema for serializing employee data for API responses."""

    id: int = Field(..., description="Unique internal employee ID")
    created_at: datetime = Field(
        ..., description="Timestamp when the record was created"
    )

    model_config = ConfigDict(from_attributes=True)
