from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class SDepartmentsBase(BaseModel):
    """Base schema with shared department attributes."""

    name: str = Field(
        ..., description="The name of the department", min_length=1
    )
    parent_id: Optional[int] = Field(
        None, description="Parent department ID if nested", gt=0
    )


class SDepartmentsCreate(SDepartmentsBase):
    """Schema for validating data on department creation."""

    pass


class SDepartmentsResponse(SDepartmentsBase):
    """Schema for serializing department data for API responses."""

    id: int = Field(..., description="Unique department ID")
    created_at: datetime = Field(
        ..., description="Timestamp when the department was created"
    )

    model_config = ConfigDict(from_attributes=True)
