import datetime


def __week_number_today():
    return datetime.date(today().year,today().month,today().day).isocalendar()[1] - 1

def __week_number(year,month,day):
    return datetime.date(year,month,day).isocalendar()[1] - 1


def __first_date_of_week():
    first_day = today() - datetime.timedelta(today().weekday())
    return first_day

def today():
    date = datetime.date.today()
    return date

def dates_of_current_week():
    dates = []
    first_day = __first_date_of_week()

    for i in range(7):
        day = first_day + datetime.timedelta(days=i)
        dates.append(day)
    
    return dates

def main():
    '''main'''
    dates_of_current_week()


main()
