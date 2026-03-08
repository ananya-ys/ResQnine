from pydantic import BaseModel, Field, field_validator


class AlertRequest(BaseModel):
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)
    location_name: str = Field(..., min_length=1, max_length=150)

    @field_validator("location_name")
    def validate_location(cls, v):
        v = v.strip()
        if not v:
            raise ValueError("location_name cannot be empty")
        return v