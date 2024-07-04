from decimal import Decimal
from enum import Enum

from pydantic import BaseModel


class ContasReceberStatus(str, Enum):
    PAGAR = 'PAGAR'
    RECEBER = 'RECEBER'


class ContasPagarReceberRequest(BaseModel):
    descricao: str
    valor: Decimal
    tipo: ContasReceberStatus   # PAGAR, RECEBER

