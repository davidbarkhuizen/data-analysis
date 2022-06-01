from collections import namedtuple

DataSource = namedtuple('DataSource', [
        'name', 
        'description', 
        'reference', 
        'url', 
        'discard_header', 
        'delimiter',
        'row_parser']
    )

def describe_data_source(ds: DataSource) -> str:
    return f'{ds.name} ({ds.url})'