from datetime import datetime
from decimal import Decimal
import math
from typing import Tuple
from logic.model import DataSource

# https://docs.python.org/3/library/datetime.html
#
# 2022-05-31 00:00:00
date_format = '%Y-%m-%d %H:%M:%S'

# timeOpen
# timeClose
# timeHigh
# timeLow
# name
# open
# high
# low
# close
# volume
# marketCap
# timestamp

# "2024-10-02T00:00:00.000Z"
# "2024-10-02T23:59:59.999Z"
# "2024-10-02T16:08:00.000Z"
# "2024-10-02T19:47:00.000Z"
# "2781"
# 60836.3246300866
# 62357.6867279553
# 59996.9473420048
# 60632.7862737945
# 40762722397.63
# 1198224649900.69
# "2024-10-02T23:59:59.999Z"

def row_parser(row: Tuple) -> Tuple[datetime, Decimal]:

    date_str, irate_str = row[0], row[1]
    
    datum = datetime.strptime(date_str, date_format)
    usd_price = math.log(Decimal(irate_str))
    
    return (datum, usd_price)

# https://coinmarketcap.com/currencies/bitcoin/historical-data/
# timeOpen;timeClose;timeHigh;timeLow;name;open;high;low;close;volume;marketCap;timestamp

source = DataSource(
    'BTC USD OHLCV Price Data',
    'BTC USD price at close averaged across exchanges',
    'https://coinmarketcap.com/currencies/bitcoin/historical-data/',
    'file://localhost/data/btc-price-usd-ohlcv.csv',
    True,
    ';',
    row_parser
)