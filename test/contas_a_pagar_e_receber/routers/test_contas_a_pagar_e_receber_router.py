from fastapi.testclient import TestClient

from app.contas_a_pagar_e_receber.models.contas_pagar_receber_request import ContasReceberStatus
from main import app

client = TestClient(app)


def test_deve_listar_contas_a_pagar_e_receber():
    response = client.get("/contas-a-pagar-e-receber")
    assert response.status_code == 200
    assert response.json() == [{'id': 1, 'descricao': 'Alugueu', 'valor': '1000.5', 'tipo': 'PAGAR'},
                               {'id': 2, 'descricao': 'Salario', 'valor': '5000.0', 'tipo': 'RECEBER'}]


def test_deve_criar_conta_a_pagar_e_receber():
    nova_conta = {
        "descricao": "Curso Python",
        "valor": '333',
        "tipo": ContasReceberStatus.PAGAR.name
    }

    nova_conta_copy = nova_conta.copy()
    nova_conta_copy["id"] = 3

    response = client.post("/contas-a-pagar-e-receber", json=nova_conta)

    assert response.status_code == 201
    assert response.json()["descricao"] == nova_conta_copy["descricao"]
    assert response.json() == nova_conta_copy
