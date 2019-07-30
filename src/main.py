"""
This file contains the main code. 
"""
import numpy as np 
import pandas as pd 

from gtal_config import ROOT_DIRECTORY
from src.utils import draw_dienst, create_input_dict, update_participants

def main_function_groups(programm_object,
                  participants):
    """
    programm_object: This object contains all important information about the
    respective programm. It is an instance of the programm class
    participants: This is a list that conatains names of all partivipants
    taking part in the programm

    :return: dictionary that contains groups as keys and list describing groups
    as values

    """
    group_list = prgramm_object.groups()


    for x in group_list:


    out = dict()
    return out



def main_dienste(participant_list,
                 service_object,
                 max_number):
    """
    This functio0n creates a full two week
     allocation of service duty.
    :return:
    """
    out_keys = service_object.create_keys()
    input_dict = create_input_dict(participant_list,
                                   max_number)
    out = dict()
    for x in out_keys():
        #TODO: sampling with replacement
        out[x] = np.random.choice(participant_list,
                               size = service_object.return_group_size(x))
        participant_list = update_participants(out,
                                               x,
                                               participant_list)



    return out

