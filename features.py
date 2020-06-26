from ecgdetectors import Detectors
from data_read import data_files_load


[data, header_data] = data_read.data_files_load(curfile)

#Before the detectors can be used the class must first be initalised with the sampling rate of the ECG recording:
detectors = Detectors(500)

#Hamilton
r_peaks = detectors.hamilton_detector(data) #I think unfiltered_ecg is the ecg data

#Christov
r_peaks = detectors.christov_detector(data)

#Engelse and Zeelenberg
r_peaks = detectors.engzee_detector(data)

#Pan and Tompkins
r_peaks = detectors.pan_tompkins_detector(data)

#Stationary Wavelet Transform
r_peaks = detectors.swt_detector(data)

#Two Moving Average
r_peaks = detectors.two_average_detector(data)

#Matched Filter
r_peaks = detectors.matched_filter_detector(data,template_file)

"""Heart Rate Variability
HR(self, rr_samples)
   Calculate heart-rates from R peak samples.

NN20(self, rr_samples)
   Calculate NN20, the number of pairs of successive
   NNs that differ by more than 20 ms.

NN50(self, rr_samples)
   Calculate NN50, the number of pairs of successive
   NNs that differ by more than 50 ms.

RMSSD(self, rr_samples, normalise=False)
   Calculate RMSSD (root mean square of successive differences).

SDANN(self, rr_samples, average_period=5.0, normalise=False)
   Calculate SDANN, the standard deviation of the average
   RR intervals calculated over short periods.

SDNN(self, rr_samples, normalise=False)
   Calculate SDNN, the standard deviation of NN intervals.

SDSD(self, rr_samples)
   Calculate SDSD (standard deviation of successive differences),
   the standard deviation of the successive differences between adjacent NNs.

fAnalysis(self, rr_samples)
   Frequency analysis to calc self.lf, self.hf,
   returns the LF/HF-ratio.

pNN20(self, rr_samples)
   Calculate pNN20, the proportion of NN20 divided by total number of NNs.

pNN50(self, rr_samples)
   Calculate pNN50, the proportion of NN50 divided by total number of NNs."""