import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print(f"Pandas version: {pd.__version__}")

# Try to create a date range with "ME" frequency
try:
    x = pd.date_range("2010-01-01", periods=20, freq="ME")
    print(f"ME frequency works: {x[0]} to {x[-1]}")
    
    # Try to create a plot with this frequency
    y = np.arange(20)
    fig, ax = plt.subplots()
    sns.barplot(x=x, y=y, native_scale=True, ax=ax)
    plt.close(fig)
    print("Plot with ME frequency works")
except Exception as e:
    print(f"Error with ME frequency: {e}")

# Try with "M" frequency instead
try:
    x = pd.date_range("2010-01-01", periods=20, freq="M")
    print(f"M frequency works: {x[0]} to {x[-1]}")
    
    # Try to create a plot with this frequency
    y = np.arange(20)
    fig, ax = plt.subplots()
    sns.barplot(x=x, y=y, native_scale=True, ax=ax)
    plt.close(fig)
    print("Plot with M frequency works")
except Exception as e:
    print(f"Error with M frequency: {e}")