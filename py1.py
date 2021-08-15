from dateutil.relativedelta import relativedelta
import datetime

before = datetime.datetime.now()
after1 = datetime.datetime.now() + relativedelta(months=-1)

after = datetime.datetime.strftime(after1,"%Y-%m-%d")

print(before)
print(after)