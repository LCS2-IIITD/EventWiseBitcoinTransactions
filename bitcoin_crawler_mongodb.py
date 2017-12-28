
import requests
import pymongo
from pymongo import MongoClient
import json

 
# setting connection with local database
client = MongoClient('localhost',27017, maxPoolSize=200)
db=client.wannacry.transac_data

# bitcoin addresses list 
alladdr = ['12t9YDPgwueZ9NyMgw519p7AA8isjr6SMw','13AM4VW2dhxYgXeQepoHkHSQuy6NgaEb94','115p7UMMngoj1pMvkpHijcRdfJNXj6LrLn']
block_explorer_url  = "https://blockexplorer.com/api/addrs/"


# transaction crawler
for add in alladdr:
    
    transactions = []
    from_number  = 0
    to_number    = 50

    block_explorer_url_full = block_explorer_url + add + "/txs?from=%d&to=%d" % (from_number,to_number)

    response = requests.get(block_explorer_url_full)

    try:
        results  = response.json()
    except:
        print ("[!] Error retrieving bitcoin transactions. Please re-run this script.")
        

    if results['totalItems'] == 0:
        print ("[*] No transactions for %s" % bitcoin_address)
        

    transactions.extend(results['items'])

    while len(transactions) < results['totalItems']:

        from_number += 50
        to_number   += 50

        block_explorer_url_full = block_explorer_url + add + "/txs?from=%d&to=%d" % (from_number,to_number)

        response = requests.get(block_explorer_url_full)

        results  = response.json()        

        transactions.extend(results['items'])

    print ("[*] Retrieved %d bitcoin transactions." % len(transactions))
    db.insert_many(transactions)

