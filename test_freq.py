import pandas as pd
import sys

print(f"Python version: {sys.version}")
print(f"Pandas version: {pd.__version__}")

# Try different frequencies
frequencies = ["ME", "M", "MS"]

for freq in frequencies:
    try:
        dates = pd.date_range("2010-01-01", periods=20, freq=freq)
        print(f"Frequency '{freq}' works: {dates[0]} to {dates[-1]}")
    except Exception as e:
        print(f"Frequency '{freq}' error: {e}")