from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

router = APIRouter()

@router.get("/")
async def get_usedItem_data():
    return {"data": []}