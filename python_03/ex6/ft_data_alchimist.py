import random 

if __name__ == "__main__":
    print("=== Game Data Alchimist ===")
    initial_name = ["Gabriel", "José", "kyle", "ana", "Lassana", "tomas", "Diakhate"]

    print(f"Inicial list of players: {initial_name}")

    all_names = [name.capitalize() for name in initial_name]
    print(f"New list with names capitalized: {all_names}")

    initial_capitalized = [name for name in initial_name if name.istitle()]
    print(f"New list of capitalized names only: {initial_capitalized}")

    players_score = {name: random.randint(10, 1000) for name in all_names}
    print(f"Score dict: {players_score}")

    average_score =  sum(players_score.values()) / len(all_names)
    print(f"Score Average: {average_score:.2f}")

    high_scores = {name: score for name,score in players_score.items() if score > average_score}
    print(f"High Score: {high_scores}")
