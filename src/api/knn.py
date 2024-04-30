from fastapi import APIRouter
from pydantic import NonNegativeInt
from schemas.mushroom import Mushroom
from services.knn import KNNService

knn_router = APIRouter(
    prefix="/knn",
    tags=["K-NN"],
)


@knn_router.post("")
async def classify_mushroom(
    mushroom: Mushroom,
    k: NonNegativeInt = 3,
):
    classification = KNNService().knn(
        mushroom_data=mushroom,
        k=k,
    )
    return {"prediction": "Edible" if classification[0] == 0 else "Not Edible"}
