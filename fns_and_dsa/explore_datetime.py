# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in 'YYYY-MM-DD HH:MM:SS' format.
    """
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date  # return so it can be reused in other functions if needed


def calculate_future_date(current_date):
    """
    Ask the user for a number of days and calculate the future date.
    """
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        future_date = current_date + timedelta(days=days_to_add)
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid input. Please enter an integer number of days.")


def main():
    current_date = display_current_datetime()
    calculate_future_date(current_date)


if __name__ == "__main__":
    main()
