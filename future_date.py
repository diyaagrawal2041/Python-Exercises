#Suppose we want to calculate date after 1 month from now
import datetime as dt
#CURRENT TIME
current_date=dt.date.today()
print("Current_date= ",current_date)
#FUTURE DATE AFTER 1 MONTH
future_date=dt.timedelta(days=30)
result=current_date+future_date
print("Future_date= ",result)
