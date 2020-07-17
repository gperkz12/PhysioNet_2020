
from ecgdetectors import Detectors
import data_read
from pyhrv.hrv import hrv
from pyhrv.time_domain import hr_parameters
from pyhrv.frequency_domain import frequency_domain
from pyhrv.tools import nn_intervals, plot_ecg, heart_rate, tachogram


def heart_rate_variability(sample, lead, rpeak_method = 'string'):
    curdir = 'DATA\TrainData_FeatureExtraction'
    [all_data, header_data, BAD_LABELS] = data_read.data_files_load(curdir)

    data = all_data[sample][lead]

    """INITIALIZE DETECTOR CLASS WITH THE SAMPLING RATE:"""
    detectors = Detectors(500)

    """FIND RPEAK USING ONE OF THE METHODS BELOW--------------------"""

    if rpeak_method == 'hamilton' or rpeak_method == 'string':
        #Hamilton.
        r_peaks = detectors.hamilton_detector(data)

    elif rpeak_method == 'christov':
        #Christov
        r_peaks = detectors.christov_detector(data)

    elif rpeak_method == 'engelse':
        #Engelse and Zeelenberg
        r_peaks = detectors.engzee_detector(data)

    elif rpeak_method == 'engelse':
        #Pan and Tompkins
        r_peaks = detectors.pan_tompkins_detector(data)

    elif rpeak_method == 'stationary_wavelet':
        #Stationary Wavelet Transform
        r_peaks = detectors.swt_detector(data)

    elif rpeak_method == 'two_moving_average':
        #Two Moving Average
        r_peaks = detectors.two_average_detector(data)

    #elif rpeak_method == 'matched_filter':
        #Matched Filter
        #go to pyhrv documentation to find the template file
        #r_peaks = detectors.matched_filter_detector(data,template_file)

    """COMPUTE NNI SERIES-------------------------------------------"""
    nn = nn_intervals(r_peaks) #nni seems to be off by a factor of 3
    print("\n\n", nn, "\n\n")

    """PLOT ECG/TACHOGRAM-------------------------------------------"""
    #plot_ecg(data, sampling_rate = 500)
    #tachogram(nn, sampling_rate = 500)

    """COMPUTE HRV--------------------------------------------------"""
    results = hrv(nn, None, None, 500)

    """COMPUTE HR PARAMETERS--(SOMETHING IS WRONG HERE BPM TOO HIGH)"""
    hr = heart_rate(nn)

    """COMPUTE FREQUENCY ANALYSIS-----------------------------------"""
    freq_results = results['fft_bands']

    return results, hr, freq_results

"""To retrieve parameters from the Tuple, index the Tuple by the 
    string description of the parameter you want
    EX: results['sdnn']"""

"""TESTING HRV METHOD------------------------------------------------"""

results, hr, freq_results = heart_rate_variability(0, 0, 'christov')

print(hr, '\n\n')
print('sdnn = ', results['sdnn'], '\n\n')
print('rmssd = ', results['rmssd'], '\n\n')
print('nn20 = ', results['nn20'], '\n\n')
print('nn50 = ', results['nn50'], '\n\n')
print('sdsd = ', results['sdsd'], '\n\n')
print('pnn20 = ', results['pnn20'], '\n\n')
print('pnn50 = ', results['pnn50'], '\n\n')
print('lf = ', freq_results['lf'] , '\n\n')
print('hf = ', freq_results['hf'], '\n\n')
print('fft_ratio = ', results['fft_ratio'], '\n\n')
print('hr_mean = ', results['hr_mean'], '\n\n')
print('hr_min = ', results['hr_min'], '\n\n')
print('hr_max = ', results['hr_mean'], '\n\n')