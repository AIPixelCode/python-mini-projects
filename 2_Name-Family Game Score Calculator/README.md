# Name-Family Game Score Calculator

A lightweight Python application that automatically calculates players' scores in a **Name-Family** game using a CSV dataset of valid answers and predefined scoring rules.

The project focuses on providing a clean, modular implementation that separates game logic from the dataset while remaining simple to use and easy to extend.

---

## Features

* Load valid answers from a CSV dataset
* Register multiple participants
* Validate answers by category
* Detect duplicate answers
* Handle empty responses
* Calculate final scores automatically
* Uses only Python's standard library

---

## Project Structure

```text
Name-Family-Game-Score-Calculator
│
├── game.py
├── game_data.csv
├── main.py
├── Documentation.pdf
├── README.md
└── LICENSE
```

| File                | Description                      |
| ------------------- | -------------------------------- |
| `game.py`           | Core game logic                  |
| `game_data.csv`     | Dataset of valid answers         |
| `main.py`           | Example application              |
| `Documentation.pdf` | Complete technical documentation |

---

## Requirements

* Python 3.8 or later

No external dependencies are required.

---

## Quick Start

Run the example application:

```bash
python main.py
```

---

## Example

```python
from game import ready_up, add_participant, calculate_all

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
        "name": "Andrew",
        "family": "Adams",
        "country": "Argentina",
        "color": "Blue",
        "object": "Book",
        "food": "Apple Pie",
    },
)

scores = calculate_all()

for player, score in scores.items():
    print(player, score)
```

---

## Sample Output

```text
==============================
 Final Scores
==============================
Alice       65 pts
Bob         60 pts
Charlie     60 pts
David       40 pts
```

---

## Documentation

Detailed information about the project's architecture, implementation, data structures, and scoring algorithm is available in **Documentation.pdf**.

---

#### Author: AiPixelCode