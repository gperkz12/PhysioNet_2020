%% test_equality

close all; clear all; clc;

PNET_dir = 'Training_WFDB/';
OTHER_dir = 'TrainingSet1/';

all_files = ls([OTHER_dir '*.mat']);
N = length(all_files);

error = zeros(1,N);

for i = 1:N
    cur_file = all_files(i,:);
    load([PNET_dir cur_file]);
    load([OTHER_dir cur_file]);
    
    error(i) = norm(round(1000*ECG.data(:)) - val(:));
end

sum(error);

different = find(error~=0);

for i = different
    cur_file = all_files(i,:);
    load([PNET_dir cur_file]);
    load([OTHER_dir cur_file]);
    figure(i);
    subplot(311); plot(round(1000*ECG.data(:))); xlabel('OTHER'); title(cur_file);
    subplot(312); plot(val(:)); xlabel('PNET');
    subplot(313); plot(round(1000*ECG.data(:)) - val(:)); xlabel(['Difference (' num2str(error(i)) ')']);
end

% Conclusion: Only a handful of files are different, and all the
% differences occur where there are huge spikes in the ECG reading. Both
% signals have the spikes, but the heights of the spikes are off by
% 5-10 mV (out of 10 V).