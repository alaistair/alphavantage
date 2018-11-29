# Alpha Vantage

import json, requests, csv, collections
import pygal
from pygal import Config
from pygal.style import Style
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
    outputWriter.writerow([date, close[date]])

ordered_close = collections.OrderedDict(sorted(close.items()))

# Graph config
config = Config()

# Graph style
custom_style = Style(
  font_family = 'Arial',
  label_font_size = 14
  )

# Graph data
graph = pygal.Line(config, style = custom_style, show_legend = False)
graph.title = 'Share Prices'
graph.x_labels = ordered_close.keys()
#graph.x_labels_major = 
graph.add(symbol, ordered_close.values(), show_dots = False)
graph.render_to_file(symbol + '.svg')

print('finished')
