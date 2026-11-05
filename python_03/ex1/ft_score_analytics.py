import sys

if __name__ == "__main__":
    score = []

    i = 1
    print("=== Player Score Analytics ===")
    while i <= len(sys.argv) - 1:
        try:
            num = int(sys.argv[i])
            score.append(num)
        except ValueError as e: 
            print(f"Invalid Parameters: {sys.argv[i]}")
        i += 1
    if len(score) > 0:
        print(f"Scores processed: {score}")
        print(f"Total Player: {len(score)}")
        print(f"Total Score: {sum(score)}")
        print(f"Average Score: {sum(score) / len(score)}")
        print(f"High Score: {max(score)}")
        print(f"Low Score: {min(score)}")
        print(f"Score range: {max(score) - min(score)}")
    else:
         print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
