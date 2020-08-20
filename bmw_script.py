##################################
#### This code runs get_12ECG_features on all
#### the files in 'DATA/TrainData_Classifier'
#### The result is saved as 'classifier_data.pkl'
#### and should be used to train the classification
#### model.
##################################
"""
import numpy as np
import data_read
from get_12ECG_features import get_12ECG_features, save_object

dir_classifier = 'DATA/TrainData_Classifier'
[data, labels, filenames, header_data] = data_read.data_files_load(dir_classifier)
#for i in range(0, (len(data))):
for i in range(0,30):
    curfeatures = get_12ECG_features(data[i], header_data[i])
    if i == 0:
        classifier_data = curfeatures
    else:
        print(i)
        tmp = np.row_stack((classifier_data, curfeatures))
        classifier_data = tmp
print(classifier_data.shape)
# Should be 3439x1220
save_object(classifier_data, 'classifier_data.pkl')
"""
##################################
##################################
#### TEST get_all_Features.py ####
"""
import get_all_Features

get_all_Features.get_all_features()
"""
##################################
##################################
#### TEST get_all_Features.py ####
"""
import data_read
import driver
import get_12ECG_features
import convert_header_data

data, header_data = driver.load_challenge_data('DATA/TrainData_Classifier')
header_data = convert_header_data.convert_header_data(header_data)
features = get_12ECG_features.get_12ECG_features(data, header_data)
print(features)
# Should be 1x1220
print(features.shape)
"""
##################################

##################################
#### TEST get_fourier_data.py ####
"""
import get_fourier_data

get_fourier_data.get_all_features()
"""
##################################

##################################
#### TEST features.py ####
"""
import hrv_features

hrv_features.heart_rate_variability(105,7,'pan')
"""
#################################

###########################
#### TEST data_read.py ####
"""
import data_read

[list_data,list_label,list_files,list_header] = data_read.data_files_load('./DATA/TrainData_FeatureExtraction_sub')
for n in list_data:
    print(n.shape)
print('................')
print(len(list_label))
print('................')

pass_header = list_header[0];
print(pass_header)
print(len(pass_header))
"""

###########################

###########################
#### TEST get_label.py ####
"""
import get_label

test1 = get_label.getLabel("A0001")
print(test1)
test2 = get_label.getLabel("A1236")
print(test2)
"""
###########################

###########################
#### TEST get_label.py ####

import convert_label

classes = ['164884008', '164889003', '164909002', '164931005', '270492004', '284470004', '426783006', '429622005', '59118001']

label = ['59118001\n']

newlabel = convert_label.convert_label(label,classes)
print(newlabel)
###########################
