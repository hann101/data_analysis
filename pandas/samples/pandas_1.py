import pandas as pd
from pandas import Series, DataFrame

sdata = {'Ohio':35000, 'Texas':71000, 'Oregon':16000, 'Utah':5000}
obj3 = pd.Series(sdata)
print(obj3)