import typing
import random

lst_names = ["Frodo", "Sam", "Merry", "Pippin"]
lst_actions = ["run", "eat", "sleep", "grab", "run", "climb",
               "sleep", "swim", "move", "release", "fight"]


def gen_event() -> typing.Generator[
                    tuple[str, str], None, None]:
    while True:
        name = random.choice(lst_names)
        action = random.choice(lst_actions)
        new_event = (name, action)
        yield new_event


def consume_event(lst_events:
                  list[tuple[str, str]]) -> typing.Generator[
                      tuple[str, str], None, None]:
    while lst_events:
        event = random.choice(lst_events)
        lst_events.remove(event)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")
    event_generator = gen_event()
    for _ in range(1000):
        event = next(event_generator)
        print(f"Event {_}: Player {event[0]} did action {event[1]}")

    lst_events = []
    for _ in range(10):
        event = next(event_generator)
        lst_events.append(event)
    print("Built list of 10 events: ", lst_events)

    for event in consume_event(lst_events):
        print("Got event from list: ", event)
        print("Remains in list: ", lst_events)


if __name__ == "__main__":
    main()
