
import numpy as np
from sklearn.decomposition import DictionaryLearning
from sklearn import datasets

#import iris practice data
iris = datasets.load_iris()
X = iris.data

#uses the dictionary learning class to transform the data

atoms = DictionaryLearning(None, 1, 1000, 1e-08, 'lars', 'omp', None, None, None, None, None, False, False, None, False, False)

#fit the data
atoms.fit(X, None)

#fit the transform data
atoms.fit_transform(X, None)

#transform the data
xNew = atoms.transform(X)

#print the new sparse data
print(xNew)


