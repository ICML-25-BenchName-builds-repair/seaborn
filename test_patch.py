import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Store the original date_range function
original_date_range = pd.date_range

# Define our compatibility function
def date_range_compat(start=None, end=None, periods=None, freq=None, **kwargs):
    """
    Compatibility wrapper for pandas.date_range that handles frequency code changes.
    
    In pandas >= 1.1.0, 'ME' is the recommended frequency for month end,
    but in older pandas versions, only 'M' is supported.
    """
    try:
        return original_date_range(start=start, end=end, periods=periods, freq=freq, **kwargs)
    except ValueError as e:
        # If 'ME' frequency fails, try with 'M' instead
        if freq == "ME" and "Invalid frequency: ME" in str(e):
            print(f"Converting 'ME' to 'M' frequency due to error: {e}")
            return original_date_range(start=start, end=end, periods=periods, freq="M", **kwargs)
        # If that's not the issue, re-raise the original error
        raise

# Patch pandas.date_range
pd.date_range = date_range_compat

# Test with ME frequency
try:
    print("Testing with ME frequency:")
    x = pd.date_range("2010-01-01", periods=20, freq="ME")
    print(f"Success! First date: {x[0]}, Last date: {x[-1]}")
except Exception as e:
    print(f"Error with ME frequency: {e}")

# Test with M frequency
try:
    print("\nTesting with M frequency:")
    x = pd.date_range("2010-01-01", periods=20, freq="M")
    print(f"Success! First date: {x[0]}, Last date: {x[-1]}")
except Exception as e:
    print(f"Error with M frequency: {e}")

# Simulate the error case
try:
    print("\nSimulating error case:")
    # Force an error with ME frequency
    original_func = original_date_range
    def mock_date_range(*args, **kwargs):
        if kwargs.get('freq') == 'ME':
            raise ValueError("Invalid frequency: ME")
        return original_func(*args, **kwargs)
    
    # Temporarily replace the original function
    original_date_range_backup = original_date_range
    globals()['original_date_range'] = mock_date_range
    
    # Test with ME frequency again
    x = pd.date_range("2010-01-01", periods=20, freq="ME")
    print(f"Success! First date: {x[0]}, Last date: {x[-1]}")
    
    # Restore the original function
    globals()['original_date_range'] = original_date_range_backup
except Exception as e:
    print(f"Error in simulation: {e}")
    # Restore the original function
    globals()['original_date_range'] = original_date_range_backup