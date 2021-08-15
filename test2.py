import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Resources/CovidDataNepal.csv',usecols= ['date','new_cases'])

#data.plot(kind='line',x='date',y='new_cases')

data['date'] = pd.to_datetime(data['date']) 

lastMnth = datetime.now()+relativedelta(months=-1)

start_date = datetime.strftime(lastMnth,"%Y-%m-%d")
end_date = datetime.strftime(datetime.now(),"%Y-%m-%d")

#latestMonthData = data.loc([start_date:end_date])

mask = (data['date'] > start_date) & (data['date'] <= end_date) 

LatestMonthData = data.loc[mask]

Date = matplotlib.dates.date2num(LatestMonthData['date'].tolist())
newCases = matplotlib.dates.date2num(LatestMonthData['new_cases'].tolist())
plt.plot(Date, newCases, label = 'NewCases')

plt.show()