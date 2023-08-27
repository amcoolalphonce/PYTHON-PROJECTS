import calendar

def main():
    try:
        year = int(input("Enter a year: "))
        if year < 1:
            raise ValueError
        print_calendar(year)

    except ValueError:
        print("Enter a valid positive year.")

def print_calendar(year):
    cal_year = calendar.TextCalendar(calendar.SUNDAY)