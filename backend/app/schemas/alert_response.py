from pydantic import BaseModel
from typing import Literal


class AlertResponse(BaseModel):
    alert_message: str
    timestamp: str
    risk_level: Literal["LOW", "MEDIUM", "HIGH", "CRITICAL"]