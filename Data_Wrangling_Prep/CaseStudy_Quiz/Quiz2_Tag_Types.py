# Quiz 2: Tag Types
# Goal: Check "k" value for each "<tag>" to identify any potential problems

import xml.etree.ElementTree as ElementTree
import pprint
import re

# Below 3 regular expressions help to identify
#1 "lower": tags that contain only lowercase letters,
#2 "lower_colon": tags with a colon in their names,
#3 "problemchars": tags with problematic characters, and
#4 "other": for other tags that do not fall into the other three categories.

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

# Assign key types
def key_type(element, keys):
    if element.tag == "tag":
        for tag in element.iter('tag'):
            if lower.search(tag.get('k')):
                keys['lower'] += 1
            elif lower_colon.search(tag.get('k')):
                keys['lower_colon'] += 1
            elif problemchars.search(tag.get('k')):
                keys['problemchars'] += 1
            else:
                keys['other'] += 1
        pass
        
    return keys

def process_map(filename):
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    for _, element in ET.iterparse(filename):
        keys = key_type(element, keys)

    return keys

def test():
    # You can use another testfile 'map.osm' to look at your solution
    # Note that the assertion below will be incorrect then.
    # Note as well that the test function here is only used in the Test Run;
    # when you submit, your code will be checked against a different dataset.
    keys = process_map('example.osm')
    pprint.pprint(keys)
    assert keys == {'lower': 5, 'lower_colon': 0, 'other': 1, 'problemchars': 1}


if __name__ == "__main__":
    test()

