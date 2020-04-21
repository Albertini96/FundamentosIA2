# -*- coding: utf-8 -*-

import pandas as pd
from math import log2
import operator


#Calculates simple entropy
#0 if all samples has same y
#0 if all samples has mixed y
def calc_entropy(p, n):
#    return (-p / (p+n)) * (log2(p / (p+n))) - (n/(p+n)) * (log2(n / (p+n)))
    return (-p / (p+n)) * (log2( (p / (p+n)) +1)) - (n/(p+n)) * (log2( n / (p+n) +1))

#Calculte entropy based on last column of dataset
def get_entropy(ds):
    
    p = ds[ds.iloc[:, - 1] == 1].count()[0]
    n = ds[ds.iloc[:, - 1] == 0].count()[0]
    
    return calc_entropy(p, n), [p, n]

#Calculate entropy foreach value of each column
def get_all_entropy(ds):
    
    entropy_dict = dict()
    
    last_col = ds.iloc[:, - 1].name
    feat_cols = ds.columns.tolist()[:-1]
    
    for col in feat_cols:
    
        entropy_dict[col] = dict()
        
        #Current Column
        cc = ds[[col, last_col]]
        
        for cc, sub_ds in cc.groupby(cc.columns[0]):
            curr_it = sub_ds.iloc[0,0]
            entropy_dict[col][curr_it] = dict()
            entropy_dict[col][curr_it]['entropy'], entropy_dict[col][curr_it]['pn'] = get_entropy(sub_ds)

    return entropy_dict

#Calculate average information gain
def get_info(ds):
    info_dict = dict()
    ds_entropy, ds_pn = get_entropy(ds)
    ds_details = get_all_entropy(ds)
    
    for col in ds_details:
        vals = ds_details.get(col)

        temp_list = list()
        for i in vals:    
            it = vals.get(i)
            temp_list.append( ((it['pn'][0] + it['pn'][1]) / (ds_pn[0] + ds_pn[1])) * it['entropy'] )
            info_dict[col] = sum(temp_list)
            

    return info_dict

#Calculate gain from dataset
def calculate_gain(ds):
    
    gain_dict = dict()
    info = get_info(ds)
    total_entropy, total_pn = get_entropy(ds)
    
    for i in info:
        val = info.get(i)
        gain_dict[i] = total_entropy - val
    
    sorted_d = dict(sorted(gain_dict.items(), key=operator.itemgetter(1),reverse=True))

    return sorted_d

ds = pd.read_excel('Base.xlsx')

print(get_all_entropy(ds))
print(get_info(ds))
print(calculate_gain(ds))

    
    









