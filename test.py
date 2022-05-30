import unittest

from model import DataSource, describe_data_source
import csv
from urllib.parse import urlparse
from datetime import datetime
from decimal import Decimal

data_source = DataSource(
        'fed funds rate', 
        'federal funds effective rate', 
        'https://fred.stlouisfed.org/series/FEDFUNDS', 
        'file:///home/david/data/fed-funds-rate.csv',
        '%Y-%m-%d'
    )

class FedFundsRateTests(unittest.TestCase):

    def test_csv_load(self):

        # DATE,FEDFUNDS
        # 1954-07-01,0.80

        uri = urlparse(data_source.uri)

        print(uri)

        def process_data_point(data, datum):
            (date_str, irate_str) = datum
            dt = datetime.strptime(date_str, data_source.date_format)
            data.append((dt, Decimal(irate_str)))
        
        def generator_from_local_file(path):
            source_file_path = uri.path
            print(source_file_path)
            with open(source_file_path) as source_file:
                reader = iter(csv.reader(source_file, delimiter=','))
                next(reader) # discard header
                for row in reader:
                    yield (row[0], row[1])
                return 

        data_point_generator = None

        match uri.scheme:
            case 'file':
                data_point_generator = generator_from_local_file(uri.path)
            case _:
                raise Exception(f'unsupported scheme {uri.scheme}')
        
        data = []
        for data_point in data_point_generator:
            process_data_point(data, data_point)        

        sorted_data = sorted(data, key=lambda x: x[0])

        print(describe_data_source(data_source))
        print(f'{len(data)} data points')
        print(sorted_data[0])
        print(sorted_data[-1])

if __name__ == '__main__':
    unittest.main()