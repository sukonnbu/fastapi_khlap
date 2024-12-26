from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from database import (
    add_used,
    delete_used,
    retrieve_used,
    retrieve_used_items,
    update_used,
)
from models.response import ResponseModel, ErrorResponseModel
from models.useditem import (
    UsedItemSchema,
)

router = APIRouter()


@router.get("/", response_description="Get UsedItem Threads from the database")
async def get_used_data():
    used_items = jsonable_encoder(await retrieve_used_items())
    return ResponseModel(used_items, "UsedItems retrieved successfully.")


@router.post("/", response_description="UsedItem added into the database")
async def add_used_data(used: UsedItemSchema = Body(...)):
    used = jsonable_encoder(used)
    new_used = await add_used(used)
    return ResponseModel(new_used, "UsedItem added successfully.")


@router.get("/{id}", response_description="UsedItem retrieved from the database")
async def get_used_by_id(id: str):
    used = await retrieve_used(id)
    return ResponseModel(used, "UsedItem retrieved successfully.")


@router.put("/{id}", response_description="UsedItem updated into the database")
async def update_used_by_id(id: str, used: UsedItemSchema = Body(...)):
    updated_used = await update_used(id, jsonable_encoder(used))
    return ResponseModel(updated_used, "UsedItem updated successfully.")
