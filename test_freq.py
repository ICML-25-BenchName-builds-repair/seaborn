import pandas as pd

# Try different frequencies
try:
    x = pd.date_range("2010-01-01", periods=5, freq="ME")
    print("ME frequency valid:", x)
except Exception as e:
    print(f"Error with ME frequency: {e}")

try:
    x = pd.date_range("2010-01-01", periods=5, freq="MS")
    print("MS frequency valid:", x)
except Exception as e:
    print(f"Error with MS frequency: {e}")

try:
    x = pd.date_range("2010-01-01", periods=5, freq="M")
    print("M frequency valid:", x)
except Exception as e:
    print(f"Error with M frequency: {e}")