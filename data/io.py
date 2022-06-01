import csv
from urllib.parse import urlparse
import logging

from data.model import DataSource

def fetch_csv_data(source: DataSource):
    
    def from_local_file(file_path):
        
        with open(file_path) as source_file:
            reader = iter(csv.reader(source_file, delimiter=source.delimiter))
            
            if source.discard_header:            
                next(reader)

            return [source.row_parser(row) for row in reader]

    locator = urlparse(source.url)
    logging.info(f'fetching data from URL {source.url}')
    
    data = None
    match locator.scheme:
        case 'file':
            data = from_local_file(locator.path)
        case _:
            raise Exception(f'unsupported URL scheme {locator.scheme}')

    return data