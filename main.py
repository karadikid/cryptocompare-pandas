# Import dotenv
import os
from dotenv import load_dotenv


# Import library for cryptocompare data
import cryptocompare

# Import data manipulation library
import pandas as pd

# Import datetime package
from datetime import datetime

# Import matplotlib and set the style for plotting
import matplotlib.pyplot as plt
from dotenv import load_dotenv

load_dotenv()

# %matplotlib inline

plt.style.use('seaborn-v0_8-darkgrid')

# Get the API key from the Quantra file located inside the data_modules folder
cryptocompare_API_key = os.getenv('API_KEY')

# Set the API key in the cryptocompare object
# cryptocompare.cryptocompare._set_api_key_parameter(cryptocompare_API_key)
cryptocompare.cryptocompare._set_api_key_parameter(os.getenv('API_KEY'))

print("API Key set!")

if(os.path.exists('./all_tickers.csv')):
    all_tickers_csv = open('./all_tickers.csv', "r")
    all_tickers = pd.read_csv(all_tickers_csv)
    print(all_tickers.head(6))
    print(all_tickers.tail(5))
    # Preview the first 6 columns and the last 5 rows of the ticker list
    # print(all_tickers.iloc[:, :5].tail())

else:
    raw_ticker_data = cryptocompare.get_coin_list()
    # Convert the raw data from dictionary format to DataFrame
    all_tickers = pd.DataFrame.from_dict(raw_ticker_data)
    # DataFrame to CSV in filesystem
    all_tickers.to_csv('./all_tickers.csv')
    # Print last five rows of DataFrame
    print(all_tickers.tail(10))

# Define the ticker symbol and other details
ticker_symbol = 'BTC'
currency = 'USD'
limit_value = 2000
exchange_name = 'CCCAGG'
data_before_timestamp = datetime(2021, 5, 1, 0, 0)

# For daily data
# cryptocompare.get_historical_price_day(ticker_symbol, currency, limit=limit_value, exchange=exchange_name, toTs=data_before_timestamp)

# For hourly data
# cryptocompare.get_historical_price_hour(ticker_symbol, currency, limit=limit_value, exchange=exchange_name, toTs=data_before_timestamp)

# For minute data
# cryptocompare.get_historical_price_minute(ticker_symbol, currency, limit=limit_value, exchange=exchange_name, toTs=data_before_timestamp)

# Fetch the raw price data
raw_price_data = \
    cryptocompare.get_historical_price_hour(
        ticker_symbol,
        currency,
        limit=limit_value,
        exchange=exchange_name,
        toTs=data_before_timestamp
    )

# Convert the raw price data into a DataFrame
hourly_price_data = pd.DataFrame.from_dict(raw_price_data)

# Set the time columns as index and convert it to datetime
hourly_price_data.set_index("time", inplace=True)
hourly_price_data.index = pd.to_datetime(hourly_price_data.index, unit='s')
hourly_price_data['datetimes'] = hourly_price_data.index
hourly_price_data['datetimes'] = hourly_price_data['datetimes'].dt.strftime(
    '%Y-%m-%d')

# Preview the last 5 values of the the first 7 columns of the DataFrame
hourly_price_data.iloc[:, :6].last()

