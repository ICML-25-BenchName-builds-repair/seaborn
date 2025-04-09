import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from seaborn import lineplot

# Create a test dataframe similar to the one in the failing test
# The key is to have a group where all weights are zero
df = pd.DataFrame({
    "x": [0, 0, 0, 12, 15],  # First group has all zero weights
    "y": [1, 2, 3, 0.449243, 0.073484],
    "a": ["a", "a", "a", "b", "c"]
})

# Try to create a lineplot with weights
try:
    ax = lineplot(df, x="a", y="y", weights="x")
    print("Test passed - no error")
    
    # Check the values
    vals = ax.lines[0].get_ydata()
    print("Y values in the plot:", vals)
    
    # Verify the values match what we expect
    for i, label in enumerate(ax.get_xticklabels()):
        pos_df = df.loc[df["a"] == label.get_text()]
        try:
            expected = np.average(pos_df["y"], weights=pos_df["x"])
            print(f"Group {label.get_text()}: expected={expected}, actual={vals[i]}")
            assert np.isclose(vals[i], expected) or (np.isnan(vals[i]) and np.isnan(expected))
        except ZeroDivisionError:
            print(f"Group {label.get_text()}: ZeroDivisionError in np.average, plot value={vals[i]}")
            assert np.isnan(vals[i])
    
    plt.savefig("test_lineplot.png")
    print("Plot saved to test_lineplot.png")
    
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")