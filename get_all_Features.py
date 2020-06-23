import numpy as np
import scipy.io as sio
import pickle as pk
from scipy.signal import butter, lfilter
from scipy import stats

# For pickling
def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pk.dump(obj, output, pk.HIGHEST_PROTOCOL)

# data files load

<<<<<<< HEAD
def get_all_features
    read_dir(traindata)
    for all_filenames
        curfile = all_filenames(i)
        [data, headerdata] = load(curfile)
        F[i] = get_all_features(data, headerdata)

        
def get_12ECG_features(data, header_data):
=======

def get_all_features(data, header_data):
>>>>>>> master
    tmp_hea = header_data[0].split(' ')
    ptID = tmp_hea[0]
    num_leads = int(tmp_hea[1])
    sample_Fs = int(tmp_hea[2])
    gain_lead = np.zeros(num_leads)

    for ii in range(num_leads):
        tmp_hea = header_data[ii + 1].split(' ')
        gain_lead[ii] = int(tmp_hea[2].split('/')[0])

    #   We are only using data from lead1
    peaks, idx = detect_peaks(data[0], sample_Fs, gain_lead[0])

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

def get_all_features():




    save_object(features, "features.pkl")