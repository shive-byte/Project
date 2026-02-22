import pandas as pd
import datetime as dt
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("superstore.csv")

miss_val=['NA','',None,np.nan]
null=df.isin(miss_val)
if null.sum().sum()!=0:
    print("there are missing values in dataset")
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(null.head())

name_dict={}
#Ship Mode  Segment  Country  City  State   Postal Code 	Region
#Category	Sub-Category	Sales       Quantity
#Discount	Profit	   Name

for i in df['Name']:
    if i not in name_dict:
        name_dict[i]=1
    elif i in name_dict:
        name_dict[i]+=1
        
#best customers

best_cust=max(name_dict)
max_cust=df.loc[df['Profit']==max(df['Profit'])]
print(str(max_cust['Profit'].iloc[0]))
int_col=[]
str_col=[]
#profit per category,sub category,state,city chart
for i in df.head():
    if df[i].dtype=='int' or df[i].dtype=='float':
        int_col.append(i)
    else:
        str_col.append(i)
print("what kind of chart would u like?")
print("1.Pie\n2.line\n3.bar\n4.Area\n5.histogram")
cat_cols=[]
val_cols=[]
ch=int(input("Choose:"))
col_dict={}
if ch==1:
    print("A pie chart can only consist of 1 categorical column (data that is usually the names) and 1 integer column (the value to be plotted with)")
    ch1=int(input("\nhow many pie charts would u like to plot?:"))
    for i in range(ch1):
        print("for pie chart no.",i+1," what integer column would u like?")
        print(int_col)
        ch11=input("name:")
        val_cols.append(ch11)
        print("for pie chart no.",i+1," what categorical column would u like?")
        print(str_col)
        ch12=input("name:")
        cat_cols.append(ch12)
    
    
    inp='no'
    for i in range(len(cat_cols)):
        plot_dict={}
        new_plot={}
        for j in df[cat_cols[i]]:
            if j not in plot_dict:
                plot_dict[j]=(df[cat_cols[i]]==j).sum()
        
        if len(plot_dict)>50:
            print("Uh Oh the data size is too great would u like to have only top 50?")
            inp=input("")
                
            if inp=='yes':
                for j in range(50):
                    new_plot[max(plot_dict.keys(),key=plot_dict.get)]=max(plot_dict.values())
                    plot_dict.pop(max(plot_dict.keys(),key=plot_dict.get))
                new_plot['Others']=sum(plot_dict.values())
                inp='no'
        else:
            new_plot=plot_dict
        plt.pie(new_plot.values(),labels=new_plot.keys())
        plt.legend()
        plt.show()

elif ch==2:
    print("A line graph can consist of 1 categorical column (preferabbly date) and multiple integer columns (column that consists of the value)")
    ch2=int(input("no. of graphs"))
    for i in range(ch2):
        val_col2=[]
        print("for line chart no.",i+1,"what categroical column would u like to plot against?")
        print(str_col)
        ch21=input('name:')
        
        
        print("for line chart no.",i+1,"how many integer columns would u like?")
        print(int_col)
        k=int(input())
        for j in range(k):
            ch22=input("\nwhich integer column?:")
            val_col2.append(ch22)
        col_dict[ch21]=val_col2
        
    
    plot_list=[]
    for i in col_dict:
        for j in col_dict[i]:
            plot_dict={}
            for k in df[i]:
                if k not in plot_dict:
                    plot_dict[k]=(df[j][df[i]==k]).sum()
            plot_list.append(plot_dict)
    inp=''
    print(len(plot_list))
    for i in plot_list:
        if len(i)>50:
            print("the data is too large :/ \ndo u want only the top 50?")
            inp=input("")
            
    if inp=='yes':
        plot_list2=[]
        k=0
        for i in plot_list:
            print(max(i))
            print(i)
            dic={}
            for j in range(50):
                dic[max(i,key=i.get)]=max(i.values())
                plot_list[k].pop(max(i,key=i.get))
            plot_list2.append(dic)
            k+=1
        print(plot_list2)
        plot_list=plot_list2
        
    if ch2==1:
        for i in plot_list:
            plt.plot(i.keys(),i.values())
    
    else:
        print(plot_list)
        fig,ax=plt.subplots(ch2)
        m=0
        for i in plot_list:
            for j in plot_list:
                print(len(plot_list)) 
                if i.keys()==j.keys() and i!=j and len(i)!=0:
                    ax[m].plot(i.keys(),i.values())
                    ax[m].plot(i.keys(),j.values())
                    plot_list.remove(i)
                    plot_list.remove(j)
                    m+=1
    plt.legend()
    plt.show()
    
    
            
    
        
