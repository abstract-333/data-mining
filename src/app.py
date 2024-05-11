from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from brotli_asgi import BrotliMiddleware
from api.apriori import AprioriRouter
from api.knn import KNNRouter


def app_factory() -> FastAPI:
    fastapi_app = FastAPI(
        title="Data Mining Project",
        version="0.0.1",
        default_response_class=ORJSONResponse,
    )

    fastapi_app.add_middleware(
        middleware_class=BrotliMiddleware,
        quality=6,
        minimum_size=1000,
    )
    fastapi_app.include_router(router=AprioriRouter().router)
    fastapi_app.include_router(router=KNNRouter().router)
    return fastapi_app


app: FastAPI = app_factory()
