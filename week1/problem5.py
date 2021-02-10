import datetime
import time
import calendar

current_datetime = datetime.datetime.now()
delta = datetime.timedelta(days = 5)

print('Current date and time:', current_datetime)
print('Current year:', current_datetime.year)
print('Current month:', current_datetime.month)
print('Current day of week:', current_datetime.weekday())
print('Current date and time added 5 days:', current_datetime + delta)
print('Current date and time substracted 5 days:', current_datetime - delta)
