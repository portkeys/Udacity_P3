#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Task: Audtit 
- audit_cityname
- audit_phone
_ audit_zipcode
_ audit_street

"""
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "sample.osm"

# Audit city name
def audit_cityname(OSMFILE):
    city = set()
    for event, elem in ET.iterparse(OSMFILE):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if tag.attrib['k'] == "addr:city" or tag.attrib['k']=="cityname":
                    city.add(tag.attrib['v'])
    return(city)

# Audit phone
def audit_phone(OSMFILE):
    phone_list = []
    for event, elem in ET.iterparse(OSMFILE):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if tag.attrib['k'] == "phone":
                    phone_list.append(tag.attrib['v'])
                    
    return(phone_list)

# Audit zipcode
def audit_zipcode(OSMFILE):
    post_list = []
    for event, elem in ET.iterparse(OSMFILE):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if tag.attrib['k'] == "addr:postcode":
                    post_list.append(tag.attrib['v'])
    return(post_list)

# Audit Street names ------start----
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

expected= ["Street", "Avenue", "Road", "Boulevard", "Drive", 
           "Lane", "Path", "Trail", "Parkway",
           "Central","East", "West", "North", "South"]

def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")
    
def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)
def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    osm_file.close()
    return street_types


# Audit Street names ------end----










