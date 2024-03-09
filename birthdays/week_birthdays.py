from datetime import datetime

def get_birthdays_per_week(users):
    # Data structure to store birthdays for each day of the week
    birthdays_per_week = {
        'Monday': [], 
        'Tuesday': [], 
        'Wednesday': [],
        'Thursday': [], 
        'Friday': [], 
        'Saturday': [], 
        'Sunday': []
    }
    
    # Iterate over the list of users
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        
        # Calculate the day of the week for the birthday
        day_of_week = birthday.strftime('%A')
        
        # Adjust birthday to Monday if falls on the weekend
        if day_of_week in ['Saturday', 'Sunday']:
            day_of_week = 'Monday'
        
        # Store the username on the corresponding day of the week
        birthdays_per_week[day_of_week].append(name)
    
    # Display the collected names by day of the week in the appropriate format
    for day, names in birthdays_per_week.items():
        if names:
            print(f"{day}: {', '.join(names)}")

# Example usage: 
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
