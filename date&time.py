from datetime import date
from datetime import datetime,timedelta
from time import time,ctime,localtime
print(time())
print(ctime(time()).capitalize())
print(ctime(time()).casefold())
print(localtime().tm_hour)
print(localtime().tm_year)
date_time = datetime.timestamp(datetime.now())
from_time = datetime.fromtimestamp(1716298175.739432)
# print(date_time)
# print(from_time)
today = date.today()
str = date.isoformat(today)
timedel = datetime.now() - timedelta(days=100)
# print(today.year)
# print(today.month)
# print(today.day)