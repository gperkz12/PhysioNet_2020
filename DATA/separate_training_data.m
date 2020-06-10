%% Random Permutation
% Randomly assign each ECG file to one of three groups:
%    Group 1: Used to train the feature extraction algorithms (PCA, sparse
%             coding, possibly other dimensionality reduction techniques)
%    Group 2: Used to train the classification algorithms.
%    Group 3: Used as validation data 
%
%
% Right now, use 25% in group 1, 50% in group 2, and 25% in group 3.
%
% To redo this, move all files from the three data folders to the 'AllData'
% directory and re-run this code.

close all; clear all; clc;

PNET_dir = 'AllData/';

all_files = ls([PNET_dir '*.mat']);
all_files = all_files(:,1:5);

N = size(all_files,1);

rand_idx = randperm(N);

N_feature = ceil(0.25*N);
N_class = ceil(0.50*N);
N_valid = N - N_feature - N_class;

idx_feature = rand_idx(1:N_feature);
idx_class = rand_idx(N_feature+1:N_feature+N_class);
idx_valid = rand_idx(N_feature+N_class+1:end);

for i = 1:N_feature
    cur_file = all_files(idx_feature(i),:);
    source_file = ['AllData/' cur_file '.mat'];
    dest_file = ['TrainData_FeatureExtraction/' cur_file '.mat'];
    movefile(source_file,dest_file);
    
    source_file = ['AllData/' cur_file '.hea'];
    dest_file = ['TrainData_FeatureExtraction/' cur_file '.hea'];
    movefile(source_file,dest_file);
end

for i = 1:N_class
    cur_file = all_files(idx_class(i),:);
    source_file = ['AllData/' cur_file '.mat'];
    dest_file = ['TrainData_Classifier/' cur_file '.mat'];
    movefile(source_file,dest_file);
    
    source_file = ['AllData/' cur_file '.hea'];
    dest_file = ['TrainData_Classifier/' cur_file '.hea'];
    movefile(source_file,dest_file);
end

for i = 1:N_valid
    cur_file = all_files(idx_valid(i),:);
    source_file = ['AllData/' cur_file '.mat'];
    dest_file = ['ValidationData/' cur_file '.mat'];
    movefile(source_file,dest_file);
    
    source_file = ['AllData/' cur_file '.hea'];
    dest_file = ['ValidationData/' cur_file '.hea'];
    movefile(source_file,dest_file);
end