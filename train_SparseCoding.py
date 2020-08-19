import numpy as np
import pickle as pk
from sklearn.decomposition import DictionaryLearning
from sklearn import datasets
from sklearn import preprocessing

# For pickling
def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pk.dump(obj, output, pk.HIGHEST_PROTOCOL)

# Load sparse data
sparse_fit = pk.load(open("sparse_fit.pkl", 'rb'))
X = sparse_fit

#uses the dictionary learning class to transform the data

atoms = DictionaryLearning(100, 1, 1000, 1e-8, 'lars', 'lasso_lars')

#fit and transform data
atoms.fit(X)


print(atoms.components_.shape)
# Pickle atoms
save_object(atoms, 'atoms.pkl')