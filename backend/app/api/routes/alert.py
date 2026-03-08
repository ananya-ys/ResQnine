from fastapi import APIRouter
from app.schemas.alert_request import AlertRequest
from app.schemas.alert_response import AlertResponse
from app.services.alert_service import AlertService
from app.services.alert_service import send_sms_alert, send_email_alert


router = APIRouter(
    prefix="/api/v1",
    tags=["Emergency Alerts"]
)

service = AlertService()


from app.services.alert_service import send_email_alert

router = APIRouter()

@router.post("/alert")
async def trigger_alert():

    await send_email_alert()

    return {
        "alert_message": "Emergency alert sent to contacts",
        "risk_level": "HIGH"
    }


@router.post("/alert")
async def trigger_alert(data: dict):

    lat = data.get("latitude")
    lng = data.get("longitude")

    send_sms_alert(lat, lng)
    await send_email_alert()

    return {
        "alert_message": "Emergency alerts sent",
        "risk_level": "HIGH"
    }