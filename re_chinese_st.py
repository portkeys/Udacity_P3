# regular expression

import re
string = u'油画路 polyline road'
pattern = re.compile(u'[路道径]')
m=pattern.search(string)
if m:
    street_ch=m.group()
    print(street_ch)

#----------
street_type_eng=re.compile(r'\b\S+\.?$', re.I)
expected_eng = ["Street", "Avenue"]

street_type_ch=re.compile(ur'[\u4e00-\u9fff]+')
expected_ch=[u"路", u"道", u"径"]

street_name = "还旁路"

def audit_street_ch(street_types, street_name):
	m=street_type_ch.search(street_name)
	if m:
		street_type = m.group()
		if street_type not in expected:
			street_type[street_type].add(street_name)
	return street_type


