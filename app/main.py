from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
from contextlib import asynccontextmanager
from app.database.session import create_db_tables
from app.api import router

@asynccontextmanager
async def lifespan_handler(app: FastAPI):
    create_db_tables()
    yield
app = FastAPI(lifespan=lifespan_handler)
app.include_router(router.master_router)
@app.get("/")
def root():
    return {"Message": "Hello World."}



# Api Documentation.
@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )