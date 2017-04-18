# UPDATE THIS VARIABLE
mapping = { "St.": "Street",
            "Ave" : "Avenue",
            "Rd." : "Road"
            }

wrong_street=[u"路“，u"道”，“徑”]

def update_chinese_st(street_name):
	wrong_street =[u"台北市“，u"南港区”]
	for target in wrong_street:
		street_name = re.sub(target,"",street_name)
	return street_name

for event, element in enumerate(get_element(file_in)):
	if element.tag=='node':
		for tag in elem.iter('tag'):
			if tag.attrib['k']=='addr:street':
				street_name=tag.attrib['v']
				better = update_chinese_st(street_name)
				if better != street_name:
					print tag.attrib['v'], "=> ", better

