#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import requests
import sys
import json
import re
import time
import urllib.request
import re
from datetime import timezone
from dateutil.parser import parse


# In[2]:


url = 'http://celestrak.com/NORAD/elements/'
resp = requests.get(url)

# TODO parse date
date = re.findall(r'(?<=<h3 class=center>Current as of ).+?(?=</h3>)', resp.text)

# TODO use crawled data
debris_urls = [ 'http://celestrak.com/NORAD/elements/2019-006.txt',       'http://celestrak.com/NORAD/elements/1999-025.txt', 'http://celestrak.com/NORAD/elements/iridium-33-debris.txt',        'http://celestrak.com/NORAD/elements/cosmos-2251-debris.txt']

satelite_urls = ['http://celestrak.com/NORAD/elements/tle-new.txt', 'http://celestrak.com/NORAD/elements/stations.txt',       'http://celestrak.com/NORAD/elements/visual.txt', 'http://celestrak.com/NORAD/elements/active.txt',
       'http://celestrak.com/NORAD/elements/analyst.txt']


# In[3]:


data_json = {}
satelites = []
tle1s = []
tle2s = []


for url in debris_urls:
    with urllib.request.urlopen(url) as f:
        html = f.read().decode('utf-8')
    html_lines = html.splitlines()
    
    for i in range(0, len(html_lines), 3):
        satelites.append(html_lines[i])
        tle1s.append(html_lines[i+1])
        tle2s.append(html_lines[i+2])


# In[5]:


if len(satelites) == len(tle1s) == len(tle2s):
    for i in range(0, len(satelites)):
        name = re.findall('(?<=2 )\d+', tle2s[i], flags=0)[0]
        # get unix date
        unix_date = re.findall('.+(?= UTC)', date[0], flags=0)[0]
        unix_date = parse(unix_date)
        unix_date = unix_date.replace(tzinfo=timezone.utc).timestamp()
        
        data_json[str(i)] = {'name': name, 'date': unix_date, 'satelite': satelites[i], 'tle1':tle1s[i], 'tle2':tle2s[i]}


# In[6]:


with open('data_CelesTrak.json', 'w') as f:
    json.dump(data_json, f)   


# In[ ]:





# In[ ]:





# In[ ]:




