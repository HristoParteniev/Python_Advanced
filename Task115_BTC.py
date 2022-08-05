'''
Program calculating VWAP for BTCUSD from finnhub.io

Author: Hristo Parteniev
'''
from collections import defaultdict
import json
import datetime
import websocket

price_volume_dict = defaultdict(list)
volume_dict = defaultdict(list)
time_dict = {}
minute = None
vwap = 0.0

def add_values_to_dicts(row):
    global minute, vwap, price_volume_dict, volume_dict, time_dict

    price_volume_dict[minute].append(row['v'] * row['p'])
    volume_dict[minute].append(row['v'])
    vwap = round(sum(price_volume_dict[minute]) / sum(volume_dict[minute]), 2)
    time_dict[minute] = vwap

def sliced_message(message):
    # The function will slice stream message into more eye-candy looks
    global minute, vwap

    my_dict = json.loads(message)['data']
    for row in my_dict:
        print("-" *60)
        timestamp = datetime.datetime.fromtimestamp((row['t'])/1000.0).strftime('%Y-%m-%d %H:%M:%S')
        # Splitting unix time into minutes
        minute = row['t'] // 60000

        #     printing timestamp, price, volume
        print(f"{timestamp}, price:{row['p']}, volume:{row['v']}")

        if minute in time_dict:
            add_values_to_dicts(row)
        else:
            #VWAP is printed after 1 min period is elapsed
            print(f"VWAP for previous minute: {vwap} ")
            add_values_to_dicts(row)


def on_message(ws, message):
    '''overriding the function printing stream data'''
    sliced_message(message)

def on_error(ws, error):
    ''' if error occurs, send error message'''
    print(error)

def on_close(wsapp, close_status_code, close_msg):
    '''when the stream is stopped, send close message'''
    print("### closed ###")

def on_open(ws):
    '''main function handlint the stream info'''
    ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')

if __name__ == "__main__":
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=cb7b3iiad3idq8jc2140",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close,
                            )
    ws.on_open = on_open
    ws.run_forever()
