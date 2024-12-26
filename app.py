from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.freeboard import router as freeboard_router
from routes.useditem import router as used_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"], allow_credentials=True,
)

app.include_router(freeboard_router, tags=["Freeboard"], prefix="/freeboard")
app.include_router(used_router, tags=["Used"], prefix="/used")
@app.get("/", tags=["Root"])
async def read_root():
    return {}
