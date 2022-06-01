from datetime import datetime
from decimal import Decimal
from data.model import DataSource

date_format = '%Y-%m-%d'

def row_parser(row):

    date_str, irate_str = row[0], row[1]
    
    datum = datetime.strptime(date_str, date_format)
    irate = Decimal(irate_str)  
    
    return (datum, irate)

source = DataSource(
    'Fed Funds Rate',
    'effective fed funds rate',
    'st louis fed https://fred.stlouisfed.org/series/FEDFUNDS',
    'file:///home/david/data/fed-funds-rate.csv',
    True,
    ',',
    lambda row: row_parser(row)    
)