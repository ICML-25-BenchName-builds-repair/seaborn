# Patch pandas.date_range to handle "ME" frequency in older pandas versions
import pandas as pd
import sys

# Store the original date_range function
_original_date_range = pd.date_range

def _date_range_compat(start=None, end=None, periods=None, freq=None, **kwargs):
    """
    Compatibility wrapper for pandas.date_range that handles frequency code changes.
    
    In pandas >= 1.1.0, 'ME' is the recommended frequency for month end,
    but in older pandas versions, only 'M' is supported.
    """
    try:
        return _original_date_range(start=start, end=end, periods=periods, freq=freq, **kwargs)
    except ValueError as e:
        # If 'ME' frequency fails, try with 'M' instead
        if freq == "ME" and "Invalid frequency: ME" in str(e):
            return _original_date_range(start=start, end=end, periods=periods, freq="M", **kwargs)
        # If that's not the issue, re-raise the original error
        raise

# Apply the patch
pd.date_range = _date_range_compat