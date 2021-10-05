#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 10:04:08 2021

@author: liningqiao
"""

import scipy.optimize as opt
from scipy.optimize import minimize
import numpy as np
import pandas as pd
import statsmodels.api as sm

# read the stata data
data = pd.read_stata('PS4_data.dta')

# generate the hourly wage variable
data['hhourly_wage'] = data['hlabinc']/data['hannhrs']

# describe the variables to check the data
data[['hlabinc', 'hannhrs', 'hhourly_wage']].describe()

# retain the dataset if the head hourly wage > $7
data1 = data[data['hhourly_wage'] > 7]

# retain the dataset if the head age is between 25 and 60.
data2 = data1[data1['age'].between(25,60)]

# convert the head race variable (hrace) to dummy
data2_dummies = pd.get_dummies(data2, columns = ['hrace'])
data3 = data2_dummies.rename(columns={"hrace_1.0":"Black", "hrace_2.0": "Hispanic", "hrace_3.0":"OtherRace"})

# get the ln value of wage and square value of age
data3['lnwage'] = np.log10(data3['hlabinc'])
data3['age_2'] = data3['age'] ** 2

# count the number of missing values for the independent variable
data3.isnull().sum()
data3 = data3.dropna(subset = ['hyrsed'])


# for t = 1971
data1971 = data3[data3['year'] == 1971]

def MLEreg(params):
    alpha, beta1, beta2, beta3, beta4, beta5, beta6 = params
#    for i in range(0, len(data1971)):
#        lnwage[i] = alpha + beta1 * hyrsed[i] + beta2 * age[i] + beta3 * age_2[i] + 
#                 beta4 * Black[i] + beta5 * Hispanic[i] + beta6 * OtherRace[i]
                 
    return alpha + beta1 * data1971['hyrsed'] + beta2 * data1971['age'] + beta3 * data1971['age_2'] + beta4 * data1971['Black'] + beta5 * data1971['Hispanic'] + beta6 * data1971['OtherRace']

initial_guess = [1, 1, 1, 1, 1, 1, 1]

result = opt.minimize(MLEreg, initial_guess)
if result.success:
    fitted_params = result.x
    print(fitted_params)
else:
    raise ValueError(result.message)
# I am sorry Professor, I got stuck here. I couldn't figure out how to write the code to estimate MLE.

# for the OLS regression
sm.OLS(data1971['lnwage'],data1971[['hyrsed','age', 'age_2', 'Black', 'Hispanic',
                                    'OtherRace']]).fit().summary()   

 
# call minimizer and use golden ratio search method.
#x_min = opt.minimize_scalar(MLEreg, args=params, method='Golden', options={'maxiter': 5000})
#print('The minimum of f(x) found numerically is ', x_min['x'])

# for t = 1980
# for t = 1990
# for t = 2000






