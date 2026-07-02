from engineer import Engineer
from teacher import Teacher
from worker import Worker

from mine import Mine

from person import Person
from work_place import WorkPlace, WorkPlaceIsFull


LINE = "=" * 90
SUB_LINE = "-" * 90


def title(text: str):
    print(f"\n{LINE}")
    print(text.center(72))
    print(LINE)


def people_table():
    print(
        f"{'Name':<12}"
        f"{'Job':<12}"
        f"{'Age':>6}"
        f"{'Level':>8}"
    )
    print(SUB_LINE)

    for person in Person.instances:
        print(
            f"{person.name:<12}"
            f"{person.get_job():<12}"
            f"{person.age:>6}"
            f"{person.level:>8}"
        )


def workplace_table():
    print(
        f"{'Name':<20}"
        f"{'Type':<10}"
        f"{'Level':>8}"
        f"{'Capacity':>12}"
        f"{'Build':>10}"
        f"{'Daily Cost':>14}"
        f"{'Balance':>12}"
    )
    print(SUB_LINE)

    for workplace in WorkPlace.instances:
        print(
            f"{workplace.name:<20}"
            f"{workplace.get_expertise():<10}"
            f"{workplace.level:>8}"
            f"{workplace.capacity:>12}"
            f"{workplace.get_price():>10}"
            f"{workplace.calc_costs():>14}"
            f"{workplace.calc():>12}"
        )


def financial_table():
    print(
        f"{'Name':<12}"
        f"{'Job':<12}"
        f"{'Income':>10}"
        f"{'Cost':>10}"
        f"{'Balance':>14}"
    )
    print(SUB_LINE)

    for person in Person.instances:
        income = person.calc_income()
        cost = person.calc_life_cost()
        balance = person.calc()

        print(
            f"{person.name:<12}"
            f"{person.get_job():<12}"
            f"{income:>10}"
            f"{cost:>10}"
            f"{balance:>14.2f}"
        )


def main():
    title("ECONOMIC SYSTEM SIMULATOR")

    print("Creating people...\n")

    engineer = Engineer("Raha", 30)
    teacher = Teacher("Sara", 25)
    worker = Worker("Taha", 22)

    print("✓ Engineer created")
    print("✓ Teacher created")
    print("✓ Worker created")

    title("PEOPLE")

    people_table()

    title("CREATE WORKPLACE")

    mine = Mine("Kavir Mine")

    print("✓ Mine created")

    title("INITIAL WORKPLACE STATUS")

    workplace_table()

    title("UPGRADE WORKPLACE")

    print("Upgrading workplace level...\n")

    mine.upgrade()

    print(f"✓ {mine.name} upgraded to Level {mine.level}")

    title("WORKPLACE STATUS")

    workplace_table()

    title("HIRE EMPLOYEES")

    for employee in (engineer, teacher, worker):
        mine.hire(employee)
        print(f"✓ {employee.name:<10} hired as {employee.get_job()}")

    print("\nCurrent employees:")

    for index, employee in enumerate(mine.employees, start=1):
        print(f"{index}. {employee.name} ({employee.get_job()})")

    title("UPGRADE PEOPLE")

    engineer.upgrade()
    worker.upgrade()

    print(f"✓ {engineer.name} upgraded to Level {engineer.level}")
    print(f"✓ {worker.name} upgraded to Level {worker.level}")

    title("UPDATED PEOPLE")

    people_table()

    title("PEOPLE FINANCIAL REPORT")

    financial_table()

    title("WORKPLACE FINANCIAL REPORT")

    workplace_table()

    title("ECONOMY SUMMARY")

    people_balance = Person.calc_all()
    workplace_balance = WorkPlace.calc_all()
    overall_balance = people_balance + workplace_balance

    print(f"{'People Net Balance':<28}: {people_balance:>10.2f}")
    print(f"{'Workplace Net Balance':<28}: {workplace_balance:>10.2f}")
    print(SUB_LINE)
    print(f"{'Overall Net Balance':<28}: {overall_balance:>10.2f}")

    title("CAPACITY TEST")

    print("Attempting to hire two more employees...\n")

    ali = Worker("Ali", 20)
    mina = Teacher("Mina", 24)

    try:
        mine.hire(ali)
        print(f"✓ {ali.name} hired successfully.")

        mine.hire(mina)
        print(f"✓ {mina.name} hired successfully.")

    except WorkPlaceIsFull as error:
        print(f"✗ {mina.name} could not be hired.")
        print(f"Reason: {error}")

    title("DEMONSTRATION FINISHED")

    print("All features were executed successfully.")


if __name__ == "__main__":
    main()