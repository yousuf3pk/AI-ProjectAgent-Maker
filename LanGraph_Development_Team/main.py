from fastapi import FastAPI
from core.database.postgres import engine
from modules.ai_team.router import ai_agent_router


from dotenv import load_dotenv
load_dotenv()


from core.database.postgres import engine
engine()
app = FastAPI()

app.include_router(ai_agent_router,tags=["AI TEAM"])