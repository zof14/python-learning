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