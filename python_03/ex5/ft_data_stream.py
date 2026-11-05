import random
from typing import Generator

def gen_event() -> Generator[tuple[str,str], None, None]:
    users = ["Lassana", "Kyle", "Tomas", "Diakhate"]
    action = ["Write", "Read", "Spell", "Count"]

    while True:
        user = random.choice(users)
        act = random.choice(action)

        yield (user, act)

def consume_event(event_list:list) -> Generator[tuple[str,str], None, None]:
    while len(event_list) > 0:
        idx = random.randint(0, len(event_list) - 1)

        event = event_list.pop(idx)

        yield event

if __name__ == "__main__":
    print("=== Game Data Stream Processsor ===")

    generator = gen_event()

    for i in range(1000):
        user, act = next(generator)
        print(f"Event {i+1}: Player {user} did action {act}")

    ten_events = [next(generator) for _ in range(10)] 
    print(f"Built list of 10 events: {ten_events}")

    for event in consume_event(ten_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")