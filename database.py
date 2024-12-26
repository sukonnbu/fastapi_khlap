import os
import motor.motor_asyncio
from bson import ObjectId
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DB_URL")
client = motor.motor_asyncio.AsyncIOMotorClient(DB_URL)

database = client.KHLaP
freeboard_collection = database.get_collection("freeboard")
used_collection = database.get_collection("used")


# FREEBOARD
def freeboard_helper(thread) -> dict:
    return {
        "id": str(thread["_id"]),
        "title": thread["title"],
        "username": thread["username"],
        "content": thread["content"],
        "image": thread["image"],
        "updated_at": thread["updated_at"],
        "comments": thread["comments"],
    }


async def retrieve_freeboard(id: str) -> dict:
    freeboard = await freeboard_collection.find_one({"_id": ObjectId(id)})
    if freeboard:
        return freeboard_helper(freeboard)


async def retrieve_freeboards():
    freeboards = []
    async for freeboard in freeboard_collection.find():
        freeboards.append(freeboard_helper(freeboard))
    return freeboards


async def add_freeboard(freeboard_data: dict) -> dict:
    freeboard = await freeboard_collection.insert_one(freeboard_data)
    new_freeboard = await freeboard_collection.find_one({"_id": freeboard.inserted_id})
    return freeboard_helper(new_freeboard)


async def delete_freeboard(id: str):
    freeboard = await freeboard_collection.find_one({"_id": ObjectId(id)})
    if freeboard:
        await freeboard_collection.delete_one({"_id": freeboard.inserted_id})
        return True


async def update_freeboard(id: str, data: dict):
    freeboard = await freeboard_collection.find_one({"_id": ObjectId(id)})
    if freeboard:
        updated_freeboard = await freeboard_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_freeboard:
            return True
        return False


# USED_ITEM
def used_helper(thread) -> dict:
    return {
        "id": str(thread["_id"]),
        "title": thread["title"],
        "username": thread["username"],
        "itemname": thread["itemname"],
        "sold": thread["sold"],
        "price": thread["price"],
        "others": thread["others"],
        "image": thread["image"],
        "updated_at": thread["updated_at"],
        "comments": thread["comments"],
    }


async def retrieve_used(id: str) -> dict:
    used = await used_collection.find_one({"_id": ObjectId(id)})
    if used:
        return used_helper(used)


async def retrieve_used_items():
    used_items = []
    async for used in used_collection.find():
        used_items.append(used_helper(used))
    return used_items


async def add_used(used_data: dict) -> dict:
    used = await used_collection.insert_one(used_data)
    new_used = await used_collection.find_one({"_id": used.inserted_id})
    return used_helper(new_used)


async def delete_used(id: str):
    used = await used_collection.find_one({"_id": ObjectId(id)})
    if used:
        await used_collection.delete_one({"_id": used.inserted_id})
        return True


async def update_used(id: str, data: dict):
    used = await used_collection.find_one({"_id": ObjectId(id)})
    if used:
        updated_used = await used_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_used:
            return True
        return False
