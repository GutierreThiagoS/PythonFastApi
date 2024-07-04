
import uvicorn
from fastapi import FastAPI

from app.contas_a_pagar_e_receber.routers import contas_a_pagar_e_receber_router
from app.site import site_controller
from shared.database import engine, Base

from app.contas_a_pagar_e_receber.models.contas_a_pagar_receber_model import ContasPagarReceber


# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)

app = FastAPI()

print("API Rodando")

app.include_router(contas_a_pagar_e_receber_router.router)
app.include_router(site_controller.router)


if __name__ == "__main__":
    uvicorn.run(app, host="192.168.203.56", port=8443)
