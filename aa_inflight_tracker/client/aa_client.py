from pydantic import ValidationError
import requests

from aa_inflight_tracker.models.get_flight_status_response import GetFlightStatusResponse


class AAInflightClient:
    def __init__(self):
        self.base_url = "https://www.aainflight.com/api/v1/"
        self.headers = {
            "Content-Type": "application/json",
        }

    def get_current_flight_status(self) -> GetFlightStatusResponse:
        url = f"{self.base_url}/connectivity/viasat/flight"
        try:
            response = requests.get(url, headers=self.headers)
            return GetFlightStatusResponse.model_validate(response.json())
        except:
            raise Exception(f"Error fetching flight status: {response.status_code}")
            