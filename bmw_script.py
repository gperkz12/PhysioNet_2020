#import data_read
import get_label

#[list_data,list_label] = data_read.data_files_load('./DATA/TrainData_FeatureExtraction')

#for n in list_data:
#    print(n.shape)


#print('................')
#print(len(list_label))

test1 = get_label.getLabel("A0001")
print(test1)
test2 = get_label.getLabel("A1236")
print(test2)
