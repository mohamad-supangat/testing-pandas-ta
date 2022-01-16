from unicorn_binance_websocket_api.unicorn_binance_websocket_api_manager import BinanceWebSocketApiManager
from datetime import datetime
import json
import pandas as pd
import pandas_ta as ta


#  we
ws = BinanceWebSocketApiManager(
    exchange="binance.com-futures")

ws.create_stream(['kline_5m'], ['btcusdt'])


# pandas dataframe
df = pd.DataFrame(columns=['datetime', 'close'])

while True:
    stream = ws.pop_stream_data_from_stream_buffer()
    if stream:
        jsonstream = json.loads(stream)
        data = jsonstream.get('data')
        if data:
            k = data['k']

            close_time = datetime.fromtimestamp(
                int(k['T'])/1000).strftime('%Y-%m-%d %H:%M:%S')

            new_data = pd.DataFrame({
                'datetime': [close_time],
                'close': [float(k['c'])]
            })

            df = df.append(new_data)

            df.to_csv('./test.csv')

            print(df)
