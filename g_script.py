import get_all_Features
import get_fourier_data
import pickle as pk

get_fourier_data.get_all_features()
sparse_fit = pk.load(open("sparse_fit.pkl", 'rb'))
print(sparse_fit.shape)