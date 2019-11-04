# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import pandas as pd
import json
import sys
import re
from datetime import datetime

def readConfig():
    with open('config.json') as config_file:
        data = json.load(config_file)
    event = data['event']
    url = data['url']
    return event, url

def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)

def get_class( kls ):
    parts = kls.split('.')
    module = ".".join(parts[:-1])
    m = __import__( module )
    for comp in parts[1:]:
        m = getattr(m, comp)            
    return m
    

class EventZurich:
        def getEvents(self, url):
            page_response = requests.get(url, timeout=5)
            soup = BeautifulSoup(page_response.content,'html.parser')
            table = soup.find_all('table')[0] 
            df = pd.read_html(str(table))[0].iloc[0:20,1:4]
            dates = obj.extractDate(df)
            print(type(df))
            print(df)
            return(df,dates)
            
        def extractDate(self,df):
            print(df.iloc[1,0])
            #match = re.search(r'\d{2}.\d{2}.\d{4}', df.iloc[1,0])
            #date = datetime.strptime(match.group(), '%d.%m.%Y').date()
            return(df)
            





event, url = readConfig()


constructor = globals()[event]
obj = constructor()
new_df,dates = obj.getEvents(url)
print(dates)





            