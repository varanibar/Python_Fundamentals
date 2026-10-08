from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(strict=True, ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("=" * 40)
    print("Valid station created:")

    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime(1995, 11, 2),
        is_operational=False,
        notes="Helaas pindakaas"
        )

    if station.is_operational:
        status = "Operational"
    else:
        status = "Non operational"

    print(f" ID: {station.station_id}")
    print(f" Name: {station.name}")
    print(f" Crew: {station.crew_size} people")
    print(f" Power: {station.power_level}%")
    print(f" Oxygen: {station.oxygen_level}%")
    print(f" Last maintenance: {station.last_maintenance}")
    print(f" Status: {status}")
    if station.notes:
        print(f" Notes: {station.notes}")

    print()
    print("=" * 40)

    try:
        SpaceStation(
            station_id="abcde",
            name="1",
            crew_size=50,
            power_level=10,
            oxygen_level=90.5,
            last_maintenance=datetime(1995, 11, 2)
            )
    except ValidationError as err:
        print("Expected validation error:")
        print(str(err).split(" [type=", 1)[0])


if __name__ == "__main__":
    main()
