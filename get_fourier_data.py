import numpy as np
import scipy.io as sio
import pickle as pk
from data_read import data_files_load
from scipy.signal import butter, lfilter
from scipy import stats
import matplotlib.pyplot as plt
from scipy import fft


# data files load


def get_all_features():
    # When on windows it's a backslash slash, on linux its a forward slash
    traindata = '/media/gperkz/KINGSTON/TrainData_FeatureExtraction'
    [data, labels, filenames, header_data] = data_files_load(traindata)
    for i in range(0, (len(data))):
         curfeatures = get_fourier_data(data[i], header_data[i])
         if i == 0:
             Fourier_data = curfeatures
         else:
             print(i)
             tmp = np.vstack((Fourier_data, curfeatures))
             Fourier_data = tmp
    print(Fourier_data.shape)
    Fourier_data1 = Fourier_data[:29739, :]

    Fourier_data2 = Fourier_data[29740:59478, :]

    Fourier_data3 = Fourier_data[59479:89217, :]

    Fourier_data4 = Fourier_data[89218:, :]

    save_object(Fourier_data1, 'sparse_fit1.pkl')
    save_object(Fourier_data2, 'sparse_fit2.pkl')
    save_object(Fourier_data3, 'sparse_fit3.pkl')
    save_object(Fourier_data4, 'sparse_fit4.pkl')



    return 0


def get_fourier_data(data, header_data):

    age = header_data[0]
    sex = header_data[1]
    sample_Fs = header_data[2]
    num_leads = len(header_data) - 3
    gain_lead = np.zeros(num_leads)

    for ii in range(num_leads):
        gain_lead[ii] = header_data[3+ii]

    n_samples = 8192
    for i in range(0, len(data)):
        curdata = np.fft.fft(data[i], n_samples)
        if i == 0:
            Fdata = curdata
        else:
            tmp = np.vstack((Fdata, curdata))
            Fdata = tmp

    Fdata = np.abs(Fdata)

    Fdata = Fdata[:, 0:round(n_samples / 2)]
    return Fdata

# For pickling
def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pk.dump(obj, output, pk.HIGHEST_PROTOCOL)