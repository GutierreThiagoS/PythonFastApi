from pydantic import BaseModel


class LoginOut(BaseModel):
    access_token: str
    token_type: str = 'bearer'
    message: str
