from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# temporary storage
user_location = {}

class Location(BaseModel):
    latitude: float
    longitude: float

@router.post("/location/update")
async def update_location(location: Location):

    user_location["lat"] = location.latitude
    user_location["lng"] = location.longitude

    return {"status": "updated"}


@router.get("/location/latest")
async def get_location():

    return {
        "latitude": user_location.get("lat"),
        "longitude": user_location.get("lng")
    }

@router.get("/location/latest")
async def get_location():
    return user_location