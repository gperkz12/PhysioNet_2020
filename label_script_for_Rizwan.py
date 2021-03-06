import numpy as np
import scipy.io as sio
import pickle as pk
import get_12ECG_features
import data_read
from scipy.signal import butter, lfilter
from scipy import stats

def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pk.dump(obj, output, pk.HIGHEST_PROTOCOL)

traindata = 'DATA/TrainData_Classifier'
[data, labels, filenames, header_data] = data_read.data_files_load(traindata)

#print(labels)   # Prints all labels, bad formatting
#print(*labels, sep = "\n") # Prints labels for each patient on new lines, but only prints the first label for each patient.

print(len(labels))  # Should equal number of patients
save_object(labels, 'y_train.pkl')

