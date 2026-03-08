from app.exceptions.handlers import (
    validation_error_handler,
    http_exception_handler,
    sheshield_exception_handler,
    generic_exception_handler,
    SheShieldBaseException
)

from fastapi.exceptions import RequestValidationError
from fastapi import HTTPException
from app.core.security import configure_cors


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.alert import router as alert_router
from app.core.logging import setup_logging
from app.core.config import get_settings

def create_app() -> FastAPI:

    setup_logging()
    settings = get_settings()

    app = FastAPI(
        title=settings.APP_NAME,
        version="1.0.0"
    )

    configure_cors(app)

    app.include_router(alert_router)

    app.add_exception_handler(RequestValidationError, validation_error_handler)
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(SheShieldBaseException, sheshield_exception_handler)
    app.add_exception_handler(Exception, generic_exception_handler)

    return app

app = create_app()


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "SheShield AI",
        "version": "1.0.0"
    }