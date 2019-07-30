"""
This file contains the main code. 
"""
import numpy as np 
import pandas as pd 

from gtal_config import ROOT_DIRECTORY
from src.utils import draw_dienst, create_input_dict, update_participants, return_dienst, get_all_days

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
    group_list = programm_object.groups()


    for x in group_list:


    out = dict()
    return out



def main_dienste(participant_list,
                 service_dict,
                 max_number):
    """
    This functio0n creates a full two week
     allocation of service duty.
    :return:
    """
    #TODO: functions or just objects to keep data
    out_keys = get_all_days(service_dict)
    input_dict = create_input_dict(participant_list,
                                   max_number
                                   )

    out = dict()
    for x in out_keys():
        #TODO: sampling with replacement
        dienst = return_dienst(x)
        out[x] = np.random.choice(input_dict[dienst].keys(),
                                  size = service_dict.return_group_size(x))
        input_dict = update_participants(out,
                                         x,
                                         dienst,
                                         input_dict)



    return out

