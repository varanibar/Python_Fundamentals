from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    # After validators run after Pydantic has validated the fields.
    def bussiness_rules(self) -> "AlienContact":
        # Double quotes are needed to be able to refer to class that
        # is not fully defined yet.
        # At this point, Python is still executing the definition of
        # AlienContact, the class has not been fully created yet.
        # The double quotes tell Python to treat AlienContact as a string
        # annotation instead of immediately evaluating it as a class
        # reference.
        if not self.contact_id.startswith("AC"):
            raise ValueError(
                " Contact ID must start with 'AC' (Alien Contact)")

        if self.contact_type == ContactType.PHYSICAL \
                and not self.is_verified:
            raise ValueError(
                " Physical contact reports must be verified")

        if self.contact_type == ContactType.TELEPATHIC \
                and self.witness_count < 3:
            raise ValueError(
                " Telepathic contact requires at least 3 witnesses")

        if self.signal_strength > 7.0 \
                and not self.message_received:
            raise ValueError(
                " Strong signals (> 7.0) should include received messages")

        return self  # The validated instance is returned


def main() -> None:
    print("Alien Contact Log Validation")
    print("=" * 40)
    print("Valid contact report:")

    contact = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime.now(),
        location="Area 51, Nevada",
        contact_type=ContactType.RADIO,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli"
        )

    print(f" ID: {contact.contact_id}")
    print(f" Last contact: {contact.timestamp}")
    print(f" Type: {contact.contact_type.value}")
    print(f" Location: {contact.location}")
    print(f" Signal: {contact.signal_strength}/10")
    print(f" Duration: {contact.duration_minutes} minutes")
    print(f" Witnesses: {contact.witness_count}")
    if contact.message_received:
        print(f" Message: '{contact.message_received}'")

    print()
    print("=" * 40)

    try:
        contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=8.5,
            duration_minutes=10,
            witness_count=5,
            # message_received="Greetings from Zeta Reticuli",
            is_verified=False
            )
    except ValidationError as err:
        print("Expected validation error:")
        print(err.errors()[0].get('msg').removeprefix('Value error, '))


if __name__ == "__main__":
    main()
