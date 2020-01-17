"""
This file contains functions for the solution of the problem
"""
import pandas as pd
import numpy as np
from functools import partial
from src.utils import HUGE_INT
from src.data_processing import process_params_and_options


def generate_groups(df, alloc_params, simulation_draws):
    """
    This function takes a full job specification and
    aims to find the optimal allocation
    :param df: pd.DataFrame that cotains individuals and their respective
    characteristics
    :param alloc_params: dict that specifies the objective to be reached
    :param simulation_draws: int indicating the number of times we check another spec
    :return:
        optimal_value: float containng the best value of the objective
        optimal_specification: list containing pd.indices of optimal groups
    """
    func_eval = create_func(df, alloc_params)

    #TODO: Check all potential use cases for this function
    df = process_params_and_options(df,alloc_params)
    group_size = alloc_params["group_size"]

    optimal_value = HUGE_INT
    optimal_specification = []

    for x in range(simulation_draws):
        # Shuffle rows
        index = [
            df.sample(frac=1).index[x::group_size]
            for x in np.arange(0, len(df), group_size)
        ]
        rslt = func_eval(index)
        if rslt < optimal_value:
            optimal_value = rslt
            optimal_allocation = index
    return optimal_value, optimal_specification


def create_func(df, alloc_params):
    """
    Takes the specifications and creates an objective function.
    """
    value_list = [
        df[x].value_counts() / (len(df) / len(alloc_params["group_size"]))
        for x in alloc_params["categorical"]
    ]
    # We need new variables to our dataframe


    return partial(_objective, df, alloc_params, value_list)


def _objective(df, alloc_params, value_list, group_list):
    """
    This function aps a specific group into a total utility level!
    Args:
        df: pd.DataFrame with all information
        alloc_params: dict with matching specs
        subgroup: list with subgroup to be evaluated
    Returns:
        rslt: float indicating the objective value of the function.
    """
    rslt = 0
    for group in group_list:
        for var in alloc_params["categorical"]:
            dist = df.loc[group, var].value_counts()
            dist_mean = value_list[var]
            dist = dist.reindex(dist_mean).replace({np.nan: 0})
            rslt += (
                np.linalg.norm(dist.to_numpy() - dist_mean.to_numpy())
                * alloc_params["categorical"][var]
            )
        for var in alloc_params["grouped"]:
            sum = (df.loc[group, var].sum() - 1) * alloc_params["grouped"][var]
            rslt += sum
    return rslt
