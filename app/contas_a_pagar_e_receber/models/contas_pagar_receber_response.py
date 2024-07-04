from decimal import Decimal

from pydantic import BaseModel

from app.contas_a_pagar_e_receber.models.contas_pagar_receber_request import ContasReceberStatus


class ContasPagarReceberResponse(BaseModel):
    id: int
    descricao: str
    valor: Decimal
    tipo: ContasReceberStatus   # PAGAR, RECEBER

