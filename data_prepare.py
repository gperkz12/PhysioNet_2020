import numpy as np



def data_prepare_list2matrix(x_lst,param):
#     """convert data from list to numpy array for feeding into classifier"""
#     x_lst - input data in list form such that x_lst = [sample_number][lead_number]
#     param - data preparation parameters in dictionary format
#             1. 'method' - type of method for data preparation in string format
#             2. 'leads'  - leads number in list form

    # SINGLE LEAD
    if('classifier1' in param['method'] and 'single' in param['method']):

        NO_SAMPLES = 4500
        lead_no = int(param['leads'][0])

        x_arr = np.zeros((len(x_lst), NO_SAMPLES))

        for ii in range(len(x_lst)):
            if(len(x_lst[ii][lead_no-1]) > NO_SAMPLES):
                x_arr[ii, :] = x_lst[ii][lead_no-1][0:NO_SAMPLES]
            else:
                x_arr[ii,0:len(x_lst[ii][lead_no-1])] = x_lst[ii][lead_no-1][:]

        return x_arr
