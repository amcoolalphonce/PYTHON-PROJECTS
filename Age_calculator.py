def age_calculator(y, m, d):
    import datetime
    today = datetime.datetime.now().date()   #get the current date/ todays date
    now = datetime.date(y, m, d) #object representing the year, month and day
    age = int((today-now).days / 365.25) #finds the difference
    print(age)
age_calculator(2001, 12, 3)