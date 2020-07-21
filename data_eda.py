import pandas as pd
from data_read import data_files_load



def stats_basic(path_data,dset_name = 'PNET2000'):
    """Calculated basic stats on the data based on the data directory"""
    # INPUT:
    #   path_data - location of directory containing ECG data files
    #   dset_name (optional) - Name of the dataset
    # OUTPUT:
    #   df_stats - DataFrame containing basic statistics of data
    #       ['File','Samples','Age','Sex','Fs','Gain_L1','Gain_L2','Gain_L3','Gain_L4','Gain_L5',
    # 'Gain_L6','Gain_L7','Gain_L8','Gain_L9','Gain_L10','Gain_L11','Gain_L12']

    if(dset_name == 'PNET2000'):
        [list_data_all,list_label_all,list_fname_all,list_meta_all] = data_files_load(path_data)

        col_names = ['File','Samples','Age','Sex','Fs','Gain_L1','Gain_L2','Gain_L3','Gain_L4','Gain_L5',
                    'Gain_L6','Gain_L7','Gain_L8','Gain_L9','Gain_L10','Gain_L11','Gain_L12']

        df_stats = pd.DataFrame(index=None, columns=col_names)
        for ii in range(len(list_data_all)):
            df_stats.loc[ii,'File'] = list_fname_all[ii]
            df_stats.loc[ii,'Samples'] = list_data_all[ii].shape[1]
            df_stats.loc[ii,'Age'] = list_meta_all[ii][0]
            df_stats.loc[ii,'Sex'] = list_meta_all[ii][1]
            df_stats.loc[ii,'Fs'] = list_meta_all[ii][2]
            df_stats.iloc[ii,5:] = list_meta_all[ii][3:]
    else:
        print('TO DO')

    return df_stats
