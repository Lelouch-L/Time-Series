import numpy as np
import pandas as pd
import sys
import os
import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels.tsa.api as smt
import matplotlib.pylab as plt
import seaborn as sns
pd.set_option('display.width',1000)
pd.set_option('display.max_rows',1000)
pd.set_option('display.max_columns',500)
pd.set_option('display.float_format',lambda x: '%.5f' % x)
np.set_printoptions(precision=5,suppress=True)
sns.set(style='ticks',context='poster')
Sentiment = 'data/sentiment.csv'
Sentiment = pd.read_csv(Sentiment, index_col=0, parse_dates=[0])