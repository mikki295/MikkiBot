import datetime

def today():
    date = datetime.date.today()
    return date

def dates_of_current_week():
    dates = []
    first_day = first_date_of_week()

    for i in range(8):
        day = first_day + datetime.timedelta(days=i)
        dates.append(day)


def week_number_today():
    return datetime.date(today().year,today().month,today().day).isocalendar()[1] - 1

def week_number(year,month,day):
    return datetime.date(year,month,day).isocalendar()[1] - 1


def first_date_of_week():
    first_day = today() - datetime.timedelta(today().weekday())
    print(first_day)

def main():
    '''main'''


main()
