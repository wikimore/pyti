from pyti import catch_errors

import pandas as pd


def smoothed_moving_average(data, period):
    """
    Smoothed Moving Average.

    Formula:
    smma = avg(data(n)) - avg(data(n)/n) + data(t)/n
    """
    catch_errors.check_for_period_error(data, period)
    series = pd.Series(data)
    return series.ewm(alpha=1.0 / period).mean().values.flatten()
