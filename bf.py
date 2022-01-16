from kucoin.client import Market
import config


# grouping candles
def convert_candles(candles):
    open = []
    high = []
    low = []
    close = []
    volume = []

    for candle in candles:
        open.append(float(candle[1]))
        close.append(float(candle[2]))
        high.append(float(candle[3]))
        low.append(float(candle[4]))
        volume.append(float(candle[5]))

    return {
        'open': open,
        'high': high,
        'low': low,
        'close': close,
        'volume': volume
    }
