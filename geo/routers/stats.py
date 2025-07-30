from fastapi import APIRouter

router = APIRouter(prefix='/stats', tags=['stats'])


#istância total, calorias, vitórias
@router.get('/stats/summary')

#Estatísticas por dia
@router.get('/stats/daily')
