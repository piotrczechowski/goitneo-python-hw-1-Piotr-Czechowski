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


