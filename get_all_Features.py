import numpy as np
import scipy.io as sio
import pickle as pk
import get_12ECG_features
import data_read
from scipy.signal import butter, lfilter
from scipy import stats


# For pickling
def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pk.dump(obj, output, pk.HIGHEST_PROTOCOL)

# data files load

def get_all_features(data, header_data):
    i = 0
    traindata = 'DATA\TrainData_Classifier'
    for all_filenames in traindata:
        data_read.data_files_list(traindata)
        curfile = all_filenames(i)
        [data, header_data] = data_read.data_files_load(curfile)
        F[i] = get_file_features(data, header_data)
        #data_read(traindata, header_data)
        pca_data[i] = F[i]
    save_object(pca_data, pca_data.pkl)



        

def get_file_features(data, header_data):
    tmp_hea = header_data[0].split(' ')
    ptID = tmp_hea[0]
    num_leads = int(tmp_hea[1])
    sample_Fs = int(tmp_hea[2])
    gain_lead = np.zeros(num_leads)

    for ii in range(num_leads):
        tmp_hea = header_data[ii + 1].split(' ')
        gain_lead[ii] = int(tmp_hea[2].split('/')[0])

    #   We are only using data from lead1
    peaks, idx = get_12ECG_features.detect_peaks(data[0], sample_Fs, gain_lead[0])

    #   mean
    mean_RR = np.mean(idx / sample_Fs * 1000)
    mean_Peaks = np.mean(peaks * gain_lead[0])

    #   median
    median_RR = 0
    median_Peaks = np.median(peaks * gain_lead[0])

    #   standard deviation
    std_RR = np.std(idx / sample_Fs * 1000)
    std_Peaks = np.std(peaks * gain_lead[0])

    #   variance
    var_RR = stats.tvar(idx / sample_Fs * 1000)
    var_Peaks = stats.tvar(peaks * gain_lead[0])

    #   Skewness
    skew_RR = stats.skew(idx / sample_Fs * 1000)
    skew_Peaks = stats.skew(peaks * gain_lead[0])

    #   Kurtosis
    kurt_RR = stats.kurtosis(idx / sample_Fs * 1000)
    kurt_Peaks = stats.kurtosis(peaks * gain_lead[0])

# Need to pickle the features here