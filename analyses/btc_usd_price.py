from datetime import datetime
from decimal import Decimal
import math
from typing import Tuple
from logic.model import DataSource

# https://docs.python.org/3/library/datetime.html
#
# 2022-05-31 00:00:00
date_format = '%Y-%m-%d %H:%M:%S'

def row_parser(row: Tuple) -> Tuple[datetime, Decimal]:

    date_str, irate_str = row[0], row[1]
    
    datum = datetime.strptime(date_str, date_format)
    usd_price = math.log(Decimal(irate_str))
    
    return (datum, usd_price)

source = DataSource(
    'BTC USD Price @ Close',
    'BTC USD price at close averaged across exchanges',
    'https://www.blockchain.com/charts/market-price',
    'file:///home/david/data/btc-market-price.csv',
    True,
    ',',
    row_parser
)