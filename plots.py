# Import Statements

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from google.colab import files
uploaded = files.upload()

# Read the Data
df_tesla = pd.read_csv('TESLA Search Trend vs Price.csv')

df_btc_search = pd.read_csv('Bitcoin Search Trend.csv')
df_btc_price = pd.read_csv('Daily Bitcoin Price.csv')

df_unemployment = pd.read_csv('UE Benefits Search vs UE Rate 2004-19.csv')
df_unemployment.head()

# Data Exploration
#Tesla

print(f'Largest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.max()}')
print(f'Smallest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.min()} ')


"""### Unemployment Data"""

print(f'Largest value for Unemployemnt Benefits {df_unemployment.UE_BENEFITS_WEB_SEARCH.max()}')

"""### Bitcoin"""

print(f'largest BTC News Search: ')

#DATA CLEANING
print(f'Missing values for Tesla?: {df_tesla.isna().values.any()}')
print(f'Missing values for U/E?: {df_unemployment.isna().values.any()}')
print(f'Missing values for BTC Search?: {df_btc_search.isna().values.any()} ')

print(f'Missing values for BTC price?:{df_btc_price.isna().values.any()} ')

print(f'Number of missing values: {df_btc_price.isna().values.sum()}')

"""**Challenge**: Remove any missing values that you found."""

df_btc_price.dropna(inplace=True)

type(df_tesla.MONTH[0])

df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)

df_btc_search.MONTH = pd.to_datetime(df_btc_search.MONTH)

df_unemployment.MONTH = pd.to_datetime(df_unemployment.MONTH)
df_btc_price.DATE = pd.to_datetime(df_btc_price.DATE)

### Converting from Daily to Monthly Data

df_btc_monthly = df_btc_price.resample('ME', on= 'DATE').last()

print(df_btc_monthly.shape)
df_btc_monthly.head()

# Data Visualisation

# Create locators for ticks on the time axis

years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')

# Register date converters to avoid warning messages

# Tesla Stock Price v.s. Search Volume


plt.figure(figsize=(14,8), dpi=120)
plt.title('Tesla Web Search vs Price', fontsize=18)
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.set_ylabel("TESLA Stock Price", color='red',fontsize=14)
ax2.set_ylabel("Search Trend",color='blue', fontsize=14)
ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='red',linewidth=3)
ax2.plot(df_tesla.MONTH,df_tesla.TSLA_WEB_SEARCH, color='blue', linewidth=3)
ax1.set_ylim([0, 600])
ax1.set_xlim([df_tesla.MONTH.min(), df_tesla.MONTH.max()])
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)
plt.show()

#bitcoin price

plt.figure(figsize=(14,8), dpi=120)
plt.title('Bitcoin Prices vs. Search volumes', fontsize=18)
plt.xticks(fontsize=14,rotation=45)
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.set_ylabel("BTC Price", color='red',fontsize=14)
ax2.set_ylabel("Search Trend",color='blue', fontsize=14)
ax1.plot(df_btc_monthly.index, df_btc_monthly.CLOSE, color='red',linewidth=3, linestyle='--')
ax2.plot(df_btc_monthly.index,df_btc_search.BTC_NEWS_SEARCH, color='blue', linewidth=3, marker = 'o')
ax1.set_ylim([0, 15000])
ax1.set_xlim([df_btc_monthly.index.min(), df_btc_monthly.index.max()])
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)
plt.show()

#Unemployement Benefits Search vs. Actual Unemployment in the U.S.
plt.figure(figsize=(14,8),dpi=120)
plt.title('Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate')
plt.yticks(fontsize=14)
plt.xticks(fontsize=14)
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.set_ylabel("FRED U/E Rate", color='purple',fontsize=14)
ax2.set_ylabel("Search Trend", color='orange',fontsize=14)

ax1.set_ylim(3,10.5)
ax1.set_xlim(df_unemployment.MONTH.min(),df_unemployment.MONTH.max())
ax1.grid(color='grey',linestyle='--')
ax1.plot(df_unemployment.MONTH, df_unemployment.UNRATE, color='purple',linewidth=3,linestyle='--')
ax2.plot(df_unemployment.MONTH, df_unemployment.UE_BENEFITS_WEB_SEARCH,color='orange',linewidth=3)

#UE Benefits Search vs UE Rate 2004
df_bs = pd.read_csv('UE Benefits Search vs UE Rate 2004-20.csv')

df_bs.MONTH=pd.to_datetime(df_bs.MONTH )
df_bs.head()

plt.figure(figsize=(14,8), dpi=120)
plt.title('UE Benefits Search vs UE Rate')


plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)
ax1=plt.gca()
ax2=ax1.twinx()

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=16)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=16)

ax1.set_xlim([df_bs.MONTH.min(), df_bs.MONTH.max()])

ax1.plot(df_bs.MONTH, df_bs.UNRATE, 'purple', linewidth=3)
ax2.plot(df_bs.MONTH, df_bs.UE_BENEFITS_WEB_SEARCH, 'skyblue', linewidth=3)

plt.show()