# Alpha Vantage

import json, requests, matplotlib.pyplot as plt, csv
from datetime import datetime

# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&outputsize=full&apikey=demo

url = 'https://www.alphavantage.co/query?'
function = 'TIME_SERIES_DAILY'
exchange = 'ASX'
symbol = 'APT'
outputsize = 'full'
apikey = '9S5XM342IGZHSVD0'

#urlfull = url + 'function=' + function + '&symbol=' + symbol + '&apikey=' + apikey
urlfull = url + 'function=' + function + '&symbol=' + exchange + ':' + symbol + '&outputsize=' + outputsize + '&apikey=' + apikey

response = requests.get(urlfull)
response.raise_for_status()
data = response.json()

series = data['Time Series (Daily)']
outputFile = open(symbol + '.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

close = {}
for datestring, price in series.items():
    date = datetime.strptime(datestring, '%Y-%m-%d')
    close[date] = float(price['4. close'])
    outputWriter.writerow([date, float(price['4. close'])])

plt.plot(close.keys(), close.values())
plt.show() # Atom
plt.savefig(symbol + '.png') # Repl.it
