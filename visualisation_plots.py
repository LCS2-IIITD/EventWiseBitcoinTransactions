import requests
import pymongo
from pymongo import MongoClient
import json



client = MongoClient('localhost',27017)
db=client.cryptolocker.cryptotransac_data

df=pd.DataFrame(list(db.find({})))

import datetime

date=[]
for i in df['time']:
    #print(datetime.datetime.fromtimestamp(int(i)).strftime('%Y-%m-%d '))
    date.append(datetime.datetime.utcfromtimestamp(int(i)).strftime('%Y-%m-%d '))
df['date']=date

time=[]
for i in df['time']:
    #print(datetime.datetime.fromtimestamp(int(i)).strftime('%H:%M:%S'))
    time.append(datetime.datetime.utcfromtimestamp(int(i)).strftime('%H:%M:%S'))
df['real_time']=time


hour=[]
for i in df['time']:
    #print(datetime.datetime.fromtimestamp(int(i)).strftime('%H'))
    hour.append(datetime.datetime.utcfromtimestamp(int(i)).strftime('%H'))
df['hour']=hour

df['hour'] = df['hour'].apply(pd.to_numeric)

list_add=['1EmLLj8peW292zR2VvumYPPa9wLcK4CPK1','19DyWHtgLgDKgEeoKjfpCJJ9WU8SQ3gr27','15sJ3pT7J6zefRs95SEsfBZMz8jAw1zAbh','1HrEqMHQVWhKuCg7a3rxo2tAFAiKquJ5iP'
         ,'18iEz617DoDp8CNQUyyrjCcC7XCGDf5SVb','1AEoiHY23fbBn8QiJ5y6oAjrhRY1Fb85uc','1KP72fBmh3XBRfuJDMn53APaqM6iMRspCh'] 
l1=len(df['vout'])
val=[]
for i in range(l1):
    l2=len(df['vout'][i])
    summ=0
    for j in range(l2):
        try:
            
            if df['vout'][i][j]['scriptPubKey']['addresses'][0] in list_add:
                summ=summ+float(df['vout'][i][j]['value'])
        except:
            pass
    val.append(summ)
    print(val)     
                   
            

df['transaction_input']=val
df.describe()


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import pylab as pl

x = df['time']
xTicks = df['date']
y = df['transaction_input']
pl.xticks(x, xTicks, rotation=45) #writes strings with 45 degree angle
pl.xlabel('Date')
pl.ylabel('value recieved in BTC')
plt.title('(Amount Recieved vs Date) for cryptolocker')
pl.plot(x,y,'go')
fig = plt.gcf()
fig.set_size_inches(19, 8)
fig.savefig('graphc1.png', dpi=100)


x = df['hour']
y = df['transaction_input']
plt.xlabel('Time in hrs')
plt.ylabel('value recieved in BTC')
plt.title('(Amount Recieved vs Time) for cryptolocker')
plt.plot(x,y,'g^')
fig = plt.gcf()
fig.set_size_inches(7, 3.5)
fig.savefig('graphc2.png', dpi=80)

sns.distplot(df['transaction_input'],axlabel="amount recieved in BTC",rug=True,kde=False,color="g")
fig = plt.gcf()
fig.set_size_inches(10, 5)
fig.savefig('graphc3.png', dpi=100)

