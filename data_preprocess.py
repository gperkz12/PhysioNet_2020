import numpy as np
from scipy.signal import butter, lfilter
from scipy import stats

def data_outlier_remove(data):
    "remove outlier values based on difference in immediate sample values"

    CONST_DATA_DIFF = 3 #
    CONST_DATA_DIMENSION = 12 # Number of ECG leads

    if(data > CONST_DATA_DIFF).any() or (data < -CONST_DATA_DIFF).any():
        for ii in range(CONST_DATA_DIMENSION):

            # STEP 1: indexes where the difference between immediate samples is greater than +/- CONST_DATA_DIFF
            idx1 = np.argwhere(np.diff(data[ii]) > CONST_DATA_DIFF)
            idx2 = np.argwhere(np.diff(data[ii]) < -CONST_DATA_DIFF)
            idx = np.unique(np.concatenate((idx1,idx2)))
            del idx1, idx2

            # STEP 2: replace above indexes ('idx') with values from previous sample
            if idx.shape[0] > 0:
                for jj in idx:
                    data[ii][jj+1] = data[ii][jj]

    return data

def remove_outlier(ecg):
    if (ecg>3).any():
        for i in range(12):
            b = np.argwhere(np.diff(ecg[i])>3)
            if b.shape[0]>0:
                for k in b[:,0]:
                    ecg[i][k+1] = ecg[i][k]
    if (ecg<-3).any():
        for i in range(12):
            b = np.argwhere(np.diff(ecg[i])<-3)
            if b.shape[0]>0:
                for k in b[:,0]:
                    ecg[i][k+1] = ecg[i][k]
    return ecg

def remove_noise(ecg):
    le = ecg.shape[1]
    for j in range(12):
        noise = []
        b = np.argwhere(np.abs(ecg[j])>2.5)
        b = b[:,0]
        c = np.diff(b)
        count = 0
        pn = 0
        for k in range(len(c)):
            if c[k]<2:
                count += 1
                if count>=8:
                    noise.append(b[k+1])
            elif c[k]>1 and c[k]<8:
                count = 0
                pn += 1
                if pn>1:
                    noise.append(b[k+1])
            elif c[k]<25:
                count = 0
                pn = 0
                noise.append(b[k+1])
            else:
                count = 0
                pn = 0
        if len(noise)>0:
            pre = -1
            for l in range(len(noise)):
                if pre>=0 and noise[l]-pre<200:
                    be = noise[l-1]
                else:
                    be = max(0,noise[l]-60)
                en = min(le,noise[l]+60)
                pre = noise[l]
                ecg[j][be:en] = 0
    return ecg

def tosamples(ecg):
    if len(ecg[0])<625:
        new = np.concatenate((ecg,np.zeros((12,625-len(ecg[0])))))
    else:
        i = 0
        new = []
        while i+625<len(ecg[0]):
            new.append(ecg[:,i:i+625])
            i += 156
        new.append(ecg[:,-625:])
    samples = np.array(new)
    return samples

def tosamples0(ecg):
    if len(ecg[0])<625:
        new = np.concatenate((ecg,np.zeros((12,625-len(ecg[0])))))
    else:
        i = 0
        new = []
        while i+625<len(ecg[0]):
            new.append(ecg[:,i:i+625])
            i += 312
        new.append(ecg[:,-625:])
    samples = np.array(new)
    return samples


def preprocess_type1(data): #

    length = data.shape[1]
    data = data[:,:int(length//4*4)]

    # split ecg data into four segments
    data = data.reshape(data.shape[0],-1,4)

    # taking average of above four segments
    data = np.average(data,axis=2)

    # removing outlier
    data = remove_outlier(data)

    # remove noise (to-do)
    #data = remove_noise(data)

    samples = tosamples(data)

    sample = samples.reshape(-1,12,625,1)

    return sample


def bandpass_filter(data, lowcut, highcut, signal_freq, filter_order):
    """
    Method responsible for creating and applying Butterworth filter.
    :param deque data: raw data
    :param float lowcut: filter lowcut frequency value
    :param float highcut: filter highcut frequency value
    :param int signal_freq: signal frequency in samples per second (Hz)
    :param int filter_order: filter order
    :return array: filtered data
    """
    nyquist_freq = 0.5 * signal_freq
    low = lowcut / nyquist_freq
    high = highcut / nyquist_freq
    b, a = butter(filter_order, [low, high], btype="band")
    y = lfilter(b, a, data)
    return y



def ecg_sig_integrated(ecg_signal,fs):
    # Parameters
    filter_lowcut = 0.001
    filter_highcut = 15.0
    filter_order = 1
    integration_window = 30  # Change proportionally when adjusting frequency (in samples).
    findpeaks_limit = 0.35
    findpeaks_spacing = 100  # Change proportionally when adjusting frequency (in samples).
    refractory_period = 240  # Change proportionally when adjusting frequency (in samples).
    qrs_peak_filtering_factor = 0.125
    noise_peak_filtering_factor = 0.125
    qrs_noise_diff_weight = 0.25



    # Measurements filtering - 0-15 Hz band pass filter.
    filtered_ecg_measurements = bandpass_filter(ecg_signal, lowcut=filter_lowcut, highcut=filter_highcut, signal_freq=fs, filter_order=filter_order)
    filtered_ecg_measurements[:5] = filtered_ecg_measurements[5]

    # Derivative - provides QRS slope information.
    differentiated_ecg_measurements = np.ediff1d(filtered_ecg_measurements)

    # Squaring - intensifies values received in derivative.
    squared_ecg_measurements = differentiated_ecg_measurements ** 2

    # Moving-window integration.
    integrated_ecg_measurements = np.convolve(squared_ecg_measurements, np.ones(integration_window)/integration_window)

    return integrated_ecg_measurements
