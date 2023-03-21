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
cryptocompare.cryptocompare._set_api_key_parameter(cryptocompare_API_key)

print("API Key set!")