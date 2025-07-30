from fastapi import APIRouter

router = APIRouter(prefix='/resources', tags=['resources'])

#Ver meus recursos atuais
@router.get('/resources')

#Coletar recursos de territórios
@router.get('/resources/collect')

#Ver era atual / desbloqueios
@router.post('/resources/progression')
