from pydantic import BaseModel, Field


class Mushroom(BaseModel):
    cap_diameter: int = Field(
        ge=0,
        le=1891,
    )
    cap_shape: int = Field(
        ge=0,
        le=6,
    )
    gill_attachment: int = Field(
        ge=0,
        le=6,
    )
    gill_color: int = Field(
        ge=0,
        le=11,
    )
    stem_height: float = Field(
        ge=0,
        le=3.84,
    )
    stem_width: int = Field(
        ge=0,
        le=3569,
    )
    stem_color: int = Field(
        ge=0,
        le=12,
    )
    season: float = Field(
        ge=0,
        le=1.8,
    )
