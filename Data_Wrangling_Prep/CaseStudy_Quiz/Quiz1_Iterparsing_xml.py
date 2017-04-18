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


