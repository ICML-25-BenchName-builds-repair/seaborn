import pandas as pd

print(f"Pandas version: {pd.__version__}")

print("\nTesting with 'ME':")
try:
    x = pd.date_range("2010-01-01", periods=20, freq="ME")
    print(f"Success! First few dates: {x[:3]}")
except Exception as e:
    print(f"Error: {e}")

print("\nTesting with 'M':")
try:
    x = pd.date_range("2010-01-01", periods=20, freq="M")
    print(f"Success! First few dates: {x[:3]}")
except Exception as e:
    print(f"Error: {e}")