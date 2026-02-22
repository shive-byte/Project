import pandas as pd
import matplotlib.pyplot as plt


int_col=[]
str_col=[]

def checknull():
    if df.isnull==True:
        print("there are null values in dataset, would u like to change them or have them handled")
        inpu=input("enter yoru choice y/n :")
        if inpu=='y':
            df.fillna
        else:
            pass
    else:
        print("goodjob")

def check_col():
    if len(str_col)==0 or len(int_col)==0:
        for i in list(df.columns.values):
            
        
            if pd.api.types.is_numeric_dtype(df[i]):
                int_col.append(i)
            else:
                str_col.append(i)
    print('the int columns are:',int_col)
    print('\n the string columns are:',str_col)
    inp=input("are these right or would u like to change a column to a different datatype?y/n")
    if inp=='n':
        chc=input('convert integer to string or string to integer?1/2')
        if chc=='1':
            print(int_col)
            chc1=input("which column?")
            df[chc1]=df[chc1].astype('str')
            int_col.remove(chc1)
            str_col.append(chc1)
            print(str_col)
        else:
            print(str_col)
            chc1=input("which column?")
            try:
                df[chc1]=df[chc1].astype('int64')
            except:
                print("oops this cannot be converted")
            str_col.remove(chc1)
            int_col.append(chc1)
            print(int_col)


def data():
    c=r"C:\Users\lenovo\OneDrive\Documents\churn data analysis\superstore.csv"
    global df
    df=pd.read_csv(c)
    global col
    col=df.columns
    print("these are the columns of the dataset")
    print(col)
    inp=input("is it ? y/n :")
    if inp=='y':
        pass
    else:
        print("add the columns of your dataset to the top and try again")
        data()
    
def inconsistencies():
    global count,in_count,col_type
    for i in col:
        count=0
        in_count=0
        col_type=None
        incon_list=[]
        m=1
        for j in df[i]:
            if m==1:
                m+=1
                continue
            if count==0:
                col_type=type(j)
            if type(j)==col_type:
                count+=1
            elif type(j)!=col_type:
                in_count+=1
                if type(j) not in incon_list:
                    incon_list.append(type(j))
            
        in_dict[i]=in_count        
        final_list.append(incon_list)
    m=0
    for i in in_dict.keys():
        if in_dict[i]!=0:
            print("column",i," has ",in_dict[i]," inconsistent values")
            print("the inconsistencies are of the following type")
            print(final_list[m])
        m+=1

def fix_incon():
    conv_list={}
    m=0
    for i in in_dict.keys():
        if in_dict[i]!=0:
            print("column",i,"has inconsistencies of following datatypes")
            print(final_list[m])
            inp=input("which of the following datatypes do u want to convert the column to \n note that float is the same as integer but has decimal value")
            conv_list[i]=inp
        m+=1
    
    try:
        global df
        df=df.astype(conv_list)
        print("succesfully converted")
    except TypeError:
        print("column could not be converted to specific type try again")
        fix_incon()

def max_min():
    max=0
    
    inp2=input("which numerical/integer column would u like to check the max of? ex: Profit/Sales")
    max=df[df[inp2]==df[inp2].max()]
    print("this is the max ",inp2,":\n", max)
    min=df[df[inp2]==df[inp2].min()]
    print("this is the min ",inp2,":\n", min)

    inp1=input("which categorical column would u like to check with previosuly mentioned integer column?")
    grouped=df.groupby(inp1)
    max=grouped[inp2].sum()[grouped[inp2].sum()==grouped[inp2].sum().max()]
    print("this is the max ",inp2,"based on ",inp1,":\n",max)
    min=grouped[inp2].sum()[grouped[inp2].sum()==grouped[inp2].sum().min()]
    print("this is the max ",inp2,"based on ",inp1,":\n",min)

def summarize(inp1,inp2):
    
    l3=[]
    df2={}
    df3={}
    l=[]
    l2=[]
    num_cols=inp2
    for j in num_cols:
        for i in df[inp1]:
            grouped=df[df[inp1]==i]
            k=grouped[j].sum()
            df2[i]=k
        l3.append(df2)
        df2={}
    df3[inp1]=l3[0].keys()
    for i,j in enumerate(l3):
        df3[num_cols[i]]=j.values()
    return pd.DataFrame(df3)


def line():
    print(col)
    num_col=[]
    inp1=int(input("how many numerical valued column would u like to plot with?"))
    for i in range(inp1):
        inp11=input("which column would u like to plot?")
        num_col.append(inp11)
    inp2=input("which categorical column would u like to choose to plot against Ex:Name/Date")
    df.plot(x=inp2,y=num_col)
    plt.show()
    return

def bar():
    print(col)
    num_col=[]
    inp1=int(input("how many numerical valued column would u like to plot with?"))
    for i in range(inp1):
        inp11=input("which column would u like to plot?")
        num_col.append(inp11)
    inp2=input("which categorical column would u like to choose to plot against Ex:Name/Date")
    df_temp=summarize(inp2,num_col)
    df_temp.plot.bar(x=inp2,y=num_col)
    plt.show() 
    return
def pie():
    print(col)

    inp1=input("which numerical column would u like to choose to plot with? Ex Profit/age:")
    inp2=input("which categorical column would u like to choose to plot against Ex:Name/Date:")
    num_col=[inp1]
    df_temp=summarize(inp2,num_col)
    df_temp.index=df_temp[inp2]
    df_temp.plot.pie(y=inp1)
    plt.show()
    return
    
def hist():
    print(col)
    inp1=input("which numerical column would u like to choose to plot with? Ex Profit/age:")
    inp2=input("which categorical column would u like to choose to plot against Ex:Name/Date:")
    df.plot.hist(x=inp2,y=inp1)
    plt.show()
    return

def area():
    print(col)
    num_col=[]
    print("NOTE: the numerical columns must not contain any negative values")
    inp1=int(input("how many numerical valued column would u like to plot with?"))
    for i in range(inp1):
        inp11=input("which column would u like to plot?")
        num_col.append(inp11)
    inp2=input("which categorical column would u like to choose to plot against Ex:Name/Date")
    df_temp=summarize(inp2,num_col)
    df_temp.plot.area(x=inp2,y=num_col)
    plt.show() 
    return

data()



#check for missing values
ch1=input("would u like to check for any missing values? y/n :")
if ch1=='y':
    checknull()

#check inconsitent data values, int and string in a column
final_list=[]
in_dict={}
incon_list=[]
count=0
in_count=0
col_type=None
ch2=input("would u like to check for inconsitencies? y/n")
if ch2=='y':
    inconsistencies()

#check each column dtype
check_col()

#fix inconsistencies
for i in in_dict:
    if in_dict[i]!=0:
        ch3=input("would u like to fix these inconsistent datatype in column",i)
        if ch3=='y':
            fix_incon()
            break
        else:
            break

#finding max & min
grouped=None
ch4=input("would u like to find out max profit/sales based on a specific category? y/n")
if ch4=='y':
    print("\n",col)
    
    max_min()


#plotting
ch5=input("welcome to plotting y/n:")
if ch5=='y':
    charts=['line','scatter','bar','histogram','pie','area']
    print(charts)
    inp=input("which of the charts do u want to plot?")
    if inp==charts[0]:
        line()
    elif inp==charts[1]:
        scatter()
    elif inp==charts[2]:
        bar()
    elif inp==charts[3]:
        hist()
    elif inp==charts[4]:
        pie()
    elif inp==charts[5]:
        area()