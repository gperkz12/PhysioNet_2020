import numpy as np
import pickle as pk
from sklearn.decomposition import DictionaryLearning
from sklearn import datasets
from sklearn import preprocessing

#load pca data
pca_data = pk.load(open("pca_data.pkl", 'rb'))
X = pca_data


def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pk.dump(obj, output, pk.HIGHEST_PROTOCOL)


rnd_index = np.random.permutation(X.shape[0])
num_test = round(X.shape[0] * 0.2)
test_index = rnd_index[0:num_test]
train_index = rnd_index[num_test:]


X_train = X[train_index][:]
X_test = X[test_index][:]

#uses the dictionary learning class to transform the data

atoms = DictionaryLearning(None, 1, 1000, 1e-8, 'lars', 'lasso_lars')

#fit and transform data
atoms.fit(X= X_train)

traindata = atoms.transform(X_train)

testdata = atoms.transform(X_test)

# Pickle atoms
save_object(atoms, 'atoms.pkl')

print(traindata, '\n\n\n', testdata)