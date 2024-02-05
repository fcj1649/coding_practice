import math
import datetime
import pathlib, os
from dateutil import parser 

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)+1):
        yield start_date + datetime.timedelta(n)

path = os.path.join(pathlib.Path(__file__).parent.resolve(),'avg_mon_balance.csv')

file = open(path, 'r')
header = file.readline()
balances = {}

format = "%m/%d/%Y"
for line in file.readlines():
    inp = line.strip().split(',')
    dat = str(datetime.datetime.strptime(inp[0], format).date().strftime("%Y%m%d"))
    balances[dat] = float(inp[1])
file.close()
print(balances)

start_date = datetime.date(2023, 11, 1)
end_date = datetime.date(2024, 1, 31)

for single_date in daterange(start_date, end_date):
    curr_date = str(single_date.strftime("%Y%m%d"))
    prev_date = str((single_date - datetime.timedelta(days = 1)).strftime("%Y%m%d"))
    if(curr_date not in balances):
        balances[curr_date] = balances[prev_date]


path = os.path.join(pathlib.Path(__file__).parent.resolve(),'avg_mon_balance_out.csv')
file = open(path, 'w')
file.write("Date,Balance,D\n")
for idx, val in enumerate(balances):
    curr_date = parser.parse(val)
    file.write(str(curr_date.strftime(format)) + ',' + str(balances[val]) + ',\n')
file.close()

