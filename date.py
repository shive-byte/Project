import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv(r"C:\Users\lenovo\OneDrive\Documents\churn data analysis\superstore.csv")
#l3=[]
#df2={}
#df3={}
#l=[]
#l2=[]
#num_cols=['Profit','Sales']
#for j in num_cols:
#    for i in df['City']:

#        grouped=df[df['City']==i]
        
#        k=grouped[j].sum()
        
#        df2[i]=k
#    l3.append(df2)
#    df2={}

    

#df3['City']=l3[0].keys()

#for i,j in enumerate(l3):
    
#    df3[num_cols[i]]=j.values()


#print(pd.DataFrame(df3))
dict1={1:3,2:4}
for i in dict1.values():
    print(i)
