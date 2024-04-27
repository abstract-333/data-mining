import json
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules


class AprioriService:
    def handle_request(self, min_support: float = 0.01, min_confidence: float = 0.6):

        df = pd.read_csv("amazon_prime_users.csv")

        frequent_itemsets = apriori(df, min_support=min_support)
        rules = association_rules(
            frequent_itemsets, metric="confidence", min_threshold=min_confidence
        )
        rules = rules.sort_values(by=["confidence", "lift"], ascending=False)

        rules_json = json.loads(rules.to_json(orient="records"))

        return rules_json
