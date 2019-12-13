from configparser import ConfigParser

def getDict(filename="dbconfig.ini",sectionname="mysql1"):
	parser = ConfigParser()
	data = parser.read(filename)
	creds = {}
	if parser.has_section(sectionname):
		items = parser.items(sectionname)
		# print(items)
		for i in items:
			creds[i[0]] = i[1]
	return creds
# print(getDict())