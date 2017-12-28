
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
