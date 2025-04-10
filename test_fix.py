import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Try to create a date range with different frequencies
print("Testing different date range frequencies:")

frequencies = ["ME", "M", "MS", "BM", "BMS"]
for freq in frequencies:
    try:
        x = pd.date_range("2010-01-01", periods=20, freq=freq)
        print(f"Frequency '{freq}' works: {x[0]} to {x[-1]}")
        
        # Try to create a plot with this frequency
        y = np.arange(20)
        fig, ax = plt.subplots()
        sns.barplot(x=x, y=y, ax=ax)
        plt.close(fig)
        print(f"  Plot with frequency '{freq}' works")
    except Exception as e:
        print(f"Frequency '{freq}' error: {e}")