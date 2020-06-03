
import numpy as np
from sklearn.decomposition import DictionaryLearning
from sklearn import datasets

#import iris practice data
iris = datasets.load_iris()
X = iris.data

#uses the dictionatry learning function to transform the data
#atoms = dict_learning(X, 4, 1, 100, 1e-8, 'lars', None, None, None, None, False, None, False, False, False)

atoms = DictionaryLearning(None, 1, 1000, 1e-08, 'lars', 'omp', None, None, None, None, None, False, False, None, False, False)





#print the sparse data

atoms.fit(X, None)

atoms.fit_transform(X, None)

params = atoms.get_params(True)

atoms.set_params()

xNew = atoms.transform(X)

print(xNew)


