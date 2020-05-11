import numpy as np
import scipy
from scipy import stats
import pandas as pd 


spotify_df= pd.read_csv("spotify.csv")
print(spotify_df.head(10))
con_a=spotify_df["A"]
con_b=spotify_df["B"]

#F-test to determine whether the variances are equal or not to choose between Student's or Welch's version of t-test
F=np.var(con_a)/np.var(con_b)
print("F",F)
df1= len(con_a)-1
df2=len(con_b)-1
p_value= scipy.stats.f.cdf(F,df1,df2)
print("p-value_variance for F test",p_value )

#Student's t-test
stat_t=scipy.stats.ttest_ind(con_a, con_b, axis=0, equal_var=True)
print("p-value_variance for Student's t-test",stat_t )

#There is no difference