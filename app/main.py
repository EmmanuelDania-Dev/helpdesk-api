from fastapi import FastAPI

from .core.config import settings
from app.api.routes import users, tickets
from app.models import User, Ticket

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug
)


@app.get("/")
def root():
    return {
        "app_name": settings.app_name,
        "environment": settings.environment,
        "debug": settings.debug
    }


app.include_router(users.router)
app.include_router(tickets.router)