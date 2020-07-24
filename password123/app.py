import os

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request
from starlette.staticfiles import StaticFiles


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

from starlette.templating import Jinja2Templates

from password123.generate import generate

app = FastAPI(title="Password 123456789")

templates = Jinja2Templates(directory="templates")


@app.get("/", include_in_schema=False)
def root(request: Request):
    return templates.TemplateResponse("index.html", context={
        "request": request,
        "new_password": generate()
    })


class PasswordResponse(BaseModel):
    password: str


@app.get("/password", summary="Generates a new password", response_model=PasswordResponse)
def new_password():
    return PasswordResponse(password=generate())


@app.get("/health", summary="Stats on the health of the system")
def health():
    return {
        "healthy": True
    }


# If no other route matches assume that it might be a static file
app.mount("/", StaticFiles(directory="static_assets"), name="static")
