import numpy as np
import pickle as pk
from sklearn.decomposition import DictionaryLearning
from sklearn import datasets
from sklearn import preprocessing

<<<<<<< HEAD
<<<<<<< HEAD
#load pca data
Fourier_data = pk.load(open("Fourier_data.pkl", 'rb'))
X = Fourier_data
<<<<<<< HEAD

#uses the dictionary learning class to transform the data

atoms = DictionaryLearning(100, 1, 1000, 1e-8, 'lars', 'lasso_lars')

=======
<<<<<<< HEAD
#load fourier data
fourier_data = pk.load(open("Fourier_data.pkl", 'rb'))
X = fourier_data
#test
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

atoms = DictionaryLearning(100, 5, 1000, 1e-8, 'lars', 'lasso_lars')
=======
=======
>>>>>>> master
#load pca data
Fourier_data = pk.load(open("Fourier_data.pkl", 'rb'))
X = Fourier_data

#uses the dictionary learning class to transform the data

atoms = DictionaryLearning(100, 1, 1000, 1e-8, 'lars', 'lasso_lars')

>>>>>>> master
#fit and transform data
atoms.fit(X)

=======

#uses the dictionary learning class to transform the data

atoms = DictionaryLearning(100, 1, 1000, 1e-8, 'lars', 'lasso_lars')

#fit and transform data
atoms.fit(X)

>>>>>>> master
traindata = atoms.transform(X)

# Pickle atoms
save_object(atoms, 'atoms.pkl')

print(traindata)
print(traindata.shape)

def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pk.dump(obj, output, pk.HIGHEST_PROTOCOL)