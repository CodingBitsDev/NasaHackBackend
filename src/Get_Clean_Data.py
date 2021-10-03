#!/usr/bin/env python
# coding: utf-8

# In[16]:


import os
import glob
import json
import sys


# In[13]:


path = "../data/"
files = []

for file in os.listdir(path):
    if file.endswith(".json"):
        files.append(os.path.join(path, file))


# In[35]:


entries_to_remove = ('CCSDS_OMM_VERS', 'COMMENT', 'ORIGINATOR', 'CENTER_NAME', 'REF_FRAME', 'TIME_SYSTEM',\
                    'MEAN_ELEMENT_THEORY', 'MEAN_MOTION', 'ECCENTRICITY', 'INCLINATION', 'RA_OF_ASC_NODE',\
                    'ARG_OF_PERICENTER', 'MEAN_ANOMALY', 'EPHEMERIS_TYPE', 'CLASSIFICATION_TYPE', 'NORAD_CAT_ID',\
                    'ELEMENT_SET_NO', 'REV_AT_EPOCH', 'BSTAR', 'MEAN_MOTION_DOT', 'MEAN_MOTION_DDOT',\
                    'SEMIMAJOR_AXIS', 'PERIOD', 'APOAPSIS', 'PERIAPSIS', 'OBJECT_TYPE', 'RCS_SIZE', 'COUNTRY_CODE',\
                    'LAUNCH_DATE', 'SITE', 'DECAY_DATE', 'GP_ID')

for file in files:
    print(f'Cleaning {file}')
    with open(file, 'r') as json_file:
        data = json.load(json_file)                
        
        for l in range(0, len(data)): 
            for k in entries_to_remove:
                try:
                    if k in data[l].keys():
                        del data[l][k]
                except:
                    continue
            
    with open(file, 'w') as f:
        json.dump(data, f)    
                
                


# In[32]:


#data[0].keys()


# In[ ]:


url = 'https://www.space-track.org/basicspacedata/query/class/boxscore/format/csv'

