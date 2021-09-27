import datetime as dt
import time as tm
#pints current time/ represents the no. of seconds since Jan 1,1970. "EPOCH"
tm.time()
#Timestamp- time registered to a file when data is added, deleted or modified
dtnow= dt.datetime.fromtimestamp(tm.time())
print(dtnow)    #prints the current date and time

#cureent date,time and year
print(dtnow.year,dtnow.month,dtnow.day,dtnow.hour,dtnow.minute,dtnow.second)

#Timedelta- it is a time duration between two deltas
delta=dt.timedelta(days=10)

#current date
today=dt.date.today()
print(today)
