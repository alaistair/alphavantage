# Alpha Vantage

import json, requests, matplotlib.pyplot as plt
from datetime import datetime

# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&outputsize=full&apikey=demo

url = 'https://www.alphavantage.co/query?'
function = 'TIME_SERIES_DAILY'
symbol = 'MSFT'
outputsize = 'full'
apikey = 'demo'

#urlfull = url + 'function=' + function + '&symbol=' + symbol + '&apikey=' + apikey
urlfull = url + 'function=' + function + '&symbol=' + symbol + '&outputsize=' + outputsize + '&apikey=' + apikey

response = requests.get(urlfull)
response.raise_for_status()
data = json.loads(response.text)

series = data['Time Series (Daily)']

close = {}
for datestring, price in series.items():
    date = datetime.strptime(datestring, '%Y-%m-%d')
    close[date] = float(price['4. close'])

plt.plot(close.keys(), close.values())
plt.show()
