import data_read

[list_data,list_label] = data_read.data_files_load('./DATA2')

for n in list_data:
    print(n.shape)


print('................')
print(list_label)
