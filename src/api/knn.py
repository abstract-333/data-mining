from fastapi import APIRouter
from pydantic import NonNegativeInt
from schemas.mushroom import Mushroom
from services.knn import KNNService


class KNNRouter:
    def __init__(self) -> None:
        self.knn_service = KNNService()
        self.router = APIRouter(
            prefix="/knn",
            tags=["K-NN"],
        )
        self.router.add_api_route(
            path="",
            endpoint=self.classify_mushroom,
            methods=["Post"],
        )

    async def classify_mushroom(
        self,
        mushroom: Mushroom,
        k: NonNegativeInt = 3,
    ):
        classification = self.knn_service.knn(
            mushroom_data=mushroom,
            k=k,
        )
        return {"prediction": "Edible" if classification[0] == 0 else "Not Edible"}
