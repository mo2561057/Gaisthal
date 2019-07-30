"""This module provides some configuration for the package."""
import sys
from pathlib import Path

import numpy as np

# We only support modern Python.
np.testing.assert_equal(sys.version_info[:2] >= (3, 6), True)

# We rely on relative paths throughout the package.
PACKAGE_DIR = Path(__file__).parent.absolute()
TEST_RESOURCES_DIR = PACKAGE_DIR / "tests"

# Hard coded values
HUGE_INT = 1e20
HUGE_FLOAT = 1.0e20
MISSING_FLOAT = -99.00
MISSING_INT = -99
LARGE_FLOAT = 1.0e8
