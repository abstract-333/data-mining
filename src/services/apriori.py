from itertools import combinations
from typing import Any, Final, Literal
import numpy as np
import pandas as pd
from pandas import DataFrame


class AprioriService:
    SETS_COUNT: Final[int] = 9836

    def __init__(self) -> None:
        self.df: DataFrame = pd.read_csv(filepath_or_buffer="apriori.csv")

    def generate_new_combinations(
        self,
        old_combinations,
        X: np.ndarray[Any, Any],
        min_support: float,
    ):

        items_from_previous_step = np.unique(old_combinations.flatten())
        rows_count: int = X.shape[0]
        threshold: float = min_support * rows_count

        for old_combination in old_combinations:

            max_combination = old_combination[-1]
            mask = items_from_previous_step > max_combination
            valid_items = items_from_previous_step[mask]
            old_tuple = tuple(old_combination)

            mask_rows = X[:, old_tuple].all(axis=1)
            supports = X[mask_rows][:, valid_items].sum(axis=0)

            valid_indices = (supports >= threshold).nonzero()[0]
            for index in valid_indices:
                yield supports[index]
                yield from old_tuple
                yield valid_items[index]

    @staticmethod
    def _support(datastore: np.ndarray[Any, Any], rows_count: int) -> np.ndarray:
        return np.sum(datastore, axis=0) / rows_count

    def get_frequent_itemsets(
        self,
        date_frame: DataFrame,
        min_support: float,
    ) -> DataFrame | None:

        values: np.ndarray[Any, Any] = date_frame.values

        support = self._support(datastore=values, rows_count=values.shape[0])
        array_column_index = np.arange(values.shape[1])
        support_dict = {1: support[support >= min_support]}
        itemset_dict = {1: array_column_index[support >= min_support].reshape(-1, 1)}

        max_itemset = 1
        rows_count = float(values.shape[0])

        while max_itemset and max_itemset < float("inf"):
            next_max_itemset: int = max_itemset + 1

            combination = self.generate_new_combinations(
                old_combinations=itemset_dict[max_itemset],
                X=values,
                min_support=min_support,
            )
            combination = np.fromiter(combination, dtype=int)
            combination = combination.reshape(-1, next_max_itemset + 1)

            if combination.size == 0:
                break

            itemset_dict[next_max_itemset] = combination[:, 1:]
            support_dict[next_max_itemset] = (
                combination[:, 0].astype(float) / rows_count
            )
            max_itemset: int = next_max_itemset

        all_result: list[pd.DataFrame] = []

        for item in sorted(itemset_dict):
            support = pd.Series(support_dict[item])
            itemsets = pd.Series(
                data=[frozenset(i) for i in itemset_dict[item]],
                dtype="object",
            )
            res: DataFrame = pd.concat((support, itemsets), axis=1)
            all_result.append(res)

        frequent_sets: pd.DataFrame = pd.concat(all_result)
        frequent_sets.columns = ["support", "itemsets"]
        mapping: dict[int, str] = {
            index: item for index, item in enumerate(iterable=date_frame.columns)
        }
        frequent_sets["itemsets"] = frequent_sets["itemsets"].apply(
            lambda x: frozenset([mapping[i] for i in x])
        )
        frequent_sets: DataFrame = frequent_sets.reset_index(drop=True)

        return None if frequent_sets.empty else frequent_sets

    def association_rules(
        self,
        frequent_itemsets: DataFrame,
        min_confidence: float,
        metric="confidence",
    ) -> DataFrame:

        # metrics for association rules
        metric_dict: dict[str, Any] = {
            "support": lambda sAC, _, __: sAC,
            "confidence": lambda sAC, sA, _: sAC / sA,
        }

        columns_ordered: list[str] = [
            "support",
            "confidence",
        ]

        # get dict of {frequent itemset} -> support
        keys = frequent_itemsets["itemsets"].values
        values = frequent_itemsets["support"].values
        frozenset_vect = np.vectorize(lambda x: frozenset(x))
        frequent_items_dict = dict(zip(frozenset_vect(keys), values))

        # prepare buckets to collect frequent rules
        rule_antecedents = []
        rule_consequents = []
        rule_supports = []

        # iterate over all frequent itemsets
        for k in frequent_items_dict.keys():
            support_antecendent_consequent = frequent_items_dict[k]
            # to find all possible combinations
            for index in range(len(k) - 1, 0, -1):
                # of antecedent and consequent
                for combination in combinations(k, r=index):
                    antecedent = frozenset(combination)
                    consequent = k.difference(antecedent)

                    try:
                        support_antecedent = frequent_items_dict[antecedent]
                        support_consequent = frequent_items_dict[consequent]
                    except KeyError:
                        raise KeyError

                    score = metric_dict[metric](
                        support_antecendent_consequent,
                        support_antecedent,
                        support_consequent,
                    )
                    if score >= min_confidence:
                        rule_antecedents.append(antecedent)
                        rule_consequents.append(consequent)
                        rule_supports.append(
                            [
                                support_antecendent_consequent,
                                support_antecedent,
                                support_consequent,
                            ]
                        )

        # check if frequent rule was generated
        if not rule_supports:
            return pd.DataFrame(
                columns=["antecedents", "consequents"] + columns_ordered
            )

        else:
            # generate metrics
            rule_supports = np.array(rule_supports).T.astype(float)
            dataframe_result = pd.DataFrame(
                data=list(zip(rule_antecedents, rule_consequents)),
                columns=["antecedents", "consequents"],
            )

            support_antecendent_consequent = rule_supports[0]
            support_antecedent = rule_supports[1]
            support_consequent = rule_supports[2]
            for m in columns_ordered:
                dataframe_result[m] = metric_dict[m](
                    support_antecendent_consequent,
                    support_antecedent,
                    support_consequent,
                )
            return dataframe_result

    def get_associations_apriori(
        self,
        limit: int,
        offset: int,
        min_support: float = 0.01,
        min_confidence: float = 0.6,
        argument: str | None = None,
    ) -> list[dict[str, list | float]] | None:

        self.df.dropna(inplace=True)

        min_support_float: float | Literal[1] = (
            min_support / self.SETS_COUNT if min_support < self.SETS_COUNT else 1
        )
        frequet: DataFrame | None = self.get_frequent_itemsets(
            date_frame=self.df,
            min_support=min_support_float,
        )
        if frequet is None:
            return None

        rules: pd.DataFrame = self.association_rules(
            frequent_itemsets=frequet,
            metric="confidence",
            min_confidence=min_confidence,
        )
        rules_dict = rules.to_dict(orient="records")
        rules_dict = self._extract_by_argument_consequents(
            rules_dict=rules_dict,
            argument=argument,
            limit=limit,
            offset=offset,
        )
        return rules_dict

    @classmethod
    def _extract_by_argument_consequents(
        cls,
        rules_dict: list[dict],
        argument: str | None,
        limit: int,
        offset: int,
    ) -> list[dict]:
        returned_list: list = []

        if argument:
            for record in rules_dict:
                if argument in record["consequents"]:
                    returned_list.append(record)
        else:
            returned_list = rules_dict

        if offset + limit < len(returned_list):
            return returned_list[offset : offset + limit]

        return returned_list
