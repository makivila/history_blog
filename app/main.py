import uvicorn

from app.handler.exceptions import ApplicationException, NotPupsik
from .handler.event import event_router
from .handler.personality import personality_router
from fastapi import FastAPI
from fastapi import APIRouter
from .handler.exception_handlers import (
    application_exception_handler,
    unexpected_exception_handler,
)


app = FastAPI()
app.include_router(event_router)
app.include_router(personality_router)
app.add_exception_handler(ApplicationException, application_exception_handler)
app.add_exception_handler(Exception, unexpected_exception_handler)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
