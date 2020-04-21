# -*- coding: utf-8 -*-

import pandas as pd
from numpy import log2
import operator


#Calculates simple entropy
#0 if all samples has same y
#1 if all samples has mixed y
def calc_entropy(p_dict):
    ret = 0
    s = 0
    for i in p_dict:
        s = s + p_dict[i]
    
    for i in p_dict:
        ret = ret + ((-p_dict[i]/s) * log2((p_dict[i]/s)))
    
    return ret


#Calculte entropy based on last column of dataset
def get_entropy(ds):
    lst = ds.iloc[:, - 1].unique()
    dict_p = dict()
    
    for i in lst:
        dict_p[i] = ds[ds.iloc[:, - 1] == i].count()[0]
    
    return calc_entropy(dict_p), dict_p


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
    
    den = 0
    for i in ds_pn:
        den = den + ds_pn[i]
    
    for col in ds_details:
        vals = ds_details.get(col)

        temp_list = list()
        for i in vals:    
            it = vals.get(i)
            
            nom = 0
            
            for c in it['pn']:
                nom = nom + it['pn'][c] 
                
            temp_list.append(( abs(nom) / abs(den) )* it['entropy'] )
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


def create_decision_tree(ds):
    
    ds_gain = calculate_gain(ds)

    tree_dict = dict()
    
    curr_col = list(ds_gain.keys())[0]    
    unique_vals = ds[curr_col].unique().tolist()
    
    print(unique_vals)
    for i in ds_gain:
        print(i)


ds = pd.read_excel('Base.xlsx')

create_decision_tree(ds)

#print(ds)
#print()
#print(get_all_entropy(ds))
#print()
#print(get_info(ds))
#print()
#print(calculate_gain(ds))

    
    









