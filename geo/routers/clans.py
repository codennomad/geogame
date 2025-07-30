from fastapi import APIRouter

router = APIRouter(prefix='/clans', tags=['clans'])

#Listar clãs existentes
@router.get('/clans')

#Ver membros e info
@router.get('/clans/{id}')

#Criar um clã
@router.post('/clans')

#Entrar em um clã
@router.post('/clans/{id}/join')
