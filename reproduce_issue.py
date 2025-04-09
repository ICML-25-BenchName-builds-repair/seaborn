import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from seaborn import lineplot
from seaborn._statistics import WeightedAggregator

# Create a test dataframe with a case where weights sum to zero
df = pd.DataFrame({
    "x": [0, 0, 0],  # All weights are zero for this group
    "y": [1, 2, 3],
    "a": ["b", "b", "b"]
})

# Try to create a lineplot with weights
try:
    ax = lineplot(df, x="a", y="y", weights="x")
    print("Test passed - no error")
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")

# Test the WeightedAggregator directly
print("\nTesting WeightedAggregator directly:")
df_with_weight = pd.DataFrame({
    "weight": [0, 0, 0],  # All weights are zero
    "y": [1, 2, 3]
})
agg = WeightedAggregator(estimator="mean")
try:
    result = agg(df_with_weight, "y")
    print(f"Result: {result}")
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")