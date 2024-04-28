from typing import Final, Literal
from fastapi import APIRouter, Query
import numpy as np
import pandas as pd
from pydantic import NonNegativeInt
from services.apriori import AprioriService
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

apriori_router = APIRouter(
    prefix="/apriori",
    tags=["Apriori"],
)
SETS_COUNT: Final[int] = 9836


@apriori_router.get("")
async def run_apriori(
    min_support: int = Query(ge=0, le=SETS_COUNT),
    offset: NonNegativeInt = 0,
    limit: int = Query(default=10, ge=10, le=50),
    argument: str | None = None,
    min_confidence: float = 0.5,
):
    """Number of sets 9836"""
    df: pd.DataFrame = pd.read_csv(
        "apriori.csv",
    )

    df.dropna(inplace=True)

    # onehot: pd.DataFrame = pd.get_dummies(data=df, sparse=False)
    extraced_data = df.iloc[:, :-1]

    min_support_float: float | Literal[1] = (
        min_support / SETS_COUNT if min_support < SETS_COUNT else 1
    )

    frequent_itemsets: pd.DataFrame = apriori(
        df=extraced_data,
        min_support=min_support_float,
        use_colnames=True,
        low_memory=True,
    )
    if frequent_itemsets.empty:
        return []

    rules: pd.DataFrame = association_rules(
        df=frequent_itemsets,
        metric="confidence",
        min_threshold=min_confidence,
    )
    rules_dict = rules.to_dict(orient="records")

    rules_dict_no_inf = replace_inf_values(
        rules_dict=rules_dict,
        argument=argument,
        limit=limit,
        offset=offset,
    )

    return rules_dict_no_inf


def replace_inf_values(
    rules_dict: list[dict],
    argument: str | None,
    limit: int,
    offset: int,
) -> list[dict]:
    placeholder = "Infinity"
    returned_list: list = []
    for record in rules_dict:
        for value in record["consequents"]:
            if value == argument or argument is None:

                record.pop("lift", None)
                record.pop("conviction", None)
                record.pop("zhangs_metric", None)
                record.pop("leverage", None)
                record.pop("consequent support", None)
                record.pop("antecedent support", None)
                record.pop("support", None)

                for key, value in record.items():
                    if isinstance(value, float) and np.isinf(value):
                        record[key] = placeholder

                returned_list.append(record)

    if offset + limit < len(returned_list):
        return returned_list[offset : offset + limit]

    return []
