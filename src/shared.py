"""
This file contains auxiliary functions
"""
import os

import numpy as np
import pandas as pd

HUGE_INT = 10e5
def update_participants(out,
                        x,
                        dienst,
                        participant_dict
                        ):
    """

    :return:
    """
    for y in out[x]:
        if participant_dict[dienst][y] == 0:
            #TODO: drop keys from dict
            participant_dict[dienst] = participant_dict[dienst]
        else:
            participant_dict[dienst][x] = participant_dict[dienst][x]-1
    return participant_dict


def create_input_dict(service_dict):
    """
    :param service_dict:
    :return:
    """
    out = dict()
    for x in service_dict["dienste"]:
        for y in service_dict["names"]:
            out[x][y] = service_dict["number_dienste"]
    return out

def return_dienst(x,service_dict):
    for y in service_dict["dienste"]:
        if y in x:
            return y


def get_all_days(service_dict):
    dienste = service_dict["dienste"]
    days = [str(x) for x in list(range(service_dict["number_days"]))]
    out = list()
    for x in dienste:
        for y in days:
            out.append("{]_{}".format(x,y))
    return out

def group_size_dict(num_groups, num_participants):
    x = np.floor(num_participants/num_groups)
    z = x.sum()
    #TODO: seems to be ad hoc maybe better way to do that
    while z <= (x+1)*num_groups:
        z = z+1
    return z
