from fastapi import APIRouter

router = APIRouter(prefix='/territories', tags=['territories'])


#Listar territórios no mapa (por área)
@router.get('/territories')

#Ver territórios que eu possuo
@router.get('/territories/mine')

#Ver dados específicos do território
@router.get('/territories/{id}')

#Conquistar área delimitada
@router.post('/territories/conquer')

#Reforçar território com nova corrida
@router.post('/territories/reinforce')
