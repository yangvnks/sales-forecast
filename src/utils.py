import matplotlib.pyplot as plt
import matplotlib 
import numpy as np
import math
from tqdm import tqdm



def autolabel(rects,bartype):

    if(bartype == 'h'):
        # Attach some text labels.
        for rect in rects:
            if(rect.get_width() > 0.0):
                plt.text((rect.get_x() + rect.get_width() / 2.),
                        (rect.get_y() + rect.get_height() / 2.)+0.4,
                        '%d'%rect.get_width(),
                        ha = 'center',
                        va = 'center',
                        color='gray',
                        fontsize=10) 
    else:
        for rect in rects:
            if(rect.get_height() > 0.0):
                plt.text((rect.get_x() + rect.get_width() / 2.),
                        (rect.get_y() + rect.get_height() / 2.),
                        '%d'%rect.get_height(),
                        ha = 'center',
                        va = 'center',
                        color='white',
                        fontsize=10) 


def replace_nan_median(visdict_list):
    for visdict in visdict_list:
        item_list=[visdict[x] for x in visdict.keys()]
        for val in range(len(item_list)):
            if(math.isnan(item_list[val])):
                prev_val = (val-1) < 0 and item_list[val+1]  or item_list[val-1]
                next_val = (val+1) > len(item_list) and item_list[val-1] or item_list[val+1]
                item_list[val] = float(int((prev_val + next_val)/2))
        iterator = 0
        for k,i in visdict.items():
            visdict[k]=item_list[iterator]
            iterator+=1


def replace_nan_df(dataset,col_name1,col_name2,dictionary):
    nan_index=dataset[dataset[col_name1].isnull()].index.tolist()
    for index in tqdm(nan_index):
        humidty_lvl = dataset.loc[index,col_name2] 
        dataset.loc[index,col_name1] = dictionary[humidty_lvl]