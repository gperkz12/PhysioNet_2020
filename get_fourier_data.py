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
    [data, header_data, BAD_LABELS] = data_read.data_files_load(traindata)
    for i in range(0, (len(data))):
        curfeatures = get_fourier_data(data[i], header_data[i])
        if i == 0:
            sparse_data = curfeatures
        else:
            tmp = np.column_stack((psa_data, curfeatures))
            sparse_data = tmp
    save_object(sparse_data, '.\sparse_data.pkl')

    return 0


def get_fourier_data(data, header_data):

    tmp_hea = header_data[0].split(' ')
    ptID = tmp_hea[0]
    num_leads = int(tmp_hea[1])
    sample_Fs = int(tmp_hea[2])
    gain_lead = np.zeros(num_leads)
    for ii in range(num_leads):
        tmp_hea = header_data[ii + 1].split(' ')
        gain_lead[ii] = int(tmp_hea[2].split('/')[0])

    for i in range(0, (len(data))):
        print(len(data[i]))

        x = [len(data[i])]

    plt.style.use('ggplot')
    plt.hist(x, bins=20)
    plt.show()

# For pickling
def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pk.dump(obj, output, pk.HIGHEST_PROTOCOL)

# Try axcept