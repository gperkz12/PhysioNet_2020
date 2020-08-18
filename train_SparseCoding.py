import numpy as np
import pickle as pk
from sklearn.decomposition import DictionaryLearning
from sklearn import datasets
from sklearn import preprocessing
import tensorflow as tf


# For pickling
def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pk.dump(obj, output, pk.HIGHEST_PROTOCOL)

# Load sparse data
Fourier_data = pk.load(open("Fourier_data.pkl", 'rb'))
X = Fourier_data

#uses the dictionary learning class to transform the data

atoms = DictionaryLearning(100, 1, 1000, 1e-8, 'lars', 'lasso_lars')

#fit and transform data
atoms.fit(X)

traindata = atoms.transform(X)



print(atoms.components_.shape)
print(traindata.shape)
traindata = np.reshape(traindata, (3439, 1200))
print(traindata.shape)

# Pickle atoms
save_object(traindata, 'traindata.pkl')