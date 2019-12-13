# config.ini <-- take

# data --> config.ini 
from configparser import ConfigParser 

def getdbdetails(filename= "config.ini", sectionname="mysql1"):
	dbdict = {}
	# parser object 
	parser = ConfigParser()
	data = parser.read(filename)
	# print(data)
	if parser.has_section(sectionname):
		items = parser.items(sectionname)
		# print(items)
		for item in items:
			dbdict[item[0]] = item[1]
	# print(dbdict)
	return dbdict

# getdbdetails("config.ini","mysql1")

# dict --> gives