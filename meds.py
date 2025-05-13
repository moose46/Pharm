import calendar
import re
from datetime import date, timedelta

from dateutil.relativedelta import *
from dateutil.rrule import *

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# create a date object for Jan 4th of the given year
# This date is always in the first week of the year iso 8601
year = 2025
month = 5
day = 10


jan4 = date(year, 1, 4)

perscription_start_date = date(year, month, day)
perscription_end_date = perscription_start_date + timedelta(days=90)


refill_days = perscription_start_date + relativedelta(day=90)
start_iso_week, start_iso_day = perscription_start_date.isocalendar()[1:3]
# weeks_diff = week - start_iso_week
next_refill = perscription_start_date + timedelta(days=90)
print(f"start-{perscription_start_date} --- end-{perscription_end_date}")
crestor_odd = 0

ezetimibe_odd = 0
crestor_even = 0
ezetimibe_even = 0
# find the next monday
next_monday = perscription_start_date - relativedelta(weekday=MO(1))
x = list(rrule(WEEKLY, dtstart=next_monday, until=next_refill))
# how many days to next monday if Sat, then Monday would be 2 days
first_week_diff = next_monday.day - perscription_start_date.day
print(f"diff = {first_week_diff}")
last_week_diff = perscription_start_date.day - next_refill.day
for y in x:

    # This is an Odd week
    if y.isocalendar().week % 2 == 1:
        print(y.isocalendar())
        ezetimibe_odd += 4
        crestor_odd += 3
        ezetimibe_week = 4
        crestor_week = 3
        print(
            f"{y.month:02}/{y.day:02}/{y.year} -> {days[y.isocalendar().weekday-1]} Odd/Week  Ezetimibe={ezetimibe_odd:02} Crestor={crestor_odd:02} Crestor=3/Week"
        )
        # print(f"Monday = {next_monday.strftime('%m/%d/%Y')}")
    # this is an Even week
    else:
        ezetimibe_even += 5
        crestor_even += 2
        ezetimibe_week = 5
        crestor_week = 2
        print(
            f"{y.month:02}/{y.day:02}/{y.year} -> {days[y.isocalendar().weekday-1]} Even/Week Ezetimibe={ezetimibe_even:02} Crestor={crestor_even:02} Crestor=2/Week"
        )
        # print(f"Monday = {next_monday.strftime('%m/%d/%Y')}")

last_week = x[:-1]
print(f"{x[-1]}")
# print(f"Monday = {next_monday.strftime('%m/%d/%Y')}")
# for i in range(perscription_start_date, perscription_start_date + timedelta(days=90)):
#     print(f"{i}")
print(
    f"Crestor: {crestor_odd + crestor_even} Ezetimibe: {ezetimibe_odd + ezetimibe_even} Total: {crestor_odd + crestor_even + ezetimibe_odd + ezetimibe_even} Completed ..."
)
print(
    f"percsription_start_date = {perscription_start_date} --- last_week_diff={last_week_diff}"
)
print(
    f"percsription_end_date = {perscription_end_date} --- last_week_diff={last_week_diff}"
)
print(f"{perscription_start_date - perscription_end_date }")
print(f"{refill_days}")
