import numpy as np
import scipy.io as sio
import pickle as pk
from sklearn.decomposition import PCA
from sklearn import decomposition, datasets
from sklearn.preprocessing import StandardScaler


def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pk.dump(obj, output, pk.HIGHEST_PROTOCOL)


iris = datasets.load_iris()
X = iris.data
# Take a random dataset to form the test and train
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

# Save X_test as a pickle file for use in get_12ECG_features
save_object(X_test, 'PhysioNet_2020/X_test.pkl')
# Save sc as a pickle file for use in get_12ECG_features
save_object(sc, 'PhysioNet_2020/sc.pkl')
# Save pca as a pickle file for use in get_12ECG_features
save_object(pca, 'PhysioNet_2020/pca.pkl')



# Save sc as a matlab file for use in get_12ECG_features
#sio.savemat('PhysioNet_2020/sc.mat', {'sc': sc})
#sio.savemat('PhysioNet_2020/pca.mat', {'pca': pca})
#json.dumps(pca)
#pk.dump(pca, open("pca.pkl""))




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
