from typing import List, Optional
from matplotlib import pyplot

def plot(
        title: str,
        time: List, 
        values: List, 
        values_secondary: Optional[List], 
        time_label: str, 
        value_label: str,
        values_secondary_label: Optional[str]
    ):

    figure, axis_1 = pyplot.subplots()

    # figure.suptitle(title)
    
    pyplot.title(title)

    axis_1.plot(time, values, color='green', linestyle='solid')
    axis_1.set_xlabel(time_label)
    axis_1.set_ylabel(value_label, color='green')

    if values_secondary:
        
        axis_2 = axis_1.twinx()
        axis_2.plot(time[:-1], values_secondary, color='purple', linestyle='solid')
        axis_2.set_xlabel(time_label)

        if values_secondary_label:
            axis_2.set_ylabel(values_secondary_label, color='purple')
    
    pyplot.show()