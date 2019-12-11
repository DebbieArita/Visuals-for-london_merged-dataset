# bar graph 1
import pandas
import matplotlib.pyplot as plt
df = pandas.read_csv("london_merged.csv", parse_dates=['timestamp'])
print(df)

df['is_weekend'].replace({1: 'weekend', 0: 'not weekend'}, inplace=True)
df['season'].replace({0: 'spring', 1: 'summer', 2:'fall', 3: 'winter'}, inplace=True)
df['is_holiday'].replace({1: 'holiday', 0: 'not holiday'}, inplace=True)


df.groupby(['season', 'is_weekend'])['cnt']. sum().unstack().plot(kind='bar', stacked=False)
# True stacked, false unstacked
plt.title('Stacked Bar graph')
plt.xlabel('season')
plt.ylabel('cnt')
plt.legend(loc='best')
plt.show()


# bar graph 2
import pandas
import matplotlib.pyplot as plt


df.groupby(['is_holiday', 'season'])['wind_speed']. sum().unstack().plot(kind='bar', stacked=False)
# True stacked, false unstacked
plt.title('Stacked Bar graph')
plt.xlabel('is_holiday')
plt.ylabel('wind_speed')
plt.legend(loc='best')
plt.show()


# scatter
import matplotlib.pyplot as plt
figure, ax = plt.subplots()
ax.scatter(df['t1'], df['t2'], color='blue', s=30)
ax.set_title('Relationship of t1 against t2')
ax.set_xlabel('t1')
ax.set_ylabel('t2')
plt.show()

# heat maps - show correlation for multiple variables
import seaborn as sns
figure, ax = plt.subplots()
df_x = df[['cnt', 'hum', 'wind_speed', 't1', 't2']]
sns.heatmap(df_x.corr(), cmap='Blues', annot=True)
ax.set_title('Relations between Variables')
plt.show()


# pie
figure, ax = plt.subplots()
df.groupby('season').size().plot(kind='pie', autopct='%1.1f%%')
ax.set_title('Distribution of seasons')
ax.set_ylabel('')
plt.show()

#  pie 2
figure, ax = plt.subplots()
df.groupby('is_holiday').size().plot(kind='pie', autopct='%1.1f%%')
ax.set_title('Distribution of is_holiday')
ax.set_ylabel('')
plt.show()

# pie 3
figure, ax = plt.subplots()
df.groupby('is_weekend').size().plot(kind='pie', autopct='%1.1f%%')
ax.set_title('Distribution of is_weekend')
ax.set_ylabel('')
plt.show()


# timeseries
date = pandas.to_datetime(['2015-01-04', '2015-01-06', '2015-01-11', '2015-01-15', '2015-01-20', '2015-01-25', '2015-01-30'])
print(date)
df = df.set_index('timestamp')
print(df)

# using loc
print(df.loc['2015-01-04': '2015-01-30'])
print("===========")

#plotting
df.loc['2015-01-04':'2015-01-30', 'cnt'].plot()
plt.title('Bike sharing in Jan, 2015')
plt.xlabel('January, 2015')
plt.ylabel('cnt')
plt.show()

