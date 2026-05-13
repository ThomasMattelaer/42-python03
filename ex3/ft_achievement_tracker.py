import random


def gen_player_achievements() -> set:
    achievements = [
        "World Savior",
        "Crafting Genius",
        "Speed Runner",
        "Ghost Mode",
        "Dragon Slayer",
        "Master Builder",
        "No Damage Run",
        "Explorer",
        "Last Stand",
        "Legendary",
        "Shadow Walker",
        "Iron Will",
        "Treasure Hunter",
        "Untouchable",
        "First Blood",
        "Night Owl",
        "Combo King",
        "Survivor",
        "Perfectionist",
        "Lone Wolf",
        "Boss Crusher",
        "Time Bender",
        "Silent Assassin",
        "Fortune Seeker",
        "Phoenix Rising",
        "War Machine",
        "Puzzle Master",
        "Dimension Hopper",
        "Unstoppable",
        "True Hero"
    ]
    number = random.randint(3, 9)
    player_set: set = set()
    while (number != 0):
        player_set.add(achievements[random.randint(0, len(achievements) - 1)])
        number -= 1
    return player_set


if __name__ == "__main__":
    print("=== Achievement Trcker System ===\n")
    alice_sets = gen_player_achievements()
    bob_sets = gen_player_achievements()
    charlie_sets = gen_player_achievements()
    dylan_sets = gen_player_achievements()
    print(f"Player Alice: {alice_sets}")
    print(f"Player Bob: {bob_sets}")
    print(f"Player charlie: {charlie_sets}")
    print(f"Player dylan: {dylan_sets}\n")
    print("All distinct achievements:" +
          f"{alice_sets.difference(bob_sets, charlie_sets, dylan_sets)}\n")
    print("Common achievements:" +
          f"{alice_sets.intersection(bob_sets, charlie_sets, dylan_sets)}\n")
