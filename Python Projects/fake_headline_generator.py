import random

subjects = [
    "Elon Musk",
    "Bill Gates",
    "A group of Monkeys",
    "Spiderman",
    "A group of Donkeys",
    "Sunny Deol",
    "A bus driver"
]

actions = [
    "enjoy",
    "dancing",
    "eat",
    "playing",
    "focusing",
    "roasting",
    "sharing"
]

places_or_things = [
    "at a park.",
    "in the washroom.",
    "a plate of samosa.",
    "at the football ground.",
    "in the England.",
    "in the kitchen.",
    "a computer."
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f" Headline: {subject} {action} {place_or_thing} "
    print("\n" + headline)

    choice = input("Can you want to generate another headline (yes/no): ")

    if choice == "no":
        break

print("\nThanks for playing this game (Fake Headline Generator)...")