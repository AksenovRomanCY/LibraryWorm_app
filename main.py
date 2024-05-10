import os
os.system("source venv/bin/activate")
os.system("export PYTHONPATH=$PATHONPATH:`pwd`")

from fastapi import FastAPI
import uvicorn
from database import Base, engine

from routers import router_user

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(router_user.router, prefix="/user")
app.include_router(router_user.router, prefix="/students")
app.include_router(router_user.router, prefix="/books")

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True, workers=3)
