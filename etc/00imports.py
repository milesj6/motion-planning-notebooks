from typing import NamedTuple, List, Dict, Tuple, Any, Callable, Iterable, Iterator, Optional

import time
from enum import Enum
import math
from math import sin, cos, sqrt, exp
import json
from datetime import timedelta
from datetime import date
from itertools import repeat, accumulate, chain, filterfalse, groupby, takewhile
from functools import reduce, partial
from operator import mul
from bokeh.plotting import figure, show, output_notebook
from bokeh.models import Range1d, Label
from random import uniform, expovariate, choice

from collections import deque
from bisect import bisect_left

import numpy as np
from numpy import mean, var, diff
from scipy.interpolate import splev, splrep
from scipy.stats import norm
