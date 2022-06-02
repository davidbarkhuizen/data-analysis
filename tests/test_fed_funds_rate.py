
import unittest
from logic.etl import fetch_csv_data
from analyses.fed_funds_rate import source
from logic.model import describe_data_source
from logic.plot import plot

class FedFundsRateTests(unittest.TestCase):

    def test_xxx(self):

        print(describe_data_source(source))

        data = fetch_csv_data(source)
        sorted_data = sorted(data, key=lambda x: x[0])
        
        print(f'{len(data)} data points')

        t = [x[0] for x in sorted_data]
        y = [x[1] for x in sorted_data]
        
        delta = []
        for i in range(len(t) - 1):
            delta.append(sorted_data[i+1][1] - sorted_data[i][1])

        plot('FED Funds Rate', t, y, delta, 'Date', 'Rate', 'Delta')

if __name__ == '__main__':
    unittest.main()