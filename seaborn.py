import numpy as np
import pandas as pd
import seaborn as sns

df=pd.read_csv("https://raw.githubusercontent.com/Premalatha-success/HHE_14th-Aug//main/loan_prediction.csv")

df.head()
     
df.dtypes

sns.relplot(x="Views",y="Upvotes",data=df)

sns.relplot(x="Views" , y="Upvotes" , hue="tag" , data=df)
     
