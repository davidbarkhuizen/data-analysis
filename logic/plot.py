from typing import List, Optional
from matplotlib import pyplot

from logic.model import Series

# time series
# value_series
# - values
# - label

def plot_time_series(
        title: str,
        time_series: Series,
        values_serieses: List[Series]
    ):

    figure, axis_1 = pyplot.subplots()

    primary_value_series = values_serieses[0]

    axis_1.plot(time_series.values, primary_value_series.values, color='green', linestyle='solid')
    axis_1.set_xlabel(time_series.label)
    axis_1.set_ylabel(primary_value_series.label, color='green')    

    for value_series in values_serieses[1:]:

        axis_2 = axis_1.twinx()
        axis_2.plot(time_series.values, value_series.values, color='purple', linestyle='solid')

        if value_series.label:
            axis_2.set_ylabel(value_series.label, color='purple')
    
    pyplot.title(title)
    # figure.suptitle(?)
    pyplot.show()