from unicorn_binance_websocket_api.unicorn_binance_websocket_api_manager import BinanceWebSocketApiManager
import json

binance_websocket_api_manager = BinanceWebSocketApiManager(
    exchange="binance.com-futures")

binance_websocket_api_manager.create_stream(['kline_5m'], ['btcusdt'])

while True:
    stream = binance_websocket_api_manager.pop_stream_data_from_stream_buffer()
    if stream:
        jsonstream = json.loads(stream)
        data = jsonstream.get('data')
        if data:
            print(data)
