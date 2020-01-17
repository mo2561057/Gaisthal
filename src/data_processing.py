"""
This file cotains hte mapping between interface and internal
objects!
"""
import pandas as pd


def process_params_and_options(df, options):
    df = df.set_index(["Name"], drop = True)
    return df
