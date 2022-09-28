# REST APIs
# REpresentational State Transfer APIs
# Client -> endpoint -> Web Service
# request | response

import pandas as pd
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)
bitcoin_price_data = bitcoin_data['prices']

data = pd.DataFrame(bitcoin_price_data, columns=['TimeStamp', 'Price'])
data['date'] = pd.to_datetime(data['TimeStamp'],unit='ms')
print(data)

