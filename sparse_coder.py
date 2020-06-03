
import numpy as np
from sklearn.decomposition import DictionaryLearning
from sklearn import datasets

#import iris practice data
iris = datasets.load_iris()
X = iris.data

#uses the dictionary learning class to transform the data

atoms = DictionaryLearning(n_components=10, alpha=5, max_iter=500, transform_n_nonzero_coefs=2, transform_alpha=5)

#fit the data
atoms.fit(X)

#fit the transform data
atoms.fit_transform(X)

#transform the data
xNew = atoms.transform(X)

#print the new sparse data
print(xNew.shape)
print(xNew)
print(atoms.components_)


