import unittest

from py import process

from model import DataSetSource
import csv
from urllib.parse import urlparse

source = DataSetSource('fed funds rate', 'federal funds effective rate', 'https://fred.stlouisfed.org/series/FEDFUNDS', 'file:///home/david/data/fed-funds-rate.csv')

class FedFundsRateTests(unittest.TestCase):

    def test_csv_load(self):

        # DATE,FEDFUNDS
        # 1954-07-01,0.80

        uri = urlparse(source.uri)

        print(uri)

        data = []
        def process_data_point(datum):
            (date_str, irate_str) = datum
            print(date_str, irate_str)

        def generator_from_local_file(path):
            source_file_path = uri.path
            print(source_file_path)
            with open(source_file_path) as source_file:
                for row in csv.reader(source_file, delimiter=','):
                    yield (row[0], row[1])
                return 

        data_point_generator = None

        match uri.scheme:
            case 'file':
                data_point_generator = generator_from_local_file(uri.path)
            case _:
                raise Exception(f'unsupported scheme {uri.scheme}')
        
        for data_point in data_point_generator:
            process_data_point(data_point)        

if __name__ == '__main__':
    unittest.main()