from pydantic import BaseModel


class LoginIn(BaseModel):
    username: str
    password: str
    keep_connected: bool
