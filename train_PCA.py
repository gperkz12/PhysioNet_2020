import numpy as np
import scipy.io as sio
import pickle as pk
from sklearn.decomposition import PCA
from sklearn import decomposition, datasets
from sklearn.preprocessing import StandardScaler


def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pk.dump(obj, output, pk.HIGHEST_PROTOCOL)


pca_data = pk.load(open("pca_data.pkl", 'rb'))

X = pca_data
# Take a random dataset to form the test and train
rnd_index = np.random.permutation(X.shape[0])
num_test = round(X.shape[0] * 0.2)
test_index = rnd_index[0:num_test]
train_index = rnd_index[num_test:]

#np.where(X.values >= np.finfo(np.float64).max)

X_train = X[train_index][:]
X_test = X[test_index][:]


sc = StandardScaler()
sc.fit(X_train)
X_std_train = sc.transform(X_train)

pca = PCA(n_components=20)
pca.fit(X_std_train)
X_pca_train = pca.transform(X_std_train)

print(pca.explained_variance_.shape)
print(pca.components_.shape)
# Save sc as a pickle file for use in get_12ECG_features
save_object(sc, 'sc.pkl')
# Save pca as a pickle file for use in get_12ECG_features
save_object(pca, 'pca.pkl')

