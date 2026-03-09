from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.alert import router as alert_router
from app.api.routes.location import router as location_router


def create_app() -> FastAPI:

    app = FastAPI(
        title="ResQnine API",
        version="1.0.0"
    )

    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # ROUTERS
    app.include_router(alert_router, prefix="/api/v1")
    app.include_router(location_router, prefix="/api/v1")

    return app


app = create_app()