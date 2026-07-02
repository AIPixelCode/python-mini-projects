# Economic System Simulator

## Description

This project implements a simple economic simulation using object-oriented programming in Python.

The system models different types of people and workplaces, allowing employees to be hired, workplaces to be upgraded, financial values to be calculated, and the overall economy of the simulation to be evaluated.

The project demonstrates how multiple interacting classes can be organized into a maintainable and extensible object-oriented design.

---

## Features

- Multiple employee types
  - Worker
  - Teacher
  - Engineer

- Multiple workplace types
  - Mine
  - School
  - Company

- Employee hiring system

- Workplace capacity management

- Level upgrade system for both people and workplaces

- Daily income and living cost calculations

- Workplace maintenance cost calculations

- Overall economy summary

- Custom exception handling for full workplaces

---

## Project Structure

```text
economic_system_simulator/
│
├── person.py
├── worker.py
├── teacher.py
├── engineer.py
│
├── work_place.py
├── mine.py
├── school.py
├── company.py
│
└── main.py
```

---

## How It Works

The simulation starts by creating people and workplaces.

Employees can then be hired into workplaces if capacity is available.

Each person calculates daily income and living costs based on their profession, while workplaces calculate their maintenance costs according to their type and level.

The simulator also supports upgrading both employees and workplaces, affecting financial calculations and workplace capacity.

Finally, the program generates a financial summary showing the contribution of people, workplaces, and the overall economy.

---

## Example Output

```text
========================================================================
                       ECONOMIC SYSTEM SIMULATOR
========================================================================

Creating people...

✓ Engineer created
✓ Teacher created
✓ Worker created

...

========================================================================
                        PEOPLE FINANCIAL REPORT
========================================================================
Name        Job             Income      Cost       Balance
------------------------------------------------------------------------
Raha        engineer           707       424        990.00
Sara        teacher            200       250         32.84
Taha        worker             545       293        797.00

...

========================================================================
                            ECONOMY SUMMARY
========================================================================
People Net Balance          :    1819.84
Workplace Net Balance       :   -2600.00
------------------------------------------------------------------------
Overall Net Balance         :    -780.16
```

---

## Source Code

**Main File:** `main.py`

---

#### Author: AiPixelCode