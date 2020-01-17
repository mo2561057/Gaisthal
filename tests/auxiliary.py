"""
This file returns test args
"""
import numpy as np
import pandas as pd

def return_test_args(constr=None):
    """
    This function returns a test  case
    """
    #TODO: Move Hardcoded numbers to config file
    n_agents = np.random.randint(20,500)
    alloc_params = {}

    if "num_cols" in constr.keys():
        num_cols = constr["num_cols"]
    else:
        num_cols = np.random.randint(5)

    cols = ["name"]+[f"feature_{x}" for x in range(num_cols)]
    df = pd.DataFrame(columns=cols,index=range(n_agents))
    cols["name"] = df.index.astype(str)

    for col in cols:
        num_values = np.random.randint(2,5)
        df[col] = np.random.randint(range(num_values), size=n_agents)

    alloc_params["group_size"] = np.random.randint(2,n_agents/4)

    if constr is None:
        alloc_params["categorical"] = {x:np.random.choice([-1,1]) for x in cols[:-1]}
        alloc_params["grouped"] = {cols[-1]:np.random.choice([-1,1])}
    else:
        alloc_params.update(constr)

    return df, alloc_params



