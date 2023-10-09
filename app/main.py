import uvicorn
from app.handler.helper.exceptions import ApplicationException
from app.handler.event import event_router
from app.handler.personality import personality_router
from app.handler.career import career_router
from fastapi import FastAPI

from .handler.helper.exception_handlers import (
    application_exception_handler,
    unexpected_exception_handler,
)


app = FastAPI()
app.include_router(router=event_router, prefix="/events")
app.include_router(router=personality_router, prefix="/personalities")
app.include_router(router=career_router, prefix="/careers")
app.add_exception_handler(ApplicationException, application_exception_handler)
app.add_exception_handler(Exception, unexpected_exception_handler)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
