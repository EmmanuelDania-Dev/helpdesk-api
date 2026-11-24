from fastapi import FastAPI

from app.api.routes import tickets, users
from app.models import Ticket, User  # noqa: F401

from .core.config import settings

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