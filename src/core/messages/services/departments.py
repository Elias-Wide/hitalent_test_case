class DepartmentsLogMessages:
    LOG_CREATE_DEPT_ERR = 'Failed to create department: {error}'
    LOG_FETCH_ALL_DEPT_ERR = 'Failed to fetch all departments: {error}'
    LOG_FETCH_ID_DEPT_ERR = (
        'Failed to fetch department by id {dept_id}: {error}'
    )


class DepartmentsErrorMessages:
    ERR_CREATE_DEPT_FAILED = 'Could not create department.'
    ERR_FETCH_ALL_DEPT_FAILED = 'Could not retrieve departments list.'
    ERR_FETCH_ID_DEPT_FAILED = 'Could not retrieve department details.'
    ERR_UQ_DEPT_NAME_BY_PARENT = (
        "Department with the name '{name}' already exists at this "
        'hierarchy level.'
    )
