def get_choice() -> bool:
    i = input("Print race times? (y/n): ").strip().lower()
    if i == "y":
        return True
    elif i == "n":
        return False
    else:
        return get_choice()


def get_scores() -> list:
    while True:
        try:
            inp = input("Enter a list of scores, separated by commas: ").split(",")
            assert len(inp) > 0
            scores = [int(n) for n in inp]
            assert all(n >= 0 for n in scores)
            assert len(scores) > 0
            return scores
        except (AssertionError, ValueError):
            print("Invalid input. Please try again.")


choice = get_choice()
scores = get_scores()
if choice:
    for score in scores:
        print(f"{score}s - {score // 3600}h {(score % 3600) // 60}m {score % 60}s")
else:
    for score in scores:
        print(score)
