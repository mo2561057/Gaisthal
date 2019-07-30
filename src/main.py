"""
This file contains the main code. 
"""
import numpy as np 
import pandas as pd 

from gtal_config import ROOT_DIRECTORY

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
                 service_object):
    """
    This functio0n creates a full two week
     allocation of service duty.
    :return:
    """
    service_object

    pass