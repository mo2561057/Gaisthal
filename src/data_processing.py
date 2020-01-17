"""
This file cotains hte mapping between interface and internal
objects!
"""
import pandas as pd

def process_params_and_options(df, alloc_params, normalize=True):
    df = df.set_index(["Name"], drop = True)
    df = pd.concat([df] + [df.eval(x) for x in alloc_params["covariates"]])
    df = _update_cols(df, alloc_params)

    #Normalize the weights. We have to find average
    #Technically we can limit all to the same dist!
    if normalize:
        for var in alloc_params["categorical"].keys():
            size = len(df[var].unique)
            weight =1/_get_average_dist(len)
            alloc_params["categorical"][var] = weight*sign(alloc_params["categorical"][var])
        for var in alloc_params["grouped"]:
            size = len(df[var].unique)
            weight = 1/_get_average_size(x,len(df),alloc_params["group_size"])
            alloc_params["grouped"][var] = weight * sign(alloc_params["grouped"][var])
    return df, alloc_params

def _get_average_dist(x):
    pass

def _update_cols(df, alloc_params):
    """
    Parse Friend Groups that are specified in the options file!
    :param df:
    :param alloc_params:
    :return:
    """
    for group in alloc_params["Friends"].keys():
        df[group] = df[df.index.isin(alloc_params["Friends"][group])].astype(int)
    return df

def _get_average_size(x,len_tot, group_size):
    pass
