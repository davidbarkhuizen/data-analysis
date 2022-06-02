
import unittest
from logic.etl import fetch_csv_data
from analyses.fed_funds_rate import source
from logic.model import describe_data_source

class FedFundsRateTests(unittest.TestCase):

    def test_xxx(self):

        print(describe_data_source(source))

        data = fetch_csv_data(source)
        sorted_data = sorted(data, key=lambda x: x[0])
        
        print(f'{len(data)} data points')
        print(sorted_data[0])
        print(sorted_data[-1])

if __name__ == '__main__':
    unittest.main()