#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Task: Clean
- update_cityname
- update_phone
_ update_street

"""
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint



# Update cityname -------------- start ----------------------------------

# Create list for Hong Kong regions, districts
regions = ['Islands', 'Kowloon', 'New Territories']
districts = ['Islands', 'Kwai Tsing', 'North', 'Sai Kung',
            'Sha Tin', 'Tai Po', 'Tsuen Wan', 'Tuen Mun',
            'Yuen Long', 'Kowloon City', 'Kwun Tong',
            'Sham Shui Po', 'Wong Tai Sin', 'Yau Tsim Mong',
            'Central', 'Western', 'Eastern','Southern', 
            'Wan Chai']
neighborhoods = ['Ta Kwu Ling', 'Hung Hom','Tsuen Wan','Mui Wo','Fo Tan']
combine = regions + districts + neighborhoods

# Create regular expression
# Join array elements with "|" as glue
subcity = re.compile('|'.join(combine))

def update_cityname(cityname):	
    m=subcity.search(cityname)
    if m:
        cityname=u'香港 Hong Kong'
    else:
        cityname=cityname
    return cityname

# Update cityname -------------- end ---------------------------

# Update phone ----------------start------------------
def update_phone(phone):
    if re.compile(r'^(\d{8})$').search(phone):
        phone = '+852'+' '+phone[0:4]+' '+phone[4:]
    elif re.compile(r'^\+852\s(\d{8})$').search(phone):
        phone = phone[0:9]+' '+phone[9:]
    else:
        phone=phone
    return phone
# Update phone ---------------- end ------------------




# Update street ----------------start------------------

mapping = { u"路": "Road",
            u"徑" : "Path",
            u"道" : "Road",
            }
def update_street(name):	
    for target in mapping.keys():
        if target in name:
            name = name+' '+mapping[target]
        else:
            name=name
    return name

# Update street ----------------end-----------------


