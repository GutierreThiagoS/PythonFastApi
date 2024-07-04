from fastapi import APIRouter

from app.users.models.login_in import LoginIn
from app.users.models.login_out import LoginOut

router = APIRouter(prefix='/users')


@router.post('/login')
async def login(login_in: LoginIn) -> LoginOut:
    if len(login_in.password) > 0 and len(login_in.username) > 0:
        return LoginOut(
            access_token='jdfnbviubdefuvgsdovihreoihrvioervkcnvirhieurijresd',
            message='Usuário autenticado com sucesso!'
        )
    else:
        raise {
            "detail": "Usuário ou senha inválidos",
            "status_code": 401
        }

