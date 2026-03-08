import re
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import get_settings


def configure_cors(app):

    settings = get_settings()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def sanitize_location_name(value: str):

    value = re.sub(r"<.*?>", "", value)
    value = re.sub(r"[^\w\s\-]", "", value)

    return value[:150]