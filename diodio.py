import pandas as pd
import requests
import json

from pyti.smoothed_moving_average import smoothed_moving_average as sma

from plotly.offline import plot
import plotly.graph_objs as go

class TradeModel:

	def __init__(self, symbol):
		self.symbol = symbol
		print(self.getData())
		self.df = self.getData()

	def getData(self):

		# define url
		accessPoint = 'https://api.binance.com'
		endpoint = '/api/v1/klines'
		parameters = '?&symbol=' + self.symbol + '&interval=1h'

		url = accessPoint + endpoint + parameters

		# download data
		data =  requests.get(url)
		dictionary = json.loads(data.text)

		# put i datafrome and clean-up
		df = pd.DataFrame.from_dict(dictionary)
		df = df.drop(range(6,12), axis=1)

		# rename columns
		col_names = ['time', 'open', 'high','low', 'close', 'volume']
		df.columns = col_names

		# string to float
		for col in col_names:
			df[col] = df[col].astype(float)

		# add the moving averages
		df['fast_sma'] = sma(df['close'].tolist(), 10)
		df['slow_sma'] = sma(df['close'].tolist(), 30)

		return df

	def plotData(self):
		df = self.df

		# plot candlestick chart
		candle = go.Candlestick(
			x = df['time'],
			open = df['open'],
			close = df['close'],
			high = df['high'],
			low = df['low'],
			name = "Candlesticks")

		# plot MAs
		fsma = go.scatter(
			x = df['time'],
			y = df['fast_sma'],
			name = "Fast SMA",
			line = dict(color = ('rgba(102, 207, 255, 50)')))

		ssma = go.scatter(
			x = df['time'],
			y = df['slow_sma'],
			name = "Slow SMA",
			line = dict(color = ('rgba(255, 207, 102, 50)')))

		# style and display
		data = [candle, ssma, fsma]

		layout = go.layout(title = self.symbol)
		fig = go.figure(data = data, layout = layout)

		plot(fig, filename = self.symbol)

def main():
	symbol = "BTCUSDT"
	model = TradeModel(symbol)
	model.plotData()

if __name__ == '__main__':
	main()
