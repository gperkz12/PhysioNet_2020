import numpy as np

def convert_header_data(header_data):
    tmp_hea = header_data[0].split(' ')
    # print(tmp_hea)
    # ['A0001', '12', '500', '7500', '16-Mar-2020', '19:07:01\n']
    ptID = tmp_hea[0] # 'A0001'
    num_leads = int(tmp_hea[1]) # '12'
    sample_Fs= int(tmp_hea[2]) # '500'
    gain_lead = np.zeros(num_leads) # 1000

    for ll in range(num_leads):
        tmp_hea = header_data[ll+1].split(' ')
        gain_lead[ll] = int(tmp_hea[2].split('/')[0])

    for iline in header_data:
        if iline.startswith('#Age'):
            tmp_age = iline.split(': ')[1].strip()
            age = int(tmp_age if tmp_age != 'NaN' else 57)
        elif iline.startswith('#Sex'):
            tmp_sex = iline.split(': ')[1]
            if tmp_sex.strip()=='Female':
                sex =1
            else:
                sex=0
        elif iline.startswith('#Dx'):
            label = iline.split(': ')[1].split(',')[0]

    tmp_meta = np.hstack([age,sex,sample_Fs,gain_lead])

    return tmp_meta
