import seaborn as sns
from seaborn._core.plot import Plot

# This will fail with NameError: name 'get_layout_engine' is not defined
p = Plot().layout(extent=(.1, .2, .6, 1)).plot()