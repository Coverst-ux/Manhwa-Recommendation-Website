from fastapi import APIRouter
from database import create_session

router = APIRouter()

@router.post("/session")
def create_session_endpoint():   
    uuid = create_session()
    return {"session_uuid": uuid}   