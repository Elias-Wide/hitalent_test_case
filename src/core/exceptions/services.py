from src.core.exceptions.base import AppError


class ServiceError(AppError):
    """Base exception for all service layer business logic."""

    msg = 'Business logic error occurred.'


# Departments


class DepartmentServiceError(ServiceError):
    """Base exception for department business logic."""


class DepartmentNotFoundError(DepartmentServiceError):
    msg = 'Department with this ID does not exist.'


class DepartmentAlreadyExistsError(DepartmentServiceError):
    msg = 'Department with this name already exists in this branch.'


class DepartmentSelfReferenceError(DepartmentServiceError):
    msg = 'A department cannot be its own parent.'


class DepartmentValidationError(DepartmentServiceError):
    msg = 'Provided department data is invalid.'


# Employees


class EmployeeServiceError(ServiceError):
    """Base exception for employee business logic."""


class EmployeeNotFoundError(EmployeeServiceError):
    msg = 'Employee with this ID does not exist.'


class EmployeeAlreadyExistsError(EmployeeServiceError):
    msg = 'Employee with this email or passport already exists.'


class EmployeeValidationError(EmployeeServiceError):
    msg = 'Provided employee data violates business rules.'
