from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from src.config.settings import Settings
from src.routers import employee, skill
from src.config.db_settings import engine, Base

settings = Settings()

app = FastAPI(title=settings.PROJECT_NAME)

Base.metadata.create_all(bind=engine)

app.include_router(employee.router)
app.include_router(skill.router)

@app.get("/")
def root():
    return RedirectResponse(url="/docs")
