import numpy as np
import scipy.io as sio
from sklearn.decomposition import PCA
from sklearn import decomposition, datasets
from sklearn.preprocessing import StandardScaler

iris = datasets.load_iris()
X = iris.data
# print(X.shape)

rnd_index = np.random.permutation(X.shape[0])
num_test = round(X.shape[0] * 0.2)
test_index = rnd_index[0:num_test]
train_index = rnd_index[num_test:]


X_train = X[train_index][:]
X_test = X[test_index][:]


sc = StandardScaler()
sc.fit(X_train)
X_std_train = sc.transform(X_train)

pca = PCA(n_components=2)
pca.fit(X_std_train)
X_pca_train = pca.transform(X_std_train)

print(pca)

sio.savemat('PhysioNet_2020/sc.mat', {'sc': sc})
#sio.savemat('PhysioNet_2020/pca.mat', {'pca': pca})



# print(X_pca_train)
#
# print(iris.target)
#
# print(pca.components_)
#
# print(pca.explained_variance_ratio_)
#
# print(pca.singular_values_)


# def get_pca_feature():
#
#     print(sc, pca)
#     X_std_test = sc.transform(X_test)
#     X_pca_test = pca.transform(X_std_test)
#
#     print(X_std_test)
#     print(X_pca_test)
#
#     return X_pca_test
#     load sc and pca
#     takes in X_test and then it does line 23 but test and line 27 but test
