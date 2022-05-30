from collections import namedtuple

DataSource = namedtuple('DataSource', 'name description reference uri date_format')

def describe_data_source(ds: DataSource) -> str:
    return f'{ds.name} ({ds.uri})'