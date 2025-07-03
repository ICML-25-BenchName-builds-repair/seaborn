import seaborn as sns
from seaborn._core.plot import Plot

# Create a plot with layout extent
p = Plot().layout(extent=(0.1, 0.2, 0.6, 1)).plot()
print("Plot created successfully!")