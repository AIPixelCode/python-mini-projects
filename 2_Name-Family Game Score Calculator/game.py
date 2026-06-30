import csv

# Global data structures
valid_words = {}
players = {}
answer_counts = {}
player_scores = {}
categories_with_missing_answers = set()


def normalize(text):
    """
    Normalize an answer by removing all spaces.
    """
    return text.replace(" ", "")


def ready_up():
    """
    Load all valid words from the CSV file and initialize game data.
    """

    valid_words.clear()
    players.clear()
    answer_counts.clear()
    player_scores.clear()
    categories_with_missing_answers.clear()

    categories = []

    with open("game_data.csv", newline="", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)

        for row_index, row in enumerate(reader):

            if row_index == 0:
                for category in row:
                    category = normalize(category)
                    categories.append(category)
                    valid_words[category] = []
                    answer_counts[category] = {}

            else:
                for column_index, word in enumerate(row):
                    if word == "":
                        continue

                    normalized_word = normalize(word)
                    valid_words[categories[column_index]].append(normalized_word)


def add_participant(participant, answers):
    """
    Add a participant and store all of their answers.
    """

    players[participant] = answers

    for category, answer in answers.items():

        normalized_answer = normalize(answer)

        if normalized_answer == "":
            categories_with_missing_answers.add(category)
            continue

        if normalized_answer not in answer_counts[category]:
            answer_counts[category][normalized_answer] = 1
        else:
            answer_counts[category][normalized_answer] += 1


def calculate_all():
    """
    Calculate and return the final score of every participant.
    """

    player_scores.clear()

    for participant, answers in players.items():

        total_score = 0

        for category, answer in answers.items():

            normalized_answer = normalize(answer)

            if normalized_answer not in valid_words[category]:
                continue

            repeated = answer_counts[category][normalized_answer] > 1
            missing_exists = category in categories_with_missing_answers

            if missing_exists:
                total_score += 10 if repeated else 15
            else:
                total_score += 5 if repeated else 10

        player_scores[participant] = total_score

    return player_scores