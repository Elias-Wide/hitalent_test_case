from fastapi import APIRouter, status
from src.schemas.departments import (
    DepartmentCreate,
    DepartmentResponse,
    DepartmentUpdate,
)

router = APIRouter(prefix="/departments", tags=["departments"])


@router.post(
    "",
    response_model=DepartmentResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new department",
)
async def create_department(department: DepartmentCreate):
    # TODO: Add database insertion logic here
    return {"id": 1, **department.model_dump()}


@router.get(
    "/{department_id}",
    response_model=DepartmentResponse,
    summary="Get department by ID",
)
async def get_department(department_id: int):
    # TODO: get from DB. Raise HTTPException(404) if not found
    return {
        "id": department_id,
        "name": "R&D",
        "description": "Research and Development",
    }


@router.patch(
    "/{department_id}",
    response_model=DepartmentResponse,
    summary="Partially update a department by ID",
)
async def update_department(
    department_id: int, department_data: DepartmentUpdate
):
    # TODO: get existing record from DB and update
    ...


@router.delete(
    "/{department_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a department by ID",
)
async def delete_department(department_id: int):
    return None


@router.post(
    "/{department_id}/employees",
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create an employee within a specific department",
)
async def create_employee(department_id: int, employee: EmployeeCreate):
    ...
