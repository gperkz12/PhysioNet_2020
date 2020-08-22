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
sparse_fit1 = pk.load(open("sparse_fit1.pkl", 'rb'))
sparse_fit2 = pk.load(open("sparse_fit2.pkl", 'rb'))
sparse_fit3 = pk.load(open("sparse_fit3.pkl", 'rb'))
sparse_fit4 = pk.load(open("sparse_fit4.pkl", 'rb'))
sparse_fit1 = np.concatenate((sparse_fit1, sparse_fit2))
print(sparse_fit1.shape)
sparse_fit2 = np.concatenate((sparse_fit3, sparse_fit4))
print(sparse_fit2.shape)
sparse_fit = np.concatenate((sparse_fit1, sparse_fit2))
print(sparse_fit.shape)
X = sparse_fit[:59478, :]
print(X.shape)

# Uses the dictionary learning class to transform the data

atoms = DictionaryLearning(100, 1, 1000, 1e-8, 'lars', 'lasso_lars')

#fit and transform data
atoms.fit(X)


print(atoms.components_.shape)
# Pickle atoms
save_object(atoms, 'atoms.pkl')