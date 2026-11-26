from contextlib import asynccontextmanager
from fastapi import FastAPI , Request
from core.database.sqlite import init_database
from modules.ai_agent.router import ai_agent_router
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_database()          # Create tables on startup
    yield

app = FastAPI(lifespan=lifespan)

origins = [

]

app.add_middleware(
    CORSMiddleware,
    allow_origin=origins,
    allow_credentials=False,
    allow_methods=["POST"],
    allow_headers=["*"]

)

app.include_router(
    ai_agent_router,
    tags=["AI Module"]
)

@app.get("/", status_code=200)
async def root():
    return {
        "message": "this is a Xander backend"
    }
