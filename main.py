from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

class Usuario(BaseModel):
    cpf: str
    nome_completo: str
    moeda_capiba: float

conectarecife = FastAPI()

usuarios_cadastrado: Dict[int, dict] = {}
usuario_id = 1

@conectarecife.post("/cadastro")
def criar_usuario(usuario: Usuario):
    global usuario_id

    novo_usuario = {
        "id": usuario_id,
        "nome_completo": usuario.nome_completo,
        "moeda_capiba": usuario.moeda_capiba
    }

@conectarecife.post("/entrar")

@conectarecife.put("/gastar")



@conectarecife.get("")
