import numpy as np
import pandas as pd
from pydantic import NonNegativeInt

from schemas.mushroom import Mushroom


class KNNService:
    def __init__(self):
        self.df = pd.read_csv(filepath_or_buffer="knn.csv")
        self.dataset = self.df.iloc[:, :-1].values
        self.classification_data = self.df.iloc[:, -1].values

    def knn(
        self,
        mushroom_data: Mushroom,
        k: NonNegativeInt,
    ):
        input = np.array(
            object=[
                [
                    mushroom_data.cap_diameter,
                    mushroom_data.cap_shape,
                    mushroom_data.gill_attachment,
                    mushroom_data.gill_color,
                    mushroom_data.stem_height,
                    mushroom_data.stem_width,
                    mushroom_data.stem_color,
                    mushroom_data.season,
                ]
            ]
        )
        return self._knn_precdict(
            dataset=self.dataset,
            classification_data=self.classification_data,
            input_data=input,
            k=k,
        )

    @classmethod
    def _knn_precdict(
        cls,
        dataset,
        classification_data,
        input_data,
        k: NonNegativeInt,
    ):

        distances = np.sqrt(((dataset - input_data[:, np.newaxis]) ** 2).sum(axis=2))
        nearest_indices = np.argpartition(distances, k, axis=1)[:, :k]

        nearest_labels = classification_data[nearest_indices]
        predictions = np.apply_along_axis(
            lambda x: np.bincount(x).argmax(),
            axis=1,
            arr=nearest_labels,
        )

        return predictions
