from catchment.models import Site
import pandas as pd
import datetime

FP23 = Site('FP23')

print(FP23)

riverlevel_data = pd.Series(
    [34.0,32.0,33.0,31.0],
    index=[
        datetime.date(2000,1,1),
        datetime.date(2000,1,2),
        datetime.date(2000,1,3),
        datetime.date(2000,1,4),
        ]
    )

FP23.add_measurement('River Level',riverlevel_data,'mm')

print(FP23.measurements['River Level'].series)

PL12 = Location('PL12')
print(PL12)

PL12.add_measurement('River Level',riverlevel_data,'mm')