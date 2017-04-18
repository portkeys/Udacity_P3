#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Use the iterative parsing to process the map file and
find out what tags are there, and how many, to get the
feeling on how much of which data you can expect to have in the map.

The count_tags function. It should return a dictionary with the 
tag name as the key and number of times this tag can be encountered in 
the map as value.

"""
import xml.etree.cElementTree as ET
import pprint
from collections import Counter

def count_tags(filename):
        # My code
    taglist=[]
    tagdict={}
    for event, element in ET.iterparse(filename):
        if event=='end':
            taglist.append(element.tag)
    tagdict=dict(Counter(taglist))
    return tagdict


