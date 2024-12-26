from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.freeboard import router as freeboard_router
from routes.useditem import router as used_router

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"]
)

app.include_router(freeboard_router, tags=["Freeboard"], prefix="/freeboard")

app.include_router(used_router, tags=["UsedItem"], prefix="/used")


@app.get("/", tags=["Root"])
async def read_root():
    return {}
