import numpy as np
import scipy.io as sio
import pickle as pk
import get_12ECG_features
import data_read
from scipy.signal import butter, lfilter
from scipy import stats
import matplotlib.pyplot as plt


# data files load


def get_all_features():

    traindata = 'DATA\TrainData_FeatureExtraction'
    [data, labels, filenames, header_data] = data_read.data_files_load(traindata)
    for i in range(0, (len(data))):
        curfeatures = get_fourier_data(data[i], header_data[i])
        if i == 0:
            Fourier_data = curfeatures
        else:
            tmp = np.column_stack((Fourier_data, curfeatures))
            Fourier_data = tmp

    print(Fourier_data.shape)

    plt.style.use('ggplot')
    plt.hist(Fourier_data, bins=20)
    plt.show()

    save_object(Fourier_data, '.\Fourier_data.pkl')


    return 0


def get_fourier_data(data, header_data):

    age = header_data[0]
    sex = header_data[1]
    sample_Fs = header_data[2]
    num_leads = len(header_data) - 3
    gain_lead = np.zeros(num_leads)

    for ii in range(num_leads):
        gain_lead[ii] = header_data[3+ii]


    tmp_fourier_data = len(data[0])
    return tmp_fourier_data

    #x = [len(data[i])]

    #plt.style.use('ggplot')
    #plt.hist(x, bins=20)
    #plt.show()

# For pickling
def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pk.dump(obj, output, pk.HIGHEST_PROTOCOL)

# Try axcept