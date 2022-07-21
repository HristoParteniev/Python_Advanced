'''imports'''
from collections import defaultdict
import json
import datetime
import websocket

price_volume_dict = defaultdict(list)
volume_dict = defaultdict(list)
time_dict = {}
START_TIME = None
END_TIME = None
VWAP = 0.0

def sliced_message(message):
    '''The function will slice stream message into more eye-candy looks'''
    global START_TIME, END_TIME, VWAP

    my_dict = json.loads(message)['data']
    for row in my_dict:
        print("-" *60 +"\n")
        timestamp = datetime.datetime.fromtimestamp((row['t'])/1000.0).strftime('%Y-%m-%d %H:%M:%S')

        if VWAP == 0.0:
            print(f"{timestamp}, price:{row['p']}, volume:{row['v']}")

        if START_TIME is not None:
            if START_TIME < row['t']/1000.0 < END_TIME:
                price_volume_dict[START_TIME].append(row['v'] * row['p'])
                volume_dict[START_TIME].append(row['v'])
                VWAP = round(sum(price_volume_dict[START_TIME]) / sum(volume_dict[START_TIME]), 2)
                time_dict[START_TIME] = VWAP

            elif ((START_TIME - 60) < row['t']/1000.0 < START_TIME) \
                and price_volume_dict.keys(len)>1:
                price_volume_dict[-2].append(row['v'] * row['p'])
                volume_dict[-2].append(row['v'])
                VWAP = round(sum(price_volume_dict[-2]) / sum(volume_dict[-2]), 2)
                time_dict[-2] = VWAP
            elif row['t']/1000.0 > END_TIME:
                START_TIME = row['t']/1000.0
                END_TIME = START_TIME + 60
                price_volume_dict[START_TIME].append(row['v'] * row['p'])
                volume_dict[START_TIME].append(row['v'])
                VWAP = round(sum(price_volume_dict[START_TIME]) / sum(volume_dict[START_TIME]), 2)
                time_dict[START_TIME] = VWAP

        else:
            START_TIME = row['t']/1000.0
            END_TIME = START_TIME + 60
            price_volume_dict[START_TIME].append(row['v'] * row['p'])
            volume_dict[START_TIME].append(row['v'])
            VWAP = round(sum(price_volume_dict[START_TIME]) / sum(volume_dict[START_TIME]), 2)
            time_dict[START_TIME] = VWAP
        print(f"{timestamp}, price:{row['p']}, volume:{row['v']}, VWAP:{VWAP}")

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
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=cb7b3iiad3idq8jc2140",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close,
                            )
    ws.on_open = on_open
    ws.run_forever()
