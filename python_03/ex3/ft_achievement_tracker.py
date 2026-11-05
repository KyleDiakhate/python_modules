import random

ACHIVEMENT = ["Legend", "Unbeatble", "Master Mind", "Goat", "The Healer", "The Wizard", "Crafter", "Team Leader", "Hot Steak", "Demon", "Angel", "Traitor"]

def gen_player_achievements() -> set:
    qty = random.randint(2, len(ACHIVEMENT))

    ach = random.sample(ACHIVEMENT, qty)

    return set(ach)

if __name__ == "__main__":
    print("=== Achivement Tracker System ===")

    lassana = gen_player_achievements()
    kyle = gen_player_achievements()
    tomas = gen_player_achievements()
    diakhate = gen_player_achievements()


    print(f"Player Lassana Achivements: {lassana}")
    print(f"Player Kyle Achivements: {kyle}")
    print(f"Player Tomas Achivements: {tomas}")
    print(f"Player Diakhate Achivements: {diakhate}\n")

    distinct = lassana.union(kyle,tomas,diakhate)
    print(f"All distinct achivements: {distinct}")

    common = lassana.intersection(kyle,tomas,diakhate)
    print(f"Common achivements: {common}\n")


    exclusive_lassana = lassana.difference(kyle,tomas,diakhate)
    print(f"Only Lassana has: {exclusive_lassana}")
    exclusive_kyle = kyle.difference(lassana,tomas,diakhate)
    print(f"Only Kyle has: {exclusive_kyle}")
    exclusive_tomas = tomas.difference(kyle,lassana,diakhate)
    print(f"Only Tomas has: {exclusive_tomas}")
    exclusive_diakhate = diakhate.difference(kyle,tomas,lassana)
    print(f"Only Diakhate has: {exclusive_diakhate}\n")

    all_achivements = set(ACHIVEMENT)
    missing_lassana = all_achivements.difference(lassana)
    print(f"Lassana is missing: {missing_lassana}")
    missing_kyle = all_achivements.difference(kyle)
    print(f"Kyle is missing: {missing_kyle}")
    missing_tomas = all_achivements.difference(tomas)
    print(f"Tomas is missing: {missing_tomas}")
    missing_diakhate = all_achivements.difference(diakhate)
    print(f"Diakhate is missing: {missing_diakhate}\n")

