from fastapi import HTTPException, status

from src.core.messages.api.base import ApiErrorMessages


class APIException(HTTPException):
    """
    Base HTTP exception for consistent application API responses.
    """

    STATUS_CODE: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    DETAIL: str = ApiErrorMessages.INTERNAL_SERVER_ERROR

    def __init__(self, detail: str = None, status_code: int = None):
        self.status_code = status_code or self.STATUS_CODE
        self.detail = detail or self.DETAIL
        super().__init__(status_code=self.status_code, detail=self.detail)


class DepartmentServiceAPIException(APIException):
    """
    Generic API exception for unhandled department service errors.
    """

    STATUS_CODE = status.HTTP_400_BAD_REQUEST
    DETAIL = 'Department business rule violation occurred.'


class DepartmentNotFoundAPIException(DepartmentServiceAPIException):
    """
    API exception when the requested department cannot be found.
    """

    STATUS_CODE = status.HTTP_404_NOT_FOUND
    DETAIL = 'Department with this ID does not exist.'


class DepartmentConflictAPIException(DepartmentServiceAPIException):
    """
    API exception when a department name already exists on the level.
    """

    STATUS_CODE = status.HTTP_409_CONFLICT
    DETAIL = 'Department with this name already exists on that level.'


class DepartmentSelfReferenceAPIException(DepartmentServiceAPIException):
    """
    API exception when a department attempts to set itself as a parent.
    """

    STATUS_CODE = status.HTTP_409_CONFLICT
    DETAIL = (
        'A department cannot be its own parent or a child of his own tree.'
    )


class DepartmentValidationAPIException(DepartmentServiceAPIException):
    """
    API exception when the provided department data is invalid.
    """

    STATUS_CODE = status.HTTP_400_BAD_REQUEST
    DETAIL = 'Provided department data is invalid.'


class EmployeeServiceAPIException(APIException):
    """
    Generic API exception for unhandled employee service errors.
    """

    STATUS_CODE = status.HTTP_400_BAD_REQUEST
    DETAIL = 'Employee service violation occurred.'


class EmployeeNotFoundAPIException(EmployeeServiceAPIException):
    """
    API exception when the requested employee cannot be found.
    """

    STATUS_CODE = status.HTTP_404_NOT_FOUND
    DETAIL = 'Employee with this ID does not exist.'


class EmployeeConflictAPIException(EmployeeServiceAPIException):
    """
    API exception when an employee email or passport already exists.
    """

    STATUS_CODE = status.HTTP_409_CONFLICT
    DETAIL = 'Employee with this data already exists.'


class EmployeeValidationAPIException(EmployeeServiceAPIException):
    """
    API exception when the provided employee data violates rules.
    """

    STATUS_CODE = status.HTTP_400_BAD_REQUEST
    DETAIL = 'Provided employee data violates business rules.'
