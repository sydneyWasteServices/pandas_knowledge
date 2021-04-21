import pandas as pd 
import numpy as np


data_left = {'key' : ['1','2','3','4','5'], 'value' : ['a','b','c','d','e'] }
df_left = pd.DataFrame(data_left)
data_right = {'key' : ['1','2','3','4'], 'value' : ['a','b','c','d'] }
df_right = pd.DataFrame(data_right)

# left_on  and right_on  => for two different index name but want to merge by those key
# on => both has same key 
# how -> similar to sql join => left => encompass all left
#  how -> similar to sql join => right => encompass all right

pd.merge(df_left, df_right, on=['key'], how='inner')

