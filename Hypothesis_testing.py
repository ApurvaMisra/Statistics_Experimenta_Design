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
print("p-value_variance for F test",p_value )

#Welch's t-test, set "equal_var" argument as False in scipy.stats.ttest_ind
stat_t=scipy.stats.ttest_ind(con_a, con_b, axis=0, equal_var=False)
print("p-value_variance for Welch's t-test",stat_t )
#Since p_value/2<alpha t<0 => mean(con_a)<mean(con_b)
#con_a=DVD tab first
#con_b=streaming tab first




########Difference between average weekly streaming hours
con_a_sum=np.sum(con_a)/len(con_a)
con_b_sum=np.sum(con_b)/len(con_b)
print("difference", con_a_sum-con_b_sum)
