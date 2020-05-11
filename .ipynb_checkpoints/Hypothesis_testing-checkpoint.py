import numpy as np
import scipy
from scipy import stats
import pandas as pd 


netflix_df= pd.read_csv("netflix.csv")
print(netflix_df.head(20))
con_a= netflix_df["A"]
con_b= netflix_df["B"]
#F-test to determine whether the variances are equal or not to choose between Student's or Welch's version of t-test
F=np.var(con_a)/np.var(con_b)
print("F",F)
df1= len(con_a)-1
df2=len(con_b)-1
p_value= scipy.stats.f.cdf(F,df1,df2)
print("p-value_variance",p_value)
