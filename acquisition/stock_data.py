import pandas as pd
from sys import argv

def get_extended_stock_data(symbol: str, api_key: str, interval: str = '1min', adjusted: bool = True) -> pd.DataFrame:
    df = pd.DataFrame()

    for year in range(1, 3):
        for month in range(1, 13):
            period = 'year{}month{}'.format(year, month)
            url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol={}&interval={}&slice={}&adjusted={}&apikey={}'.format(symbol, interval, period, adjusted, api_key)
            df_period = pd.read_csv(url)
            df = df.append(df_period)

    return df

if len(argv) != 4:
    raise TypeError('Incorrect number of arguments.')

symbol = argv[1]
api_key = argv[2]
file_name = argv[3]
data = get_extended_stock_data(symbol=symbol, api_key=api_key)
data.to_csv(file_name, index=False)