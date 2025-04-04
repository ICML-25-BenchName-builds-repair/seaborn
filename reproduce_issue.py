import pandas as pd

print(f"Pandas version: {pd.__version__}")

# Try with 'ME' (will fail in pandas 1.2.0)
try:
    print("\nTrying with 'ME':")
    x = pd.date_range("2010-01-01", periods=20, freq="ME")
    print(f"Success! First few dates: {x[:3]}")
except Exception as e:
    print(f"Error: {e}")

# Try with 'M' (should work in all pandas versions)
try:
    print("\nTrying with 'M':")
    x = pd.date_range("2010-01-01", periods=20, freq="M")
    print(f"Success! First few dates: {x[:3]}")
except Exception as e:
    print(f"Error: {e}")