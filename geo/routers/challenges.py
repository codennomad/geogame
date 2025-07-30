from fastapi import APIRouter

router = APIRouter(prefix='/challenges', tags=['challenges'])


#Ver desafios em andamento
@router.get('/challenges/active')

#Iniciar ataque a território de outro jogador
@router.post('/challenges/start')

#Resolver (ganhou, perdeu, empatou)
@router.post('/challenges/{id}/resolve')