from week_birthdays import *

def main():

    users = [
        {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
        {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
        {"name": "Steve Jobs", "birthday": datetime(1955, 2, 24)},
        {"name": "Mark Zuckerberg", "birthday": datetime(1984, 5, 14)},
        {"name": "Elon Musk", "birthday": datetime(1971, 6, 28)},
        {"name": "Piotr Czechowski", "birthday": datetime(1982, 6, 6)}
        ]

    print("Birthdays for all users:")
    get_birthdays_per_week(users)

if __name__ == "__main__":
    main()
