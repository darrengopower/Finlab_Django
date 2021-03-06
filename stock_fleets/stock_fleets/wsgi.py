import os
from django.core.wsgi import get_wsgi_application
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stock_fleets.settings.development")
application = get_wsgi_application()

from stock_fleets.urls import router as main_router
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(main_router, prefix="/api")

# use django with uvicorn(asgi)
app.mount("/django", WSGIMiddleware(application))
# https://fastapi.tiangolo.com/tutorial/static-files/
app.mount("/static", StaticFiles(directory="static"), name="static")
