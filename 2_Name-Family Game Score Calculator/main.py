from game import ready_up, add_participant, calculate_all


def main():
    ready_up()

    add_participant(
        participant="Alice",
        answers={
            "name": "Alice",
            "family": "Anderson",
            "country": "Australia",
            "color": "Amber",
            "object": "Anchor",
            "food": "Apple Pie",
        },
    )

    add_participant(
        participant="Bob",
        answers={
            "name": "Bob",
            "family": "Brown",
            "country": "Brazil",
            "color": "Blue",
            "object": "Bottle",
            "food": "Burger",
        },
    )

    add_participant(
        participant="Charlie",
        answers={
            "name": "Charlie",
            "family": "Clark",
            "country": "Canada",
            "color": "Blue",          # Duplicate answer
            "object": "Camera",
            "food": "Cake",
        },
    )

    add_participant(
        participant="David",
        answers={
            "name": "Daniel",         # Invalid name
            "family": "Davis",
            "country": "Denmark",
            "color": "",              # Missing answer
            "object": "Desk",
            "food": "Pizza",          # Invalid food
        },
    )

    scores = calculate_all()

    print("=" * 30)
    print(" Final Scores")
    print("=" * 30)

    for player, score in sorted(scores.items(), key=lambda item: item[1], reverse=True):
        print(f"{player:<10} {score:>3} pts")


if __name__ == "__main__":
    main()