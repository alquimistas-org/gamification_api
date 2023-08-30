from fastapi import FastAPI

from models import Base
from service.global_results_service import GlobalResultsService
from sql_alchemy_repository.global_results_repository_sql_alchemy import GlobalResultsSQLAlchemy
from sql_conf.database import engine

app = FastAPI()
Base.metadata.create_all(bind=engine)


@app.get("/global_results")
async def global_results():
    service = GlobalResultsService(GlobalResultsSQLAlchemy())
    return service.get()
