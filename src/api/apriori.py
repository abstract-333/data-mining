from typing import Final, Literal
from fastapi import APIRouter
import numpy as np
import pandas as pd
from services.apriori import AprioriService
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

apriori_router = APIRouter(
    prefix="/apriori",
    tags=["Apriori"],
)
SETS_COUNT: Final[int] = 9836


@apriori_router.get("/{argument}")
async def run_apriori(
    argument: str,
    min_support: int,
    min_confidence: float = 0.5,
):
    """Number of sets 9836"""
    df: pd.DataFrame = pd.read_csv(
        "apriori.csv",
    )

    df.dropna(inplace=True)

    onehot: pd.DataFrame = pd.get_dummies(data=df, sparse=False)

    min_support_float: float | Literal[1] = (
        min_support / SETS_COUNT if min_support < SETS_COUNT else 1
    )

    frequent_itemsets: pd.DataFrame = apriori(
        df=onehot,
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

    rules_dict_no_inf = replace_inf_values(rules_dict=rules_dict, argument=argument)

    return rules_dict_no_inf


def replace_inf_values(rules_dict: list[dict], argument: str) -> list[dict]:
    placeholder = "Infinity"
    returned_list: list = []

    for record in rules_dict:
        for value in record["consequents"]:
            if value == argument:
                record.pop("lift")
                record.pop("conviction")
                record.pop("zhangs_metric")
                record.pop("leverage")
                record.pop("consequent support")
                record.pop("antecedent support")
                record.pop("support")
                for key, value in record.items():
                    if isinstance(value, float) and np.isinf(value):
                        record[key] = placeholder

                returned_list.append(record)

    return returned_list
