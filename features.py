
from ecgdetectors import Detectors
import data_read
from pyhrv.hrv import hrv
from pyhrv.time_domain import nn20, nn50, sdnn, sdsd, rmssd, hr_parameters
from pyhrv.frequency_domain import frequency_domain
from pyhrv.tools import nn_intervals, time_varying, heart_rate_heatplot, plot_ecg

curdir = 'DATA\TrainData_FeatureExtraction'
[all_data, header_data, BAD_LABELS] = data_read.data_files_load(curdir)


data = all_data[0][0]
print(data.shape)
print(data)

#Before the detectors can be used the class must first be initialised with the sampling rate of the ECG recording:
detectors = Detectors(500)

#Hamilton.
r_peaks = detectors.hamilton_detector(data) #I think unfiltered_ecg is the ecg data

#Christov
#r_peaks = detectors.christov_detector(data)

#Engelse and Zeelenberg
#r_peaks = detectors.engzee_detector(data)

#Pan and Tompkins
#r_peaks = detectors.pan_tompkins_detector(data)

#Stationary Wavelet Transform
#r_peaks = detectors.swt_detector(data)

#Two Moving Average
#r_peaks = detectors.two_average_detector(data)

#Matched Filter
#r_peaks = detectors.matched_filter_detector(data,template_file)

#compute nni series
nn = nn_intervals(r_peaks)

#compute hrv
results = hrv(nn, None, None, 500)

#compute and print nn20, nn50, pn20, pn50
print("nn20 =", results['nn20'], "pnn20 =", results['pnn20'])
print("nn50 =", results['nn50'], "pnn50 =", results['pnn50'])

#compute and print rmssd, sdnn, sdsd, rmssd, hr_parameters
print("sdnn =", results['sdnn'])
print("sdsd =", results['sdsd'])
print("rmssd =", results['rmssd'])

print(hr_parameters(nn))

#compute and print a frequency analysis
freq_results = frequency_domain(nn, None, None, 500)
print(freq_results)



