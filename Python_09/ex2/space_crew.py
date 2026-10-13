from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum
from typing import Any
import json


class Rank (str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """Crew member data with validated personal data."""

    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    """Space mission data with field and business rule validation."""

    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember]
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission_rules(self) -> "SpaceMission":
        """Enforce mission rules after field validation."""

        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        if not 1 <= len(self.crew) <= 12:
            raise ValueError("Crews must contain 1-12 members")

        ranks: list[str] = [member.rank.value for member in self.crew]
        if "commander" not in ranks and "captain" not in ranks:
            raise ValueError(
                "Must have at least one Commander or Captain")

        if self.duration_days > 365:
            crew_size = len(self.crew)
            experienced_members = sum(
                member.years_experience >= 5
                for member in self.crew
                )

            if experienced_members * 2 < crew_size:
                raise ValueError(
                    "Long missions (> 365 days) need 50% "
                    "experienced crew (5+ years)"
                    )

        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self

    def show(self) -> None:
        print(
            f"\nValid mission created:\n"
            f" Mission: {self.mission_name}\n"
            f" ID: {self.mission_id}\n"
            f" Destination: {self.destination}\n"
            f" Duration: {self.duration_days} days\n"
            f" Budget: ${self.budget_millions}M\n"
            f" Crew size: {len(self.crew)}\n"
            f" Crew members:"
        )
        for member in self.crew:
            print(
                f"  - {member.name} ({member.rank.value})"
                f"  - {member.specialization}"
                )


def unpack(space_missions: list[dict[str, Any]]) -> None:
    for mission_data in space_missions:
        try:
            mission = SpaceMission(**mission_data)
            mission.show()

        except ValidationError as err:
            print("\nInvalid mission data:")

            for error in err.errors():
                loc = error["loc"]
                src = ".".join(map(str, error["loc"]))
                msg = error["msg"]

                if not loc:
                    src = " model_validator rule"
                    msg = error["msg"].removeprefix("Value error, ")

                elif len(loc) == 1:
                    src = f" SpaceMission field '{src}'"

                else:
                    src = f" CrewMember field   '{src}'"

                print(f"{src} -> {msg}")


def test_json() -> None:
    try:
        with open("space_missions.json", "r") as file:
            missions = json.load(file)

    except Exception as err:
        print(f"JSON file: {err}")

    else:
        unpack(missions)


def test_python() -> None:
    try:
        import space_missions  # type: ignore[import-not-found, unused-ignore]
        missions = space_missions.SPACE_MISSIONS

    except Exception as err:
        print(f"Python file: {err}")

    else:
        unpack(missions)


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 40)

    print("Testing with provided JSON file:")
    test_json()

    print()
    print("=" * 40)
    print("Testing with provided Python file:")
    test_python()


if __name__ == "__main__":
    main()
