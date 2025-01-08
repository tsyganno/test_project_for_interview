from fastapi import HTTPException


class UserExists(HTTPException):
    def __init__(self, detail: str = 'Error! User already exists.', status_code: int = 400):
        super().__init__(detail=detail, status_code=status_code)


class UserNotFoundException(HTTPException):
    def __init__(self, detail: str = 'Error! The user was not found.', status_code: int = 400):
        super().__init__(detail=detail, status_code=status_code)
