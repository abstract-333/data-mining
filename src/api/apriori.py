from fastapi import APIRouter, Query
from pydantic import NonNegativeInt
from services.apriori import AprioriService


apriori_router = APIRouter(
    prefix="/apriori",
    tags=["Apriori"],
)


@apriori_router.get("")
async def run_apriori(
    min_support: int = Query(ge=0, le=AprioriService.SETS_COUNT),
    offset: NonNegativeInt = 0,
    limit: int = Query(default=10, ge=10, le=50),
    argument: str | None = None,
    min_confidence: float = 0.5,
):
    """Number of sets 9836"""
    return AprioriService().get_associations_apriori(
        min_support=min_support,
        min_confidence=min_confidence,
        limit=limit,
        offset=offset,
        argument=argument,
    )
