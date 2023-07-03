from catchment.models import Site
import pandas as pd
import datetime

PL23 = Site('PL23')

riverlevel_data = pd.Series(
    [34.0,32.0,33.0,31.0],
    index=[
        datetime.date(2000,1,1),
        datetime.date(2000,1,2),
        datetime.date(2000,1,3),
        datetime.date(2000,1,4),
        ]
    )

waterph_data = pd.Series(
    [7.8,8.0,7.9],
    index=[
        datetime.date(2000,1,1),
        datetime.date(2000,1,2),
        datetime.date(2000,1,3)
        ]
    )

PL23.add_measurement('River Level', riverlevel_data, 'mm')
PL23.add_measurement('Water pH', waterph_data)


print(PL23.measurements['River Level'])
print(PL23.measurements['Water pH'])

lastdata = PL23.last_measurements
print(lastdata)