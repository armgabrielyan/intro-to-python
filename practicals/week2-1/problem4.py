import argparse
import datetime 
from dateutil.relativedelta import relativedelta

parser = argparse.ArgumentParser(description = 'Year calculator')
parser.add_argument('--num_y', help = 'Number of years', type = int)
parser.add_argument('--num_d', help = 'Number of days', type = int)

args = parser.parse_args()

current_datetime = datetime.datetime.now()
result_datetime = current_datetime

num_y = 'not given'
num_d = 'not given'

if args.num_y:
  result_datetime += relativedelta(years = args.num_y)
  num_y = args.num_y

if args.num_d:
  result_datetime += datetime.timedelta(days = args.num_d)
  num_d = args.num_d

print('Current date:', current_datetime)
print('Given years:', num_y)
print('Given days:', num_d)
print('Final date:', result_datetime)