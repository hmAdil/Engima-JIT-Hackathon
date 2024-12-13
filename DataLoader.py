import os
import json
import pandas as pd
import urllib.request

# Defining Alpha Vantage API Key
API_KEY = "26KZDRIYWGLXL28H"

# Stock Name
STOCK_NAME = "AAl"

# Preparing to download the data using API
data_url = (
    "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=%s&interval=5min&apikey=%s"
    % (STOCK_NAME, API_KEY)
)
file_to_save = "Daily_Adjusted_Market_Data_%s.csv" % STOCK_NAME

# Checking if we have the dataset loaded
if os.path.exists(file_to_save):
    print("Dataset Exists Already!")
    data = pd.read_csv(file_to_save)

else:
    # Opening the Request URL
    with urllib.request.urlopen(data_url) as url:
        data = json.loads(url.read().decode())
        print(data)
