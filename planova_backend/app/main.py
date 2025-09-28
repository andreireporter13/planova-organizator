from fastapi import FastAPI
from app.api import auth, whois
from app.core.middleware import add_middlewares
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

add_middlewares(app)

app.include_router(auth.router, prefix="/whois-backend/auth", tags=["auth"])
app.include_router(whois.router, prefix="/whois-backend/whois", tags=["whois"])
