#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 21:43:31 2021

@author: liningqiao
"""

#set up arries for the function

df07=df07[['year', 'buyer_id','target_id']]
df08=df08[['year', 'buyer_id','target_id']]

list1 = []
list3 = []

for seq in df07['buyer_id']:
    # create the column for real buyers list1
    list1.append([seq] *  (len(df07) - seq))
    # create the counterfact for counterfactual buyers
    list3.append(range(seq + 1, len(df07) + 1))

# flatten the two lists
list1 =list(np.concatenate(list1).flat)
list3 =list(np.concatenate(list3).flat)

list2, list5, list8 = list1, list1, list1 
list4, list6, list7 = list3, list3, list3
list0 = ['2007'] *len(list1)

# construct the dataframe of all the real and counterfactual buyer and targets.
df_result = pd.DataFrame(data = np.array([list0, list1, list2, list3, list4, 
                                          list5, list6, list7, list8]).T)
# add the name to each column.
df_result.columns =['year', 'buyer', 'target', 'buyer_prime', 'target_prime', 'buyer',
                    'target_prime', 'buyer_prime', 'target']
df_result
