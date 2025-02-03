from fastapi import APIRouter

router = APIRouter()

@router.get("/stream")
def stream():
    return {"message": "Live streaming endpoint"}
