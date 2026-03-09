from fastapi import APIRouter
from app.services.alert_service import send_sms_alert, send_email_alert

router = APIRouter(
    prefix="/api/v1",
    tags=["Emergency Alerts"]
)


@router.post("/alert")
async def trigger_alert(data: dict):

    latitude = data.get("latitude")
    longitude = data.get("longitude")
    location_name = data.get("location", "Unknown location")

    # send alerts
    await send_sms_alert(latitude, longitude, location_name)
    await send_email_alert(latitude, longitude, location_name)

    return {
        "alert_message": "Emergency alerts sent to guardians",
        "risk_level": "HIGH",
        "latitude": latitude,
        "longitude": longitude
    }