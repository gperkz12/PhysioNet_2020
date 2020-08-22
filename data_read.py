import numpy as np
import pandas as pd
import os
import sys

from driver import load_challenge_data

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



def data_files_load(input_directory,input_files = '',mapping_labels = False, reference_label = False, meta_data = True):
    """Load data files as list along with the labels from the given data directory"""
    # INPUT:
    # input_directory - path of input data
    # input_files - list of files
    # mapping_labels - True (map labels e.g. AF to string numbers)
    # reference_label - True (Load labels from the given 'REFERENCE.csv' in the given 'input_directory')
    # meta_data - True (return meta_data list)

    # OUTPUT:


    # Example
    # [list_data,list_label] = data_files_load(pth_data)
    # list_data - list comprising data (list_data[0][1,:] --> To access first sample and 2nd channel ECG data )
    # list_label = list comprising labesl (list_label[0] --> To access label of first sample)

    if(len(input_files) == 0):
        print('Getting files list from the data directoy - OK')
        input_files = data_files_list(input_directory)

    # converting list of files to absolute path
    string_pth = input_directory+os.path.sep
    input_files_pth = [string_pth+s for s in input_files]

    list_data = []
    list_label = []
    list_fname = []
    list_meta = []

    if(reference_label): # Load labels from the given reference file 'REFERENCE.csv'
        print('Getting labels from the REFERENCE file - OK')
        df_reference = pd.read_csv('REFERENCE.csv', sep=',')
    else:
        print('Getting labels from HEADER - OK')


    for ii in range(len(input_files_pth)):

        tmp_input_file = input_files_pth[ii]
        print('Loading --> ',tmp_input_file)
        data, header_data = load_challenge_data(tmp_input_file)


        if(meta_data or not reference_label):
            tmp_hea = header_data[0].split(' ')
            # print(tmp_hea)
            # ['A0001', '12', '500', '7500', '16-Mar-2020', '19:07:01\n']
            ptID = tmp_hea[0] # 'A0001'
            num_leads = int(tmp_hea[1]) # '12'
            sample_Fs= int(tmp_hea[2]) # '500'
            gain_lead = np.zeros(num_leads) # 1000

            for ll in range(num_leads):
                tmp_hea = header_data[ll+1].split(' ')
                gain_lead[ll] = int(tmp_hea[2].split('/')[0])


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

            tmp_meta = np.hstack([age,sex,sample_Fs,gain_lead])

        if(reference_label): # Load labels from the given reference file 'REFERENCE.csv'
            tmp_idx = df_reference[df_reference['Recording'] == input_files[ii][:-4]].index[0]
            label = df_reference.loc[tmp_idx,['First_label','Second_label','Third_label']].tolist()

        else: # Extract labels from the given header
            #------------------------------------------------------------
            # Extracting label from header data
            #--------------------------------------------------------------
            pass

            #print('Label: ',label)

            if(mapping_labels):
                mapping =  {'Normal': '1', 'AF': '2', 'I-AVB': '3', 'LBBB':'4', 'RBBB':'5', 'PAC':'6', 'PVC' :'7', 'STD':'8', 'STE': '9'}
                for key, value in mapping.items():
                    label = label.replace(key, value)
                    label = label[:-1]

        list_data.append(data)
        list_label.append(label)
        list_fname.append(input_files[ii])
        if(meta_data):
            list_meta.append(tmp_meta)
        else:
            list_meta.append(header_data)

    return list_data,list_label,list_fname,list_meta