elif ch==3:
    print("a bar graph consists of 1 categorical column and multiple integer column")
    ch2=int(input("\nhow many bar graphs would u like?:"))
    for i in range(ch2):
        val_col2=[]
        print("for line chart no.",i+1,"what categroical column would u like to plot against?")
        print(str_col)
        ch21=input('name:')
        
        
        print("for line chart no.",i+1,"how many integer columns would u like?")
        print(int_col)
        k=int(input())
        for j in range(k):
            ch22=input("\nwhich integer column?:")
            val_col2.append(ch22)
        col_dict[ch21]=val_col2
        
    
    plot_list=[]
    for i in col_dict:
        for j in col_dict[i]:
            plot_dict={}
            for k in df[i]:
                if k not in plot_dict:
                    plot_dict[k]=(df[j][df[i]==k]).sum()
            plot_list.append(plot_dict)
    inp=''
    for i in plot_list:
        if len(i)>50:
            print("the data is too large :/ \ndo u want only the top 50?")
            inp=input("")
            if inp=='yes':
                pass
            else:
                break #return
    if inp=='yes':
        plot_list2=[]
        k=0
        for i in plot_list:
            print(max(i))
            dic={}
            for j in range(50):
                dic.update({max(i):i[max(i)]})
                plot_list[k].pop(max(i))
            plot_list2.append(dic)
            k+=1
        plot_list=plot_list2
        
    if ch2==1:
        for i in plot_list:
            plt.bar(i.keys(),i.values())
    else:
        fig,ax=plt.subplots(1,ch2)
        m=0
        for i in plot_list:
            for j in plot_list:
                print(len(plot_list))
                
                if i.keys()==j.keys() and i!=j and len(i)!=0:
                    ax[m].bar(i.keys(),i.values())
                    ax[m].bar(i.keys(),j.values())
                    
                    plot_list.remove(i)
                    plot_list.remove(j)
                    
                    m+=1
    plt.legend()
    plt.show()
elif ch==4:
    print("an area chart consists of 1 categorical column and multiple integer column")
    ch4=int(input("\nhow many area chart would u like?:"))
    for i in range(ch4):
        val_col2=[]
        print("for area chart no.",i+1,"what categorical column would u like?")
        print(cat_col)
        ch41=input('name:')
        print("for area chart no.",i+1,"how many integer columns would u like?")
        print(int_col)
        k=int(input('number:'))
        for j in range(k):
            ch42=input("which integer column?:")
            val_col2.append(ch42)
        col_dict[ch41]=val_dict
    for i in range(len(cat_cols)):
        plot_dict={}
        for j in df[cat_cols[i]]:
            if j not in plot_dict:
                plot_dict[j]=(df[cat_cols[i]]==j).sum()
        
        print(len(plot_dict)) 
        plt.pie(plot_dict.values(),labels=plot_dict.keys())
        plt.legend()
        plt.show()
elif ch==5:
    print("a histogram can only consist of 1 categorical column and 1 integer column")
    ch1=int(input("\nhow many historgams would u like to plot?:"))
    for i in range(ch1):
        print("for histogram no.",i+1," what integer column would u like?")
        print(int_col)
        ch11=input("name:")
        val_cols.append(ch11)
        print("for histogram no.",i+1," what categorical column would u like?")
        print(str_col)
        ch12=input("name:")
        cat_cols.append(ch12)
    for i in range(len(cat_cols)):
        plot_dict={}
        for j in df[cat_cols[i]]:
            if j not in plot_dict:
                plot_dict[j]=(df[cat_cols[i]]==j).sum()
        
        print(len(plot_dict)) 
        plt.pie(plot_dict.values(),labels=plot_dict.keys())
        plt.legend()
        plt.show()
else:
    print("invalid input")
   

