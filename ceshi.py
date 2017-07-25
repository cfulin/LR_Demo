import pandas as pd
import numpy as np
from pandas import Series, DataFrame

ser = Series(np.arange(3.))

data = DataFrame(np.arange(16).reshape(4, 4), index=list('abcd'), columns=list('wxyz'))

data['w']

data[['w']]
data.head(2)
data.tail(2)

print data.iloc[1]
