import uvicorn
from .handler.event import event_router
from .handler.personality import personality_router
from fastapi import FastAPI
from fastapi import APIRouter


app = FastAPI()
app.include_router(event_router)
app.include_router(personality_router)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
