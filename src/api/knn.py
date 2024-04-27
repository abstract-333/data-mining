from fastapi import APIRouter
import numpy as np
import pandas as pd
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
    df: pd.DataFrame = pd.read_csv(filepath_or_buffer="knn.csv")
    X_train = df.iloc[:, :-1].values
    y_train = df.iloc[:, -1].values
    X_test = np.array(
        object=[
            [
                mushroom.cap_diameter,
                mushroom.cap_shape,
                mushroom.gill_attachment,
                mushroom.gill_color,
                mushroom.stem_height,
                mushroom.stem_width,
                mushroom.stem_color,
                mushroom.sesson,
            ]
        ]
    )
    prediction = KNNService().knn_predict(
        X_train=X_train,
        y_train=y_train,
        X_test=X_test,
        k=k,
    )
    return {"prediction": "Edible" if prediction[0] == 0 else "Not Edible"}
