"""
This file contains auxiliary functions
"""
import os

import numpy as np
import pandas as pd

from gtal_config import ROOT_DIRECTORY

def update_participants(out,
                        x,
                        dienst
                        participant_dict
                        ):
    """

    :return:
    """
    for y in out[x]:
        if participant_dict[y] == 0:
            #TODO: drop keys from dict
            participant_dict = participant_dict
        else:
            participant_dict[x] = participant_dict[x]-1
    return participant_dict


    pass

def create_input_dict():
    pass
def draw_dienst():
    """

    :return:
    """
    pass


def return_dienst():
    pass


def get_all_days():
    pass
