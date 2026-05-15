import random
from typing import Generator

players = [
    "alice", "bob", "charlie", "dylan", "eve",
    "frank", "grace", "henry", "iris", "jack",
    "karen", "leo", "maya", "nathan", "olivia"
]

actions = [
    "run", "jump", "swim", "climb", "grab",
    "release", "move", "sleep", "eat", "use",
    "attack", "defend", "craft", "build", "explore"
]


def gen_event() -> Generator:
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(lst: list) -> Generator:
    while (lst):
        element = random.choice(lst)
        lst.remove(element)
        yield element


if __name__ == "__main__":
    n = 1000
    generator = gen_event()
    while (n > 0):
        tuple_generator = next(generator)
        print(f"event {1000 - n}: Player " +
              f"{tuple_generator[0]} did action {tuple_generator[1]}")
        n -= 1
    n = 10
    tuple_list: list = []
    while (n > 0):
        tuple_list.append(next(gen_event()))
        n -= 1
    print(f"Built list of 10 events : {tuple_list}")
    for element in consume_event(tuple_list):
        print(f"Got event from list: {element}")
        print(f"Remains in list: {tuple_list}")
