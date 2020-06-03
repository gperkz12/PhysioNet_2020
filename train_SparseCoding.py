
import numpy as np
from sklearn.decomposition import DictionaryLearning
from sklearn import datasets

#import iris practice data
iris = datasets.load_iris()
X = iris.data

rnd_index = np.random.permutation(X.shape[0])
num_test = round(X.shape[0] * 0.2)
test_index = rnd_index[0:num_test]
train_index = rnd_index[num_test:]


X_train = X[train_index][:]
X_test = X[test_index][:]

#uses the dictionary learning class to transform the data

atoms = DictionaryLearning(None, 1, 1000, 1e-08, 'lars', 'omp', None, None, None, None, None, False, False, None, False, False)

#fit and transform data

sparsedata = atoms.fit_transform(X_test, None)

#print the new sparse data
print(X.shape, sparsedata.shape)
print(sparsedata)