from typing import Annotated

from fastapi import APIRouter, Depends, Response, status

from src.dependencies.db_manager import DBManagerDep
from src.schemas.departments import SDepartmentsCreate, SDepartmentsResponse
from src.services.departments import DepartmentsService

router = APIRouter(prefix='/departments', tags=['departments'])


@router.post(
    '',
    response_model=SDepartmentsResponse,
    status_code=status.HTTP_201_CREATED,
    summary='Create a new department',
)
async def create_department(
    db: DBManagerDep, department: Annotated[SDepartmentsCreate, Depends()]
):
    service = DepartmentsService(db)
    new_department = await service.create_department(department)
    return SDepartmentsResponse.model_validate(new_department)


@router.get(
    '/',
    response_model=list[SDepartmentsResponse],
    summary='Get all departments',
)
async def get_all_departments(db: DBManagerDep) -> list[SDepartmentsResponse]:
    service = DepartmentsService(db)
    return await service.get_all_departments()


@router.get(
    '/{department_id}',
    response_model=SDepartmentsResponse,
    summary='Get department by ID',
)
async def get_department(
    db: DBManagerDep, department_id: int
) -> SDepartmentsResponse:
    service = DepartmentsService(db)
    department = await service.get_department_by_id(department_id)
    if not department:
        return Response(
            status_code=status.HTTP_404_NOT_FOUND,
            content={'detail': 'Department not found'},
        )
    return SDepartmentsResponse.model_validate(department)


# @router.patch(
#     '/{department_id}',
#     response_model=SDepartmentsResponse,
#     summary='Partially update a department by ID',
# )
# async def update_department(
#     department_id: int, department_data: SDepartmentsUpdate
# ):
#     # TODO: get existing record from DB and update
#     ...
