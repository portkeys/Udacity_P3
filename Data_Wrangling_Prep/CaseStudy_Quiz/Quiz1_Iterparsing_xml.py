# Quiz 1: Iterative Parsing
# Goal: iterative parsing xml file to find top-level tags and their count
# Output: dictionary including tag name as key, and tag count as value.

import xml.etree.ElementTree as ET
import pprint
from Collections import Counter

def count_tags(filename):
	taglist=[]
	tagdict={}
	for event, element in ET.iterparse(filename):
		if event=='end':
			taglist.append(element.tag)
	tagdict=DICT(Counter(taglist))
	return tagdict

def test():

    tags = count_tags('example.osm')
    pprint.pprint(tags)
    assert tags == {'bounds': 1,
                     'member': 3,
                     'nd': 4,
                     'node': 20,
                     'osm': 1,
                     'relation': 1,
                     'tag': 7,
                     'way': 1}

    

if __name__ == "__main__":
    test()
