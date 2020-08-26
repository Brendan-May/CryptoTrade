import pandas as pd
import requests
import json

from binance.client import Client 

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

		# put i dataframe and clean-up
		df = pd.DataFrame.from_dict(dictionary)
		df = df.drop(range(6,12), axis=1)

		# rename columns
		col_names = ['time', 'open', 'high','low', 'close', 'volume']
		df.columns = col_names

		# string to float
		for col in col_names:
			df[col] = df[col].astype(float)
			
		return df

def main():
	symbol = "BTCUSDT"
	model = TradeModel(symbol)

if __name__ == '__main__':
	main()
