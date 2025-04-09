import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# This reproduces the failing test in TestBarPlot.test_datetime_native_scale_axis
try:
    # Create data with ME frequency (which fails in older pandas versions)
    x = pd.date_range("2010-01-01", periods=20, freq="ME")
    y = np.arange(20)
    
    # Create the plot
    ax = sns.barplot(x=x, y=y, native_scale=True)
    
    # Check assertions from the test
    assert "Date" in ax.xaxis.get_major_locator().__class__.__name__
    
    print("Test passed with ME frequency")
    
except Exception as e:
    print(f"Error with ME frequency: {e}")
    
    # Try with M frequency instead (which should work in older pandas)
    try:
        x = pd.date_range("2010-01-01", periods=20, freq="M")
        y = np.arange(20)
        
        # Create the plot
        ax = sns.barplot(x=x, y=y, native_scale=True)
        
        # Check assertions from the test
        assert "Date" in ax.xaxis.get_major_locator().__class__.__name__
        
        print("Test passed with M frequency")
        
    except Exception as e:
        print(f"Error with M frequency: {e}")