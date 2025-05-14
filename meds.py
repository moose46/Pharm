"""_summary_
Author: Robert Wayne Curtiss
Date: 5/13/2025
Counts ezetimibe and crestor doses for a 90 day period
Rules:S
    ezetimibe every sat and sun
    every other week:
    Even week:
        ezetimibe mon, wed, fri
        crestor tue, wed
    Odd week
        ezetimibe tue, thur
        crestor mon, wed, fri
"""

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

# Perscription starting date
perscription_start_date = date(year, month, day)
# Perscription start date + perscription length in days
perscription_end_date = perscription_start_date + timedelta(days=89)

# init variables
ezetimibe = 0
crestor = 0
# make a lif of all days betwwen perscription start date and end date
x = list(rrule(DAILY, dtstart=perscription_start_date, until=perscription_end_date))

# loop through all the perscription days
for y in x:

    # This is an Even week
    if y.isocalendar().week % 2 == 0:
        # Sun, Mon, Wed, Fri, Sat
        if y.isoweekday() in [1, 2, 4, 6, 7]:
            ezetimibe += 1

        # Tue and Thursday
        if y.isoweekday() in [3, 5]:
            crestor += 1
    # this is an Odd week
    else:
        # Sun, Tue, Thur, Sat
        if y.isoweekday() in [1, 3, 5, 7]:
            ezetimibe += 1
        # Mon, Wed, Fri
        if y.isoweekday() in [2, 4, 6]:
            crestor += 1
print(f"start-{perscription_start_date} --- end-{perscription_end_date}")
# print(f"{perscription_end_date - perscription_start_date}")
print(f"ezetimibe={ezetimibe}\ncrestor={crestor}\ntotal={ezetimibe+crestor}")
