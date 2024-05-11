from fastapi import APIRouter, Query
from pydantic import NonNegativeInt
from schemas.products import PRODUCTS_LIST
from services.apriori import AprioriService


class AprioriRouter:
    def __init__(self) -> None:
        self.apriori_service = AprioriService()
        self.router = APIRouter(
            prefix="/apriori",
            tags=["Apriori"],
        )
        self.router.add_api_route(
            path="",
            endpoint=self.run_apriori,
            methods=["Get"],
        )
        self.router.add_api_route(
            path="/products/all",
            endpoint=self.get_all_products,
            methods=["Get"],
        )

    async def run_apriori(
        self,
        argument: str | None = None,
        min_support: int = Query(ge=10, le=AprioriService.SETS_COUNT),
        offset: NonNegativeInt = 0,
        limit: int = Query(default=10, ge=10, le=50),
        min_confidence: float = 0.5,
    ):
        """Number of sets 9836"""
        return self.apriori_service.get_associations_apriori(
            min_support=min_support,
            min_confidence=min_confidence,
            limit=limit,
            offset=offset,
            argument=argument,
        )

    @staticmethod
    async def get_all_products() -> list[str]:
        return PRODUCTS_LIST
