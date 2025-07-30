from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

router = APIRouter(prefix='/users', tags=['users'])

# Criar conta
@router.post('/users/signup')

# Dados do perfil
@router.get('/users/me')

#Editar perfil, bandeira, avatar 
@router.patch('/users/me')

