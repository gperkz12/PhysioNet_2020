%% Train Classifiers

close all; clear all; clc;

load data_for_training;

DATA_AF = [all_features; all_labels(1,:)]';
DATA_IAVB = [all_features; all_labels(2,:)]';
DATA_LBBB = [all_features; all_labels(3,:)]';
DATA_Normal = [all_features; all_labels(4,:)]';
DATA_PAC = [all_features; all_labels(5,:)]';
DATA_PVC = [all_features; all_labels(6,:)]';
DATA_RBBB = [all_features; all_labels(7,:)]';
DATA_STD = [all_features; all_labels(8,:)]';
DATA_STE = [all_features; all_labels(9,:)]';


%% Get these using MATLAB's Classification Learner App
model.AF = CubicSVM_AF;
model.IAVB = MediumGaussianSVM_IAVB;
model.LBBB = WeightedKNN_LBBB;
model.Normal = MediumGaussianSVM_Normal;
model.PAC = WeightedKNN_PAC;
model.PVC = MediumGaussianSVM_PVC;
model.RBBB = CubicSVM_RBBB;
model.STD = CubicSVM_STD;
model.STE = QuadraticSVM_STE;

save('trained_model','model');