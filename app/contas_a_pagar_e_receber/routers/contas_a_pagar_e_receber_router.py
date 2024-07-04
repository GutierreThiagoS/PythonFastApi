from http.client import HTTPException
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.contas_a_pagar_e_receber.models.contas_a_pagar_receber_model import ContasPagarReceber
from app.contas_a_pagar_e_receber.models.contas_pagar_receber_request import ContasPagarReceberRequest, ContasReceberStatus
from app.contas_a_pagar_e_receber.models.contas_pagar_receber_response import ContasPagarReceberResponse
from shared.dependecies import get_db

router = APIRouter(prefix='/contas-a-pagar-e-receber')


@router.get("", response_model=List[ContasPagarReceberResponse])
def listar_contas(db: Session = Depends(get_db)) -> List[ContasPagarReceberResponse]:

    return db.query(ContasPagarReceber).all()



@router.post("", response_model=ContasPagarReceberResponse, status_code=201)
def criar_conta(
        contas_a_pagar_e_receber_request: ContasPagarReceberRequest,
        db: Session = Depends(get_db)
) -> ContasPagarReceberResponse:

    contas_a_pagar_e_receber = ContasPagarReceber(
        descricao=contas_a_pagar_e_receber_request.descricao,
        valor=contas_a_pagar_e_receber_request.valor,
        tipo=contas_a_pagar_e_receber_request.tipo
    )

    db.add(contas_a_pagar_e_receber)
    db.commit()
    db.refresh(contas_a_pagar_e_receber)

    return contas_a_pagar_e_receber


