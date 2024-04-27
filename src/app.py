from fastapi import FastAPI

from api.apriori import apriori_router
from api.knn import knn_router


def app_factory() -> FastAPI:
    fastapi_app = FastAPI(
        title="Data Mining Project",
        version="0.0.1",
    )

    fastapi_app.include_router(router=apriori_router)
    fastapi_app.include_router(router=knn_router)

    return fastapi_app


app: FastAPI = app_factory()
