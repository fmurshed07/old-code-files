from configparser import ConfigParser
# # parser = ConfigParser()
# # print(dir(parser))

def dbcreds(filename = "config.ini" , section = "mysql"):
	db = {}
	parser = ConfigParser()
	data = parser.read(filename)
	# print(data)
	if parser.has_section(section):
		items = parser.items(section)
		# print(items)
		for item in items:
			db[item[0]] = item[1]
	return db