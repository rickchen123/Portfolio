

import pandas as pd
import numpy as np

def get_month(column):
    '''pass in a coulmn with timestamp type and return only the month'''
    mon = []
    for i in column:
        mon.append(i.month)
    return mon

def rsquared(x, y):
    """ Return R^2 where x and y are array-like."""
    n = len(x)
    r = (n*sum(x*y) - sum(x)*sum(y)) / np.sqrt((n*sum(x**2) - sum(x)**2)*(n*sum(y**2) - sum(y)**2) )
    
    return r**2

