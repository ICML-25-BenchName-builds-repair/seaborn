# Import seaborn objects
from .rcmod import *  # noqa: F401,F403
from .utils import *  # noqa: F401,F403
from .palettes import *  # noqa: F401,F403
from .relational import *  # noqa: F401,F403
from .regression import *  # noqa: F401,F403
from .categorical import *  # noqa: F401,F403
from .distributions import *  # noqa: F401,F403
from .matrix import *  # noqa: F401,F403
from .miscplot import *  # noqa: F401,F403
from .axisgrid import *  # noqa: F401,F403
from .widgets import *  # noqa: F401,F403
from .colors import xkcd_rgb, crayons  # noqa: F401
from . import cm  # noqa: F401

# Import compatibility functions
from ._compat import safe_date_range  # noqa: F401

# Capture the original matplotlib rcParams
import matplotlib as mpl
_orig_rc_params = mpl.rcParams.copy()

# Define the seaborn version
__version__ = "0.14.0.dev0"

# Monkey patch pandas.date_range to handle 'ME' frequency in older pandas versions
import pandas as pd

# The original date_range is already stored in _compat.py
def _patched_date_range(*args, **kwargs):
    """
    Patched version of pandas.date_range that handles 'ME' frequency in older pandas versions.
    """
    return safe_date_range(*args, **kwargs)

pd.date_range = _patched_date_range
