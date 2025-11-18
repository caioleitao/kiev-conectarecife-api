from http.client import HTTPException

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict


class Usuario(BaseModel):
    id: int
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

    usuarios_cadastrado[usuario_id] = novo_usuario
    usuario_id += 1

    return usuarios_cadastrado


@conectarecife.post("/entrar")


@conectarecife.put("/gastar")



@conectarecife.get("/usuario/{usuario_id}")
def obter_info(usuario_id: int):
    info = usuarios_cadastrado.get(usuario_id)

    if not info:
        raise HTTPException(status_code=404)

    return info
