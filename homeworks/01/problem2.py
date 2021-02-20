# 1)

import datetime
import time
import calendar

# 2)

birthday = datetime.datetime(1999, 4, 16)

# a)

print('Date of birthday:', birthday.date())

# b)

print('Year of birthday:', birthday.year)

# c)

print('Month of birthday:', calendar.month_name[birthday.month])

# d)

print('Day of birthday:', birthday.day)

# e)

print('Week day of birthday:', calendar.day_name[birthday.weekday()])

# f)

upcoming_birthday = datetime.datetime(2021, 4, 16)
till_upcoming = upcoming_birthday - datetime.datetime.now()

print('Days till upcoming birthday:', till_upcoming.days)

# 3)

print(calendar.month(2017, 5))

# 4)

yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)

print('Yesterday:', yesterday)

# a)

print('Two days after yesterday:', yesterday + datetime.timedelta(days = 2))

# b)

print('Three days before yesterday:', yesterday - datetime.timedelta(days = 3))
