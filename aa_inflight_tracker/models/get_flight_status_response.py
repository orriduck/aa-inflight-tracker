import math
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class GetFlightStatusResponse(BaseModel):
    timestamp: datetime = Field(..., description="Timestamp of the flight status update")
    eta: Optional[datetime] = Field(None, description="Estimated Time of Arrival")
    flightDuration: int = Field(..., description="Flight duration in minutes")
    flightNumber: str = Field(..., description="Flight number")
    latitude: float = Field(..., description="Current latitude of the flight")
    longitude: float = Field(..., description="Current longitude of the flight")
    noseId: str = Field(..., description="Nose ID of the aircraft")
    paState: Optional[str] = Field(None, description="Passenger state")
    vehicleId: str = Field(..., description="Vehicle ID of the aircraft")
    destination: str = Field(..., description="Flight destination")
    origin: str = Field(..., description="Flight origin")
    flightId: str = Field(..., description="Unique flight ID")
    airspeed: Optional[float] = Field(None, description="Current airspeed of the flight")
    airTemperature: Optional[float] = Field(None, description="Current air temperature")
    altitude: float = Field(..., description="Current altitude of the flight")
    distanceToGo: float = Field(..., description="Distance to go in nautical miles")
    doorState: str = Field(..., description="State of the aircraft doors")
    groundspeed: float = Field(..., description="Current ground speed of the flight")
    heading: float = Field(..., description="Current heading of the flight")
    timeToGo: int = Field(..., description="Time to go in minutes")
    wheelWeightState: str = Field(..., description="Wheel weight state of the aircraft")
    grossWeight: Optional[float] = Field(None, description="Gross weight of the aircraft")
    windSpeed: Optional[float] = Field(None, description="Current wind speed")
    windDirection: Optional[float] = Field(None, description="Current wind direction")
    flightPhase: str = Field(..., description="Current phase of the flight")
    
    @staticmethod
    def get_time_to_go_display(time_to_go):
        return f"{math.floor(time_to_go / 60)} hours {time_to_go % 60} mins"
    
    def __str__(self):
        return (
            f"[{self.flightNumber}] ({self.origin}) >> ({self.destination})\n"
            f"- Flight Phase: {self.flightPhase} \n"
            f"- Ground speed: {self.groundspeed} knots, Altitude {self.altitude} ft\n"
            f"- Longitude: {self.longitude:.3f}, Latitude: {self.latitude:.3f}\n" 
            f"- Remaining flight time: {self.get_time_to_go_display(self.timeToGo)}."
        )
    