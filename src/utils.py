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


def get_region_updatemenu(default_active=0):
    return list([
    dict(active=default_active,
         buttons=list([  
             dict(label = 'All Regions',
                 method = 'update',
                 args = [{'visible': [True, True, True, True,True, True, True,True, True, True,True]},
                         {'title': 'All Regions'}]),
            dict(label = 'Region 0',
                 method = 'update',
                 args = [{'visible': [True, False, False, False,False, False, False,False, False, False,False]},
                         {'title': 'Region 0'}]),
            dict(label = 'Region 1',
                 method = 'update',
                 args = [{'visible': [False, True, False, False,False, False, False,False, False, False,False]},
                         {'title': 'Region 1'}]),
            dict(label = 'Region 2',
                 method = 'update',
                 args = [{'visible': [False, False, True, False,False, False, False,False, False, False,False]},
                         {'title': 'Region 2'}]),
             dict(label = 'Region 3',
                 method = 'update',
                 args = [{'visible': [False, False, False, True,False, False, False,False, False, False,False]},
                         {'title': 'Region 3'}]),
             dict(label = 'Region 4',
                 method = 'update',
                 args = [{'visible': [False, False, False, False,True, False, False,False, False, False,False]},
                         {'title': 'Region 4'}]),
             dict(label = 'Region 5',
                 method = 'update',
                 args = [{'visible': [False, False, False, False,False, True, False,False, False, False,False]},
                         {'title': 'Region 5'}]),
             dict(label = 'Region 6',
                 method = 'update',
                 args = [{'visible': [False, False, False, False,False, False, True,False, False, False,False]},
                         {'title': 'Region 6'}]),
             dict(label = 'Region 7',
                 method = 'update',
                 args = [{'visible': [False, False, False, False,False, False, False,True, False, False,False]},
                         {'title': 'Region 7'}]),
             dict(label = 'Region 8',
                 method = 'update',
                 args = [{'visible': [False, False, False, False,False, False, False,False, True, False,False]},
                         {'title': 'Region 8'}]),
             dict(label = 'Region 9',
                 method = 'update',
                 args = [{'visible': [False, False, False, False,False, False, False,False, False, True,False]},
                         {'title': 'Region 9'}]),
             dict(label = 'Region 10',
                 method = 'update',
                 args = [{'visible': [False, False, False, False,False, False, False,False, False, False,True]},
                         {'title': 'Region 10'}]),
        ]),
    )
])
