import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn._statistics import WeightedAggregator

# Create a test dataframe with a case where weights sum to zero for one category
df = pd.DataFrame({
    "a": ["b", "b", "c", "c"],  # Category
    "y": [0.5, 0.6, 0.7, 0.8],  # Values
    "x": [1, 2, 0, 0]           # Weights that sum to zero for category "c"
})

print("DataFrame:")
print(df)

# Test the WeightedAggregator directly
print("\nTesting WeightedAggregator directly:")
aggregator = WeightedAggregator("mean")

# Test with category "b" (non-zero weights)
b_data = df[df["a"] == "b"].copy()
b_data["weight"] = b_data["x"]  # WeightedAggregator expects a column named "weight"
b_result = aggregator(b_data, "y")
print(f"Category 'b' weighted average: {b_result}")

# Test with category "c" (zero weights)
c_data = df[df["a"] == "c"].copy()
c_data["weight"] = c_data["x"]  # WeightedAggregator expects a column named "weight"
c_result = aggregator(c_data, "y")
print(f"Category 'c' weighted average: {c_result}")

# Test the lineplot function
print("\nTesting lineplot function:")
try:
    ax = sns.lineplot(df, x="a", y="y", weights="x")
    plt.close()
    
    # Extract the values from the plot
    vals = ax.lines[0].get_ydata()
    labels = [label.get_text() for label in ax.get_xticklabels()]
    
    print("Plot values:")
    for i, label in enumerate(labels):
        print(f"Category '{label}': {vals[i]}")
    
    print("\nNo ZeroDivisionError was raised in the lineplot function")
except ZeroDivisionError:
    print("\nZeroDivisionError was raised in the lineplot function")

# Test np.average directly to show the original issue
print("\nTesting np.average directly:")
for category in df["a"].unique():
    pos_df = df.loc[df["a"] == category]
    print(f"\nCategory: {category}")
    print(f"Values: {pos_df['y'].values}")
    print(f"Weights: {pos_df['x'].values}")
    print(f"Sum of weights: {pos_df['x'].sum()}")
    
    try:
        avg = np.average(pos_df["y"], weights=pos_df["x"])
        print(f"Weighted average: {avg}")
    except ZeroDivisionError:
        print("ZeroDivisionError occurred")