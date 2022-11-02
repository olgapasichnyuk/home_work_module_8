from datetime import datetime, timedelta

users = [
    {"name": "Ron", "birthday": datetime(year=1987, month=11, day=14)},
    {"name": "Julia", "birthday": datetime(year=1967, month=11, day=5)},
    {"name": "Harry", "birthday": datetime(year=1997, month=11, day=6)},
    {"name": "Fred", "birthday": datetime(year=1993, month=11, day=7)},
    {"name": "Carry", "birthday": datetime(year=1988, month=11, day=8)},
    {"name": "Kelly", "birthday": datetime(year=1999, month=11, day=8)},
    {"name": "Bin", "birthday": datetime(year=2000, month=11, day=9)},
    {"name": "Wolter", "birthday": datetime(year=2002, month=11, day=9)},
    {"name": "Helen", "birthday": datetime(year=1997, month=11, day=10)},
    {"name": "Paula", "birthday": datetime(year=1978, month=11, day=11)},
    {"name": "Ross", "birthday": datetime(year=1980, month=12, day=4)},
    {"name": "Kali", "birthday": datetime(year=1997, month=10, day=15)},
    {"name": "Larry", "birthday": datetime(year=1967, month=2, day=26)},
    {"name": "Fredy", "birthday": datetime(year=1993, month=1, day=7)},
    {"name": "Larry", "birthday": datetime(year=1988, month=11, day=18)},
    {"name": "Nelly", "birthday": datetime(year=1989, month=9, day=28)},
    {"name": "Bonny", "birthday": datetime(year=2000, month=7, day=3)},
    {"name": "Would", "birthday": datetime(year=2002, month=11, day=11)},
    {"name": "Holly", "birthday": datetime(year=1997, month=11, day=3)},
    {"name": "Molly", "birthday": datetime(year=1978, month=11, day=8)}
]


def print_result(result_list):
    for day_key, name_list in result_list.items():

        if name_list:
            print(f'{day_key}: {", ".join(name_list)}')
        else:
            print(f"{day_key}: no one has a birthday today ")


def get_birthdays_per_week(employees: list):
    days_dict = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday"}
    day = datetime.now()

    next_week_list = []
    result = {}

    while day < (datetime.now() + timedelta(days=7)):

        day += timedelta(days=1)
        next_week_list.append(day)

        if day.weekday() in range(5):
            result[days_dict[day.weekday()]] = []

    for day in next_week_list:

        for employee in employees:

            if (day.month == employee["birthday"].month) and (day.day == employee["birthday"].day) and (
                    day.weekday() in range(5)):

                result[days_dict[day.weekday()]].append(employee["name"])

            elif (day.month == employee["birthday"].month) and (day.day == employee["birthday"].day) and (
                    day.weekday() in range(5, 7)):
                result[days_dict[0]].append(employee["name"])

    print_result(result)


if __name__ == "__main__":
    get_birthdays_per_week(users)
