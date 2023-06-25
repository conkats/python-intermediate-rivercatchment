"""Tests for statistics functions within the Model layer."""

import pandas as pd
import pandas.testing as pdt
import datetime
import pytest
import numpy.testing as npt
import numpy as np

'''Adding parameterising for our unit tests
using decorators for scaling up unit testing'''
#for test_daily_mean_integers()

@pytest.mark.parametrize(
    "test_data, test_index, test_columns, expected_data,\
      expected_index, expected_columns",
    [
        (
            [ [0.0, 0.0], [0.0, 0.0], [0.0, 0.0] ],
            [ [0.0, 0.0], [0.0, 0.0], [0.0, 0.0] ], #2x2
            [ pd.to_datetime('2000-01-01 01:00'),
                pd.to_datetime('2000-01-01 02:00'),
                pd.to_datetime('2000-01-01 03:00') ],
            [ 'A', 'B' ],
            [ [0.0, 0.0] ],
            [ [0.0, 0.0] ],#2x1
            [ datetime.date(2000, 1, 1) ],
            [ 'A', 'B' ]
        ),
        (
            [ [1, 2], [3, 4], [5, 6] ],
            [ pd.to_datetime('2000-01-01 01:00'),
                pd.to_datetime('2000-01-01 02:00'),
                pd.to_datetime('2000-01-01 03:00') ],
            [ 'A', 'B' ],
            [ [3.0, 4.0] ],
            [ datetime.date(2000, 1, 1) ],
            [ 'A', 'B' ]
        ),
    ])

def test_daily_mean(test_data, test_index, test_columns, expected_data, 
                    expected_index, expected_columns):
    """Test mean function works for array of zeroes and positive integers."""
    from catchment.models import daily_mean
    pdt.assert_frame_equal(daily_mean(pd.DataFrame(data=test_data, 
                                                   index=test_index, columns=test_columns)),
                           pd.DataFrame(data=expected_data, 
                                        index=expected_index, columns=expected_columns))

@pytest.mark.parametrize(
    "test_data, test_index, test_columns, expected_data, expected_index,\
    expected_columns",
    [
        (
            [ [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0] ],
            [ pd.to_datetime('2000-01-01 01:00'),
                pd.to_datetime('2000-01-01 02:00'),
                pd.to_datetime('2000-01-01 03:00') ],
            [ 'A', 'B', 'C' ],
            [ [0.0, 0.0, 0.0] ],
            [ datetime.date(2000, 1, 1) ],
            [ 'A', 'B', 'C' ]
        ),
        (
            [ [4, 2, 5], [1, 6, 2], [4, 1, 9] ],
            [ pd.to_datetime('2000-01-01 01:00'),
                pd.to_datetime('2000-01-01 02:00'),
                pd.to_datetime('2000-01-01 03:00') ],
            [ 'A', 'B', 'C' ],
            [ [4, 6, 9] ],
            [ datetime.date(2000, 1, 1) ],
            [ 'A', 'B', 'C' ]
        ),
        (
            [ [4, -2, 5], [1, -6, 2], [-4, -1, 9] ],
            [ pd.to_datetime('2000-01-01 01:00'),
                 pd.to_datetime('2000-01-01 02:00'),
                 pd.to_datetime('2000-01-01 03:00') ],
            [ 'A', 'B', 'C' ],
            [ [4, -1, 9] ],
            [ datetime.date(2000, 1, 1) ],
            [ 'A', 'B', 'C' ]
        ),
    ])
def test_daily_max(test_data, test_index, test_columns, expected_data, 
                    expected_index, expected_columns):
    """Test max function works for array of zeroes and positive integers."""
    from catchment.models import daily_max
    pdt.assert_frame_equal(daily_max(pd.DataFrame(data=test_data, 
                                                  index=test_index, 
                                                  columns=test_columns)),
                           pd.DataFrame(data=expected_data, 
                                        index=expected_index,
                                        columns=expected_columns))
@pytest.mark.parametrize(
    "test_data, test_index, test_columns, expected_data, expected_index,\
     expected_columns",
    [
        (
            [ [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0] ],
            [ pd.to_datetime('2000-01-01 01:00'),
                pd.to_datetime('2000-01-01 02:00'),
                pd.to_datetime('2000-01-01 03:00') ],
            [ 'A', 'B', 'C' ],
            [ [0.0, 0.0, 0.0] ],
            [ datetime.date(2000, 1, 1) ],
            [ 'A', 'B', 'C' ]
        ),
        (
            [ [4, 2, 5], [1, 6, 2], [4, 1, 9] ],
            [ pd.to_datetime('2000-01-01 01:00'),
                pd.to_datetime('2000-01-01 02:00'),
                pd.to_datetime('2000-01-01 03:00') ],
            [ 'A', 'B', 'C' ],
            [ [1, 1, 2] ],
            [ datetime.date(2000, 1, 1) ],
            [ 'A', 'B', 'C' ]
        ),
        (
            [ [4, -2, 5], [1, -6, 2], [-4, -1, 9] ],
            [ pd.to_datetime('2000-01-01 01:00'),
                 pd.to_datetime('2000-01-01 02:00'),
                 pd.to_datetime('2000-01-01 03:00') ],
            [ 'A', 'B', 'C' ],
            [ [-4, -6, 2] ],
            [ datetime.date(2000, 1, 1) ],
            [ 'A', 'B', 'C' ]
        ),
    ])
def test_daily_min(test_data, test_index, test_columns, expected_data, 
                   expected_index, expected_columns):
    """Test min function works for array of zeroes and positive integers."""
    from catchment.models import daily_min
    pdt.assert_frame_equal(daily_min(pd.DataFrame(data=test_data, 
                                                  index=test_index, 
                                                  columns=test_columns)),
                           pd.DataFrame(data=expected_data, 
                                        index=expected_index, 
                                        columns=expected_columns))
@pytest.mark.parametrize(
    "test, expected, expect_raises",
    [
        (
            'hello',
            None,
            TypeError,
        ),
        (
            3,
            None,
            TypeError,
        ),
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[0.33, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]],
            None,
        )
    ])
def test_data_normalise(test, expected, expect_raises):
    """Test normalisation works for arrays of one and positive integers."""
    from catchment.models import data_normalise
    if isinstance(test, list):
        test = np.array(test)
    if expect_raises is not None:
        with pytest.raises(expect_raises):
            npt.assert_almost_equal(data_normalise(test), np.array(expected), decimal=2)
    else:
        npt.assert_almost_equal(data_normalise(test), np.array(expected), decimal=2)