from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum
from typing import Any
import json

class Rank (Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def mission_rules(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        ranks: list[str] = [member.rank.value for member in self.crew]
        if "commander" not in ranks and "captain" not in ranks:
            raise ValueError("Must have at least one Commander or Captain")

        if self.duration_days > 365:
            crew_experience: list[int] = [member.years_experience for member in self.crew]
            crew_size: int = len(self.crew)
            total_exp = sum(crew_experience)
            media = total_exp // crew_size
            if media <= 5.0:
                raise ValueError("Long missions (> 365 days) need 50%% experienced crew (5+ years)")

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
                f"  - {member.name} ({member.rank.value}) - {member.specialization}"
                )


def unpack(space_missions: list[dict[str, Any]]) -> None:
    for mission_data in space_missions:
        try:
            mission = SpaceMission(**mission_data)
            mission.show()

        except ValueError as err:
            print("\nInvalid mission data:\n")

            for error in err.errors():
                loc = error["loc"]
                msg = error["msg"].removeprefix("Value error, ")

                if not loc:
                    source = "SpaceMission rule:"

                elif loc[0] == "crew" and len(loc) >= 2:
                    member_index = loc[1]
                    field = ".".join(map(str, loc[2:1]))

                    source = f"CrewMember rule: crew member {member_index} in {field}"

                else:
                    source = f"SpaceMission rule: {'.'.join(map(str, loc))}"
                print(f" {source}")
                print(f" {msg}")





            # location = err.errors()[0].get('loc')
            # if not location or len(location) == 1:
            #     if len(location) == 1:
            #         location = f"SpaceMission rule: {location[0]}\n"
            #     else:
            #         location = "SpaceMission rule:\n"
            # else:
            #     location = f"CrewMember rule: crew member {location[1]} in {location[2]}\n"
            # msg = err.errors()[0].get('msg')
            # err = str(err).split(msg, 1)[0].removeprefix("1 validation error for SpaceMission\n")
            # msg = msg.removeprefix("Value error, ")
            # print(
            #     f" {location}"
            #     f"  {msg}"
            #     )


def test_json() -> None:
    try:
        with open("/home/varaniba/CODAM_CORE/Python/Python_09/ex2/space_missions.json", "r") as file:
            space_missions_json = json.load(file)
    except Exception as err:
        print(f"JSON file: {err}")
    else:
        unpack(space_missions_json)


def test_python() -> None:
    try:
        from space_missions import SPACE_MISSIONS as space_missions_py
    except Exception as err:
        print(f"Python file: {err}")
    else:
        unpack(space_missions_py)


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 40)

    print("Testing with provided JSON file:")
    test_json()

    print("=" * 40)
    print("Testing with provided Python file:")
    # test_python()


if __name__ == "__main__":
    main()
