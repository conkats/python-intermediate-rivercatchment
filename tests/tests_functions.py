#!/usr/bin/env python3
""" Writing tests to verity correct behaviour"""

import pandas as pd
import pandas.testing as pdt
from catchment.models import daily_mean
import datetime

test_input = pd.DataFrame(
                data=[[1.0, 2.0],
                      [3.0, 4.0],
                      [5.0, 6.0]],
                index=[pd.to_datetime('2000-01-01 01:00'),
                       pd.to_datetime('2000-01-01 02:00'),
                       pd.to_datetime('2000-01-01 03:00')],
                columns=['A', 'B']
)

test_result = pd.DataFrame(
                 data=[[3.0, 4.0]],
                 index=[datetime.date(2000, 1, 1)],
                 columns=['A', 'B']
)

pdt.assert_frame_equal(daily_mean(test_input), test_result)


"""Keep testing assertion"""
test_input = pd.DataFrame(
                data=[[2.0, 0.0],
                      [4.0, 0.0]],
                index=[pd.to_datetime('2000-01-01 01:00'),
                       pd.to_datetime('2000-01-01 02:00')],
                columns=['A', 'B']
)
test_result = pd.DataFrame(
                 data=[[3.0, 0.0]],
                 index=[datetime.date(2000, 1, 1)],
                 columns=['A', 'B']
)
pdt.assert_frame_equal(daily_mean(test_input), test_result)

test_input = pd.DataFrame(
                data=[[0.0, 0.0],
                      [0.0, 0.0]],
                index=[pd.to_datetime('2000-01-01 01:00'),
                       pd.to_datetime('2000-01-01 02:00')],
                columns=['A', 'B']
)
test_result = pd.DataFrame(
                 data=[[0.0, 0.0]],
                 index=[datetime.date(2000, 1, 1)],
                 columns=['A', 'B']
)
pdt.assert_frame_equal(daily_mean(test_input), test_result)

test_input = pd.DataFrame(
                data=[[1.0, 2.0],
                      [3.0, 4.0],
                      [5.0, 6.0]],
                index=[pd.to_datetime('2000-01-01 01:00'),
                       pd.to_datetime('2000-01-01 02:00'),
                       pd.to_datetime('2000-01-01 03:00')],
                columns=['A', 'B']
)
test_result = pd.DataFrame(
                 data=[[3.0, 4.0]],
                 index=[datetime.date(2000, 1, 1)],
                 columns=['A', 'B']
)
pdt.assert_frame_equal(daily_mean(test_input), test_result)