


def main():
    month = int(input("Enter the month number: "))
    assert 1<=month<=12
    year = int(input("Enter the year: "))
    assert year>=1753
    year_days = days_in_years(year)
    month_days = days_in_current_year(year,month)
    dow = day_of_week(year_days,month_days)
    dom = days_in_month(month,year)
    display_table(dow,dom)

def is_leap_year(year):
    if year % 4 == 0 or year % 400 == 0 :
        if year % 100 == 0:
            return False
        else:
            return True
    else:
        return False

def days_in_years(year):
    days = 0
    for year_count in range(1753,year,1):
        if is_leap_year(year_count) == True:
            days +=366
        else:
            days += 365
    return days

def days_in_current_year(year,month):
    days = 0
    for month_count in range(1,month):
        month_days = days_in_month(month_count,year)
        days +=month_days
    return days

def days_in_month(month,year):
    days = 0
    if month == 4 or month == 6 or month == 9 or month== 11:
            days = 30
    elif month == 2:
        if is_leap_year(year) == True:
            days = 29
        else:
            days =28
    else:
        days = 31
    return days

def day_of_week(year_days, month_days):
    return (year_days+month_days+1) % 7
    


def display_table(dow,dom):
    table = ""
    print("Su  Mo  Tu  We  Th  Fr  Sa")
    for index in range(0,dow):
        table +="    "
    for index in range(1,dom+1):
        if index<10:
            table += " "
        table += str(index)
        table += "  "
        dow +=1
        if dow%7 == 0:
            table += "\n"

    print(table)
if __name__ == "__main__":
    main()