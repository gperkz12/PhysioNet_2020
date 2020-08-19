##################################
#### TEST get_all_Features.py ####

from get_12ECG_features import get_train_classifier_features

get_train_classifier_features()

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
