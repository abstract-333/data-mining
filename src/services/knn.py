import numpy as np
from pydantic import NonNegativeInt


class KNNService:

    def knn_predict(
        self,
        X_train,
        y_train,
        X_test,
        k: NonNegativeInt,
    ):

        distances = np.sqrt(((X_train - X_test[:, np.newaxis]) ** 2).sum(axis=2))
        nearest_indices = np.argpartition(distances, k, axis=1)[:, :k]

        nearest_labels = y_train[nearest_indices]
        predictions = np.apply_along_axis(
            lambda x: np.bincount(x).argmax(),
            axis=1,
            arr=nearest_labels,
        )

        return predictions
