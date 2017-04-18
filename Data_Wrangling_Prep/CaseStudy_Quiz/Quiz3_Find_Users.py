# Quiz 3: Find Unique users who contributed to the map

# Output: return a list of unique users IDs ("uid")


import xml.etree.cElementTree as ET
import pprint
import re

def get_user(element):
    return


def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        if 'uid' in element.attrib:
            users.update([element.attrib['uid']])
        pass

    return users