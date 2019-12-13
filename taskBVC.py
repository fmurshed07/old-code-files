tags = ['B', 'O', 'O', 'O', 'O', 'B', 'B', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',  'B', 'O', 'B', 'O','O', 'B', 'O', 'B', 'B', 'B', 'O', 'B', 'B', 'B', 'O', 'O', 'O', 'B', 'B', 'B', 'B', 'O', 'B', 'O', 'B', 'O', 'B', 'B', 'O', 'O', 'B', 'B']

Sentence = "TNS is looking for a Sr software developer to join a team that is responsible for the development and maintenance of the TNSOnline and MMIS web portals. The TNS web portal is used by internal and external customers to monitor and report on transactions processed through the TNS network."

entities = ["TNS", "Sr software developer", "development", "maintenance", "TNSOnline", "MMIS web portals", "TNS web portal", "internal and external customers", "monitor", "report", "transactions processed", "TNS network"]









# st = Sentence.split()
# o=[]
# c=0
# # j=-1
# for i in range(len(tags)):
# 	if(tags[i]=='O'):
# 		c=0
# 	elif(tags[i]=="B" and c == 0):
# 		c=c+1
# 		o.append(st[i])
# 		# j=j+1
# 	else:
# 		# o[j]=o[j]+" "+st[i]
# 		o[len(o)-1]=o[len(o)-1]+" "+st[i]
# 		# if len(o) == 0 :
# 		# 	o.append(" "+st[i])
# 		# else:
# 		# 	o[len(o)-1]=o[len(o)-1]+" "+st[i]
# print(o)

# # print(len(tags))
# # print(len(Sentence.split()))

# # op =[]

# # for i in range(1,len(tags)-1):
# # 	ans = ""
# # 	if tags[i-1] != "B" and tags[i] == "B" and tags[i+1] != "B":
# # 		ans = ans + Sentence.split()[i]
# # 		op.append(ans)
# # print(op)

# # import json
# # with open('demo.json', 'r') as f:
# #     distros_dict = json.load(f)

# # print(distros_dict)
# # for i in distros_dict.values():
# # 	print(i)
# # 	print

# # # for distro in distros_dict:
# # #     print(distro['java'])

# # # import json
# # # input_file=open('demo.json', 'r')
# # # # output_file=open('test.json', 'w')
# # # json_decode=json.load(input_file)
# # # for item in json_decode:
# # #     my_dict={}
# # #     my_dict['title']=item.get('labels').get('en').get('value')
# # #     my_dict['description']=item.get('descriptions').get('en').get('value')
# # #     my_dict['id']=item.get('id')
# # #     print my_dict

# # # result = []
# # # for item in json_decode.items():
# # #     my_dict={}
# # #     my_dict['title']=item.get('labels').get('en').get('value')
# # #     my_dict['description']=item.get('descriptions').get('en').get('value')
# # #     my_dict['id']=item.get('id')
# # #     print(my_dict)
# # #     result.append(my_dict)

# # import rhinoscriptsyntax as rs
# import json

# with open('demo.json', 'r') as f:
#         datastore = json.load(f)
# # print datastore["canonicals"]["parent_skills"][0]["child"]["skills"]
# # print datastore["canonicals"]["parent_skills"][0]["child"]["count"]
# # print(len(datastore["canonicals"]["parent_skills"]))

# allTech = []
# allCount = []
# op = {}
# for i in range(8):
# 	sname = ""
# 	scount = 0
# 	slist = datastore["canonicals"]["parent_skills"][i]["child"]["skills"]
# 	scounts = datastore["canonicals"]["parent_skills"][i]["child"]["count"]
	
# 	print(len(slist),len(scounts))
# 	# for ele in slist:
# 	# 	allTech.append(ele.lower())
# 	# for ele in scounts:
# 	# 	allCount.append(ele)

# 	# for i in range(len(slist)):
# 	# 	op[slist[i]] = scounts[i]
# 	# 	print(slist[i])
# 	# 	print(scounts[i])


# # print(len(set(allTech)))
# # print(op)
# # print(len(allTech))
# # print(len(allCount))


# x=[2,3,4,7,5,8,6,3,4,7,2,3,4]

# tags = ['B', 'O', 'O', 'O', 'O', 'B', 'B', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',  'B', 'O', 'B', 'O','O', 'B', 'O', 'B', 'B', 'B', 'O', 'B', 'B', 'B', 'O', 'O', 'O', 'B', 'B', 'B', 'B', 'O', 'B', 'O', 'B', 'O', 'B', 'B', 'O', 'O', 'B', 'B']

# Sentence = "TNS is looking for a Sr software developer to join a team that is responsible for the development and maintenance of the TNSOnline and MMIS web portals. The TNS web portal is used by internal and external customers to monitor and report on transactions processed through the TNS network."

# entities = ["TNS", "Sr software developer", "development", "maintenance", "TNSOnline", "MMIS web portals", "TNS web portal", "internal and external customers", "monitor", "report", "transactions processed", "TNS network"]

# def sub_lists(list1): 
#     sublist = [[]] 
#     for i in range(len(list1) + 1): 
#         for j in range(i + 1, len(list1) + 1): 
#             sub = list1[i:j] 
#             if len(sub)>1:
# 	            sublist.append(str(sub).strip("[]")) 

#     return sublist 
# # print(sub_lists(x)) 
# sublist = sub_lists(x)

# # print(sublist)
# ss = str(x).strip("[]")
# ll = sublist
# del ll[0]
# # print(ss)

# # print(ll)
# # print(type(ll))

# for i in set(ll):
# 	if i in ss:
# 		if ss.count(i) > 1 :
# 			print("[%s]  --> %d "%(i , ss.count(i)))

list1 = [2,3,4,7,5,8,6,3,4,7,2,3,4]
x = list1 
sublist = [[]] 
for i in range(len(list1) + 1): 
    for j in range(i + 1, len(list1) + 1): 
        sub = list1[i:j] 
        if len(sub)>1:
            sublist.append(str(sub).strip("[]")) 
ss = str(x).strip("[]")
ll = sublist
print(ll)
del ll[0]
for i in set(ll):
	if i in ss:
		if ss.count(i) > 1 :
			print("[%s]  --> %d "%(i , ss.count(i)))




	









