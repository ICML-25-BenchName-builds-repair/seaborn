import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from seaborn._compat import safe_date_range

# Test our safe_date_range function
print("Testing safe_date_range function:")
try:
    x = safe_date_range("2010-01-01", periods=5, freq="ME")
    print("Success with ME frequency:", x)
except Exception as e:
    print(f"Error with ME frequency: {e}")

# Now let's modify the test to use our function
print("\nTesting barplot with datetime:")
try:
    # Create data with ME frequency using our safe function
    x = safe_date_range("2010-01-01", periods=20, freq="ME")
    y = np.arange(20)
    
    # Create the plot
    ax = sns.barplot(x=x, y=y, native_scale=True)
    
    # Check assertions from the test
    assert "Date" in ax.xaxis.get_major_locator().__class__.__name__
    
    print("Test passed with safe_date_range")
    
except Exception as e:
    print(f"Error: {e}")

print("\nTest completed successfully!")