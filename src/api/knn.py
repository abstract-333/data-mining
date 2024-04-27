from fastapi import APIRouter
from pydantic import NonNegativeInt
from schemas.mushroom import Mushroom
from services.knn import KNNService

knn_router = APIRouter(
    prefix="/knn",
    tags=["K-NN"],
)


@knn_router.post("")
async def predict(
    mushroom: Mushroom,
    k: NonNegativeInt = 3,
):
    prediction = KNNService().knn(
        mushroom_data=mushroom,
        k=k,
    )
    return {"prediction": "Edible" if prediction[0] == 0 else "Not Edible"}
