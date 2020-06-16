import numpy as np
import os
import sys

from driver import load_challenge_data, get_classes

def data_files_list(input_directory):
    """Get a list of files in the input directory"""
    # input_directory - path of input data
    # Example
    # input_files = data_files_list(input_directory)
    # input_files - list of files in input_directory with extension '.mat'

    input_files = []
    for f in os.listdir(input_directory):
        if os.path.isfile(os.path.join(input_directory, f)) and not f.lower().startswith('.') and f.lower().endswith('mat'):
            input_files.append(f)

    return input_files



def data_files_load(input_directory,input_files = '',mapping_labels = False):
    """Load data files as list along with the labels from the given data directory"""
    # input_directory - path of input data
    # input_files - list of files
    # mapping_labels - True (map labels e.g. AF to string numbers)
    # Example
    # [list_data,list_label] = data_files_load(pth_data)
    # list_data - list comprising data (list_data[0][1,:] --> To access first sample and 2nd channel ECG data )
    # list_label = list comprising labesl (list_label[0] --> To access label of first sample)

    if(len(input_files) == 0):
        input_files = data_files_list(input_directory)

    # converting list of files to absolute path
    string_pth = input_directory+os.path.sep
    input_files_pth = [string_pth+s for s in input_files]

    del input_files
    
    list_data = []
    list_header = []
    list_label = []

    for ii in range(len(input_files_pth)):

        tmp_input_file = input_files_pth[ii]
        data, header_data = load_challenge_data(tmp_input_file)

        #------------------------------------------------------------
        # Extracting label from header data
        #--------------------------------------------------------------
        for iline in header_data:
            if iline.startswith('#Age'):
                tmp_age = iline.split(': ')[1].strip()
                age = int(tmp_age if tmp_age != 'NaN' else 57)
            elif iline.startswith('#Sex'):
                tmp_sex = iline.split(': ')[1]
                if tmp_sex.strip()=='Female':
                    sex =1
                else:
                    sex=0
            elif iline.startswith('#Dx'):
                label = iline.split(': ')[1].split(',')[0]


        #print('Label: ',label)

        if(mapping_labels):
            mapping =  {'Normal': '1', 'AF': '2', 'I-AVB': '3', 'LBBB':'4', 'RBBB':'5', 'PAC':'6', 'PVC' :'7', 'STD':'8', 'STE': '9'}
            for key, value in mapping.items():
                label = label.replace(key, value)

        list_data.append(data)
        list_header.append(header_data)
        list_label.append(label)

    return list_data,list_header,list_label
