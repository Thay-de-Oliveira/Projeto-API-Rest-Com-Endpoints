import requests
from fastapi import FastAPI, HTTPException
#from fastapi.responses import HTMLResponse
from fastapi.testclient import TestClient
from fastapi.responses import JSONResponse

app = FastAPI()

#Lista de dados
clientes = [
    {
        "id": 1,
        "nome": "Silvio Santos",
        "valor_na_conta": 10000,
        "transacoes": [
            {
                "id": 1,  #Id transação
                "valor": 1500,
                "tipo": "d",
                "descricao": "Uma transacao"
            }
        ],
    },
    {
        "id": 2,
        "nome": "Fausto Silva",
        "valor_na_conta": 10,
        "transacoes": [
            {
                "id": 1,  #Id transação
                "valor": 1500,
                "tipo": "c",
                "descricao": "Uma transacao"
            },
            {
                "id": 2,  #Id transação
                "valor": 32,
                "tipo": "d",
                "descricao": "Uma transacao"
            }
        ],
    },
    {
        "id": 3,
        "nome": "Gugu Liberato",
        "transacoes": [],
    }
]

@app.delete("/clientes/{cliente_id}/transacoes/{transacao_id}")
def delete_transaction(cliente_id: int, transacao_id: int): #Função
    for cliente in clientes: #Percorre lista de clientes
        if cliente["id"] == cliente_id:  #Verifica se id cliente corresponde ao id fornecido
            for transacao in cliente["transacoes"]:  #Percorre lista de transação do cliente
                if transacao["id"] == transacao_id:  #Verifica se id transação corresponde ao id fornecido
                    cliente["transacoes"].remove(transacao)  #Remove a transação da lista de transações do cliente
                    return None, 204  #Retorna código 204
            else:
                raise HTTPException(status_code=404, detail="Ops! Transação não encontrada")  #Se transação não encontrada 
    else:
        raise HTTPException(status_code=404, detail="Ops! Cliente não encontrado")  #Se cliente não encontrado

   
