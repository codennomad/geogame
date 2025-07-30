from fastapi import APIRouter

router = APIRouter(prefix='/activities', tags=['activities'])


#Histórico de corridas
@router.get('/activities')

#Mostrar progresso do dia
@router.get('/activities/today')

#Registrar nova atividade (com GPS + val.)
@router.post('/activities')
