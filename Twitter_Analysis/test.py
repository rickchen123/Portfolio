from p3funcs import *
import pandas as pd
import numpy as np
import numpy.testing as npt
from datetime import datetime
import warnings

def test_monthvalue():
	date = ['01/20/2017', '10/24/2017']
	new_date = [datetime.strptime(date[i], '%m/%d/%Y') for i in range(len(date))]
	obs = get_month(new_date)
	exp = [1,10]
	assert obs == exp

def test_rsquared():
	x = np.array(1,2,3,4,5)
	y = np.array(1,2,3,4,5)
	assert rsquared([1]) == 1

def test_ints():
	x = np.array(1,2,3,4,6)
	y = np.array(1,2,3,4,5)
	obs = rsquared(num_list)
	exp = 1
	assert obs == exp
