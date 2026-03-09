from typing import Dict


async def send_sms_alert(latitude: float, longitude: float, location_name: str) -> Dict:
    return {
        "status": "sms_sent",
        "message": "SMS alert sent to guardians",
        "latitude": latitude,
        "longitude": longitude,
        "location": location_name
    }


async def send_email_alert(latitude: float, longitude: float, location_name: str) -> Dict:
    return {
        "status": "email_sent",
        "message": "Email alert sent to guardians",
        "latitude": latitude,
        "longitude": longitude,
        "location": location_name
    }