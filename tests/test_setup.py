"""
This file tests whether the general setup works!

"""
import os

import pytest
import numpy as np
import pandas as pd

from test.auxiliary import return_test_args
from src.groups import generate_groups



def test_robustness():
    df, alloc_params = return_test_args()
    out = generate_groups(df,alloc_params)
    return out


