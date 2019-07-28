import datetime

def today():
    date = datetime.date.today()
    return date

def dates_of_week():
    '''Returns days of the week'''
    dates = []
    #weekday = today().isoweekday()
    weekday = datetime.date(2019,7,24).isoweekday()

def week_number_today():
    return datetime.date(today().year,today().month,today().day).isocalendar()[1]

def week_number(year,month,day):
    return datetime.date(year,month,day).isocalendar()[1]

def main():
    '''main'''
    dates_of_week()

    print(week_number(2019,7,21))


main()
