# # # # # # uses 
# # # # # # features 

# # # # # # py3.7 --> latest stable --> py3
# # # # # # py2.7 --> mostly used  --> py2 

# # # # # # py2 ---> py3 XXX 
# # # # # # py3 ---> py2 XXX 

# # # # # # py2 , py3 

# # # # # # install 
# # # # # # 	win --> python.exe 
# # # # # # 	linux,mac --> py2 --> upgrade --> py3 

# # # # # # py  libs 
# # # # # # py shell 
# # # # # # IDLE 

# # # # # # writing of code 
# # # # # # ----------------
# # # # # # single line --> cmd , shell
# # # # # # python files --> IDLE , editor
# # # # # # project --> IDE(PyCharm)

# # # # # # running of code
# # # # # # --------------
# # # # # # single line --> cmd , shell
# # # # # # python files -->	
# # # # # # 		cmd>python <filename>.py 
# # # # # # 		idle --> run --> run module
# # # # # # IDE --> editor + console 

# # # # # # keywords 
# # # # # # --------
# # # # # # java --> ??
# # # # # # py2 --> 31 
# # # # # # py3.5 --> 33 
# # # # # # py3.7 --> 35 

# # # # # # >>>import keyword 
# # # # # # >>>keyword.kwlist
# # # # # # 	pre defined 
# # # # # # 	specific 
# # # # # # 	immutable ( XX add XX delete XX modify)
# # # # # # 	libs

# # # # # # identifiers 
# # # # # # -----------
# # # # # # 	user defined words 
# # # # # # 	naming components ( variable , function , class , object)
# # # # # # 	rules 
# # # # # # 		XX keyword 
# # # # # # 		small case (recommended)
# # # # # # 		upper case (not recommended)
# # # # # # 		XX start symbol XX _ __ @(special)
# # # # # # 		XX start number XX 
# # # # # # 		use number 
# # # # # # 		XX use symbol XX _
	
# # # # # # name , AGE , mobile2 , user_name ,__pwd ,_address , @staticmethod --> valid 
# # # # # # &name , 2mobile ,user$name --> invalid

# # # # # # variables 
# # # # # # ---------
# # # # # # data store 
# # # # # # 3 components
# # # # # # 	- name / identifier
# # # # # # 	- data / value 
# # # # # # 	- location / address
# # # # # # <varname> = <varvalue>

# # # # # # a = 10 

# # # # # # id(<varname>) --> location of var
# # # # # # type(<varname>) --> datatype of var

# # # # # # datatypes 
# # # # # # 	5 datatypes
# # # # # # 	independent 
# # # # # # 		numbers 
# # # # # # 		strings
# # # # # # 	collections / derived 
# # # # # # 		lists 
# # # # # # 		tuples
# # # # # # 		dictionaries 

# # # # # # 	special collections
# # # # # # 		sets 
# # # # # # 		frozensets

# # # # # # numbers --> py3 
# # # # # # 	int --> all whole
# # # # # # 	float --> all decimals 
# # # # # # 	complex --> <c>+<d>j 

# # # # # # numbers --> py2
# # # # # # 	int 
# # # # # # 	long
# # # # # # 	float 
# # # # # # 	complex 


# # # # # # -----------int--------------|------------long------------- py2
# # # # # # -----------int--------------|------------int-------------- py2

# # # # # # | --> max possible integer --> 9223372036854775807

# # # # # # >>>import sys
# # # # # # >>>sys.maxint py2 
# # # # # # >>>sys.maxsize py3
















# # # # # import sys
# # # # # import keyword

# # # # # print(keyword.kwlist)
# # # # # print(sys.maxsize)

# # # # # a = 10 
# # # # # print(a)
# # # # # print(id(a))
# # # # # print(type(a))

# # # # # numbers --> operations 
# # # # # operators  --> ??
# # # # # 	arithmetic 
# # # # # 	logical 
# # # # # 	comparision 
# # # # # 	bitwise

# # # # # 	membership 
# # # # # 	identity 

# # # # # arithmetic --> 7 --> values 
# # # # # + add 
# # # # # - sub 
# # # # # * mul 
# # # # # / div 
# # # # # // floordiv 
# # # # # % modulo / rem 
# # # # # ** exponent 

# # # # a = 25
# # # # b = 8 

# # # # # print(a+b)
# # # # # print(a-b)
# # # # # print(a*b)
# # # # # py2  a = 25.0 
# # # # # print(a/b) # float
# # # # # print(a//b) # int
# # # # # py3  a = 25 
# # # # # print(a/b) # float
# # # # # print(a//b) # int
# # # # # print(a%b)
# # # # # print(25**8)
# # # # # print(3**2)

# # # # # comparision --> 6 --> True/False
# # # # # == equality 
# # # # # != non equality
# # # # # >
# # # # # <
# # # # # >=
# # # # # <=
# # # # # a = 25
# # # # # b = 8 
# # # # # print(a==b)
# # # # # print(a!=b)
# # # # # print(a>b)
# # # # # print(a<b)
# # # # # print(a>=b)
# # # # # print(a<=b)

# # # # # logical --> 3 --> True/False/values
# # # # # and 
# # # # # or
# # # # # not 

# # # # # truthtables 

# # # # # ip1			ip2			ip1 and ip2 
# # # # # t 			 t 				t 
# # # # # t 			 f 				f 
# # # # # f    		 	 t 				f 
# # # # # f 			 f  			f 
# # # # # and --> tt t 

# # # # # ip1			ip2			ip1 or ip2 
# # # # # t 			 t  			t 
# # # # # t 			 f 				t 
# # # # # f  			 t 				t 
# # # # # f 			 f 				f  
# # # # # or --> ff f 

# # # # # 1's complement 
# # # # # not(t) --> f 
# # # # # not(f) --> t 

# # # # a = 10 
# # # # b = 5 
# # # # c = 1 

# # # # # print(a>b and b>c) # t t --> t 
# # # # # print(a<b and b>c) # f t --> f 
# # # # # print(a>b and b<c) # t f --> f
# # # # # print(a<b and b<c) # f f --> f 

# # # # # print(a>b or b>c) # t t --> t
# # # # # print(a<b or b>c) # f t --> t 
# # # # # print(a>b or b<c) # t f --> t
# # # # # print(a<b or b<c) # f f --> f 

# # # # # print(not(a>b))
# # # # # print(not(c>b))

# # # # # print(10 and 20) # 20
# # # # # print(10 or 20) # 10

# # # # # print(20 and 10) # 10
# # # # # print(20 or 10) # 20

# # # # # 10 and 20 
# # # # # t  and  t --> 20 

# # # # # 10 or 20 
# # # # # t  or ---> 10  
# # # # # print(a or 20)

# # # # # bitwise --> 6 --> values 
# # # # # number --> bits 

# # # # # bw and ---> & 
# # # # # bw or -->   |
# # # # # bw not --> ~ 
# # # # # right shift --> >>
# # # # # left shift --> <<
# # # # # xor --> ^  exclusive or 

# # # # # 	  128  64  32  16  8  4  2  1 
# # # # # 10 -   0   0   0   0   1  0  1  0   --> 00001010
# # # # # 20 -   0   0   0   1   0  1  0  0   --> 00010100

# # # # # & --> ttt --> 111 

# # # # # 10    -   00001010
# # # # # 20    -   00010100
# # # # # 10|20 -   00011110  --> 30 
# # # # # 10&20 -   00000000  --> 0 

# # # # # ~ --> 2's complement 

# # # # # ~x --> -(x+1)
# # # # # ~10 --> -11
# # # # # ~(-10) --> 9 

# # # # # right shift --> >>

# # # # # 10 >> 2 --> 00001010 >> 2 --> 00000010 --> 2 
# # # # # 10 << 2  --> 00001010 << 2 --> 00101000 --> 40

# # # # # 8>>2  --> 2 
# # # # # 12<<2 --> 48  

# # # # # xor --> ??? 

# # # # # output in python 
# # # # # print --> command --> py2 
# # # # # print()-> function --> py3 

# # # # # py2 , py3 
# # # # # print(10)
# # # # # print(20)
# # # # # print(30)

# # # # # py3
# # # # # print(10,end=" ")
# # # # # print(20,end=" ")
# # # # # print(30)

# # # # # strings
# # # # # -------
# # # # # 	' ' or " "
# # # # # 	<class str> 
# # # # # 	features
# # # # # 	--------
# # # # # 	immutable
# # # # # 	indexed 
# # # # # 	sliced 
# # # # # 	concatenated 
# # # # # 	iterated 

# # # # # <strname> = "<strvalue>"
# # # # tech = "python"
# # # # # print(tech)
# # # # # print(type(tech))

# # # # # indexing
# # # # # --------
# # # # # p   y   t   h   o   n 
# # # # # 0   1   2   3   4   5  --> forward indices 
# # # # # -6 -5  -4  -3  -2  -1  --> reverse indices

# # # # # 3 --> h 
# # # # # 0 --> p 
# # # # # 5 --> n 
# # # # # -3 --> h
# # # # # -2 --> o 

# # # # # <strname>[<index>]
# # # # # print(tech[0]) # p
# # # # # print(tech[-4])
# # # # # print(tech[5])
# # # # # print(tech[-3])

# # # # tech = 'python and machine learning'
# # # # # print(tech[10])
# # # # # print(tech[-4])

# # # # # slicing 
# # # # # -------
# # # # # python --> 012345

# # # # <strname>[<sindex> : <eindex>]
# # # # # print(tech[0:6]) # python 0 --> 5
# # # # # print(tech[10:19]) # 10 --> 18 
# # # # # print(tech[-10:-6]) # -10 -9 -8 -7 
# # # # # print(tech[-20:-14])

# # # # # print(tech[5:15]) # 5678. . .14 --> +1 --> step
# # # # # <strname>[<sindex> : <eindex> : <step>]
# # # # # print(tech[5:15:1])
# # # # # print(tech[5:15:2]) # 5 7 9 11 13 step --> +2 

# # # # # print(tech[:10])
# # # # # print(tech[11:])
# # # # # print(tech[::2]) # step --> +2

# # # # # <strname>[<sindex> : <eindex> : <step>] sindex > eindex , step<0
# # # # # print(tech[15:5:-1]) # 15 14 13 12  . . . . . 6
# # # # # print(tech[:5:-1])
# # # # # print(tech[17::-1])
# # # # # print(tech[::-1]) # reversing of string 
# # # # # print(tech[::-2])

# # # # # concatenation 
# # # # # -------------
# # # # tech = "python"
# # # # # db = "mysql"

# # # # # print(tech + " " + db)
# # # # # newvar = tech + " " + db
# # # # # print(newvar)

# # # # version = 3
# # # # # # print(tech + version) # error 

# # # # # string literals 
# # # # # %d --> int 
# # # # # %f --> float
# # # # # %s --> str 

# # # # # tech = "python"
# # # # # version = 3

# # # # # # print("python 3")
# # # # # print("%s %d" %(tech,version))

# # # # # newvar = "%s %d" %(tech,version)
# # # # # print(newvar)

# # # # tech = "python"
# # # # ver = 3.7 
# # # # year = 2019 

# # # # # print("the version of python is 3.7 in 2019")
# # # # # print("the version of %s is %f in %d"%(tech,ver,year))

# # # # name = "khan"
# # # # marks = 80 

# # # # # print("%s has secured %d marks"%(name,marks))

# # # # name = "khan"
# # # # perc = 80

# # # # print("%s has secured %d %%  marks" %(name,perc))

# # # # # escape char --> % --> string literals

# # # # # index , slicing --> ??

# # # # type casting , special strings

# # # tech = "python"
# # # version = 3 

# # # # int --> str 
# # # # str --> int (not always)
# # # # "100" --> 100 
# # # # "abc" -->  ?? XX 

# # # # number --> string --> str()

# # # # print(version)
# # # # print(type(version))
# # # # version = str(version)
# # # # print(version)
# # # # print(type(version))

# # # # tech = "python"
# # # # version = 3 

# # # # print(tech + str(version))
# # # # str() , repr() --> number --> string

# # # # n = "100"
# # # # print(n)
# # # # print(type(n))

# # # # n = int(n)

# # # # print(n)
# # # # print(type(n))

# # # # name = "khan"
# # # # print(name)
# # # # name = int(name)
# # # # print(name)

# # # # char --> number --> ascii 
# # # # ord() char --> ascii 
# # # # chr() ascii --> char 

# # # # print(ord("c"))
# # # # print(ord("a"))
# # # # print(ord("Z"))
# # # # print(ord("A"))
# # # # print(ord("1"))

# # # # print(chr(100))
# # # # print(chr(80))
# # # # print(chr(32))

# # # # stmt = "i'm in a python session"
# # # # print(stmt)

# # # # escape char --> \
# # # # stmt = 'i\'m in a python session'
# # # # print(stmt)

# # # # special chars --> \n \t 

# # # # para = "first\n second\n third\n fourth\n fifth"
# # # # print(para)

# # # # tech = "python\tdjango"
# # # # print(tech)

# # # # multi line strings
# # # # book = '''first
# # # # second
# # # # third
# # # # fourth
# # # # fifth'''
# # # # print(book)

# # # # path = "c\demo\programs\python\technology\newcode"
# # # # print(path)

# # # # path = "c\demo\programs\python\\technology\\newcode"
# # # # print(path)

# # # # raw strings --> sys paths , URLs

# # # # path = r"c\demo\programs\python\technology\newcode"
# # # # print(path)

# # # # unicode strings --> ???

# # # # user inputs 
# # # # 	keyboard inputs 
# # # # 	CLI inputs

# # # # input() --> scanf , java.util.Scanner

# # # # py3 
# # # # user --> input() ---> code 
# # # # 10     -> input() --> "10"
# # # # 10.34  -> input() --> "10.34"
# # # # "khan"   -> input() --> "khan"

# # # # py2 
# # # # user --> input() ---> code 
# # # # 10     -> input() --> 10
# # # # 10.34  -> input() --> 10.34
# # # # "khan"   -> input() --> "khan"

# # # # py2 
# # # # user -->   raw_input() ---> code 
# # # # 10     ->  raw_input() --> "10"
# # # # 10.34  ->  raw_input() --> "10.34"
# # # # "khan"  -> raw_input() --> "khan"

# # # # py2 --> input() , raw_input()
# # # # py3 --> input()

# # # # <varname> = input("<dialouge>")
# # # # a = input("enter anything : ")
# # # # print(a)
# # # # print(type(a))

# # # # raw_input()

# # # # string functions 
# # # # ----------------
# # # # functions
# # # 	# attribute fetching . 
# # # 	# parameterised (<something>)

# # # # string functions
# # # 	# case based 
# # # 	# check 
# # # 	# manipulative 

# # # # stmt = "Python is an EASY Programming language"
# # # # case based 

# # # # <strname>.lower() 
# # # # print(stmt.lower())
# # # # stmt = stmt.lower()
# # # # print(stmt)

# # # # <strname>.upper()
# # # # print(stmt.upper()) 

# # # # <strname>.swapcase() 
# # # # print(stmt.swapcase())

# # # # <strname>.capitalize() 
# # # # print(stmt.capitalize())

# # # # <strname>.title() 
# # # # print(stmt.title())

# # # # check functions --> True / False
# # # stmt = "Python is an EASY Programming language"

# # # # <strname>.startswith(<char/substring>)
# # # # print(stmt.startswith("P"))
# # # # print(stmt.startswith("Pyt"))
# # # # print(stmt.startswith("z"))
# # # # print(stmt.startswith("p"))

# # # # <strname>.endswith(<char/substring>)
# # # # print(stmt.endswith("e"))
# # # # print(stmt.endswith("language"))
# # # # print(stmt.endswith("z"))
# # # # print(stmt.endswith("LANGUAGE"))

# # # # <strname>.isdigit()
# # # # 		- True --> only number
# # # # 		- False --> alphasymbol

# # # # a = "python"
# # # # print(a.isdigit())

# # # # n = "100"
# # # # print(n.isdigit())

# # # # n = "100a"
# # # # print(n.isdigit())

# # # # membership operators --> True / False
# # # # --------------------
# # # # in , not in 

# # # # stmt = "Python is an EASY Programming language"
# # # # print("p" in stmt)
# # # # print("P" in stmt)

# # # # print("z" not in stmt)
# # # # print("n" not in stmt)

# # # # identity operators --> True / False
# # # # ------------------
# # # # is , is not 

# # # # tech = "python"
# # # # print(tech is "python")
# # # # print(tech is not "python")

# # # # print(tech is "pyth")
# # # # print(tech is not "pyt")

# # # # comments 
# # # # --------
# # # # single line 
# # # ''' 
# # # multi 
# # # line 
# # # comments
# # # '''

# # # # print("isfunction : " + str(varname))
# # # # print("is function %s" %(varname))

# # # # enter a stmt 
# # # # "python and machine learning"
# # # # enter a char 
# # # # "p"
# # # # true 
# # # # true 

# # # # enter a stmt 
# # # # "python and machine learning"
# # # # enter a char 
# # # # "h"
# # # # true 
# # # # false 

# # # # enter a stmt 
# # # # "python and machine learning"
# # # # enter a char 
# # # # "P"
# # # # true 
# # # # true 

# # # # enter a stmt 
# # # # "python and machine learning"
# # # # enter a char 
# # # # "z"
# # # # false 
# # # # false 

# # # # stmt = input("enter a statement : ")
# # # # char = input("enter a character : ")

# # # # print(char.lower() in stmt.lower())
# # # # print((stmt.lower()).startswith(char.lower()))

# # # # manipulative --> 040919

# # # stmt = "python and machine learning"

# # # # len(<strname>) # length of string / no of chars 
# # # # print(len(stmt))

# # # # <strname>.index(<char/substring>)
# # # # print(stmt.index("p"))
# # # # print(stmt.index("python"))
# # # # print(stmt.index("n")) # 5
# # # # print(stmt.index("n",6)) # 8
# # # # print(stmt.index("n",9)) # 16 
# # # # print(stmt.index("n",17)) # 23 
# # # # print(stmt.index("n",24)) # 25
# # # # print(stmt.index("z")) # error

# # # # <strname>.find(<char/substring>)
# # # # print(stmt.find("p"))
# # # # print(stmt.find("python"))
# # # # print(stmt.find("n")) # 5
# # # # print(stmt.find("n",6)) # 8
# # # # print(stmt.find("n",9)) # 16 
# # # # print(stmt.find("n",17)) # 23 
# # # # print(stmt.find("n",24)) # 25
# # # # print(stmt.find("z")) # -1

# # # stmt = "python and machine learning"

# # # # <strname>.count(<char/substring>)
# # # # print(stmt.count("p"))
# # # # print(stmt.count("n"))
# # # # print(stmt.count("thon"))
# # # # print(stmt.count("in"))
# # # # print(stmt.count("z"))

# # # # <strname>.replace(<old> , <new>)
# # # # print(stmt.replace("python" , "java"))
# # # # print(stmt)
# # # # print(stmt.replace("n" , "m"))

# # # # <strname>.replace(<old> , <new> ,<count>)
# # # # print(stmt.replace("n" , "m" , 1))
# # # # print(stmt.replace("n" , "m" , 3))

# # # stmt = "python and machine learning"
# # # # <strname>.split() # delimiter = " "
# # # # print(stmt.split())
# # # # <strname>.split(<delimiter>)
# # # # print(stmt.split("a"))
# # # # print(stmt.split("and"))

# # # words = stmt.split()
# # # # print(words) # collection

# # # # <delimiter>.join(<collection>)
# # # # print(" ".join(words))
# # # # print("_".join(words))
# # # # print("\n".join(words))

# # dia = "    in india we live    "
# # # # print(dia)
# # # # <strname>.strip()
# # # print(dia.strip(" in"))
# # # # <strname>.rstrip()
# # # # print(dia.rstrip())
# # # # <strname>.lstrip()
# # # # print(dia.lstrip())

# # # # print(dia.strip(" i"))
# # # # print(dia.strip(" in"))
# # # # print(dia.strip("in "))
# # # # print(dia.strip(" live")) 

# # # # <strname>.zfill(<lenint>)
# # # # tech = "python"
# # # # print(tech.zfill(10))

# # # # num = 1234
# # # # print(str(num).zfill(8)) # 00001234

# # # rstrip() , lstrip() --> remove chars 
# # # isalpha() , isnum() --> ???

# # # enter a stmt 
# # # python is easy 
# # # enter a char 
# # # p 
# # # index of p is 0 

# # # enter a stmt 
# # # python is easy 
# # # enter a char 
# # # z
# # # index of z is -1

# # # enter a stmt 
# # # python is easy 
# # # enter an old word 
# # # easy
# # # enter a new word 
# # # tough 
# # # python is tough

# # # enter a number 
# # # 189 
# # # enter a length 
# # # 5 
# # # 00189

# # conditional statements 
# # 	descision trees 
# # 	condition  --> T / F 
# # 	statements --> executable code / logic 

# # if  -> 1 statement
# # if else  -> 2 statements
# # if elif elif else  -> 4 statements

# # syntax:
# # -------

# # if <condition>:
# # 	<statements>

# # if <condition>:
# # 	<statements1>
# # else:
# # 	<statements2>	

# # if <condition1>:
# # 	<statements1>
# # elif <condition2>:
# # 	<statements2>	
# # elif <condition3>:
# # 	<statements3>	
# # elif <condition4>:
# # 	<statements4>	
# # else:
# # 	<statements5>

# # java --> switch case default --> XXX 

# # a = 4 
# # if a > 5: # condition
# # 	print("hello")

# # a = 14 
# # if a > 5: # condition
# # 	print("hello")
# # else:
# # 	print("bye")

# # a = 2 
# # if a>5:
# # 	print("a 5")
# # elif a>8:
# # 	print("a 8")
# # elif a==10:
# # 	print("a 10")
# # else:
# # 	print("none")

# # even / odd 
# # n = 812 
# # if n%2 == 0 :
# # 	print(str(n) + " is even")
# # else:
# # 	print(str(n) + " is odd")

# # enter a number:
# # 8 
# # 8 is even

# # enter a number:
# # 81 
# # 81 is odd

# # enter a number:
# # abc
# # invalid input

# # int str --> ?? if else 
# # 	int --> even odd --> ?? if else 
# # 	str 
	
# # nested if else 
# # n = input("enter a number : ") 
# # if n.isdigit(): 
# # 	n = int(n) 
# # 	if n%2 == 0:
# # 		print(str(n) + " is even")
# # 	else:
# # 		print(str(n) + " is odd")
# # else:
# # 	print("invalid input")

# # 3 5 multiples 
# # enter a number 
# # 6 
# # 6 is multiple of 3 only 
# # enter a number 
# # 10 
# # 10 is multiple of 5 only 
# # enter a number 
# # 30 
# # 30 is multiple of 3 and 5 
# # enter a number 
# # 12
# # 12 is multiple of 3 only 
# # enter a number 
# # 14 
# # 14 is not multiple of 3 and 5
# # enter a number 
# # 90
# # 90 is multiple of 3 and 5  

# # n = int(input("enter a number : "))

# # if n%3 == 0 and n%5 == 0 :
# # 	print(str(n)+ " is multiple of 3 and 5")
# # elif n%5 == 0 :
# # 	print(str(n)+ " is multiple of 5 only")
# # elif n%3 == 0  :
# # 	print(str(n)+ " is multiple of 3 only ")
# # else:
# # 	print("none")

# # enter a stmt 
# # 	python is easy 
# # enter an old word
# # 	python 
# # enter a new word
# # 	java 
# # java is easy 

# # enter a stmt 
# # 	python is easy 
# # enter an old word
# # 	s
# # enter a new word
# # 	j
# # python ij eajy 

# # enter a stmt 
# # 	python is easy 
# # enter a old word
# # 	php 
# # php not in stmt 

# # membership , replace()

# # tasks cdst --> 060919

# # enter a value :
# # 10.05 
# # 100
# # 25

# # enter a value :
# # abc.df 
# # 3
# # 2 

# # enter a value :
# # abc.10 
# # 3
# # 100

# # enter a value :
# # 10.3.8 
# # invalid inputs 

# # enter a value :
# # ab.cd.ef.th
# # invalid inputs 

# # print(dir(str))

# # n = input("enter an input:") # 100.03
# # if n.count(".") > 1:
# # 	print("invalid inputs")
# # else:
# # 	i = n.index(".") # 3
# # 	f = n[:i] # n[:3] --> 100
# # 	s = n[i+1:] # n[4:] --> 03
# # 	# print(f)
# # 	# print(s)
# # 	if f.isdigit() and s.isdigit():
# # 		print("%d \n %d"%(int(f)**2 , int(s)**2))
# # 	elif f.isdigit() and s.isalpha():
# # 		print("%d \n %d"%(int(f)**2 , len(s)))
# # 	elif f.isalpha() and s.isdigit():
# # 		print("%d \n %d"%(len(f) ,int(s)**2))
# # 	else:
# # 		print("%d \n %d"%(len(f),len(s)))

# # enter time in hh:mm:ssFF format 
# # 10:34:56pm
# # 22:34:56

# # enter time in hh:mm:ssFF format 
# # 10:34:56am
# # 10:34:56

# # enter time in hh:mm:ssFF format 
# # 8:34:56pm
# # invalid format passed 

# # enter time in hh:mm:ssFF format 
# # 08:34:56pm
# # 20:34:56

# # enter time in hh:mm:ssFF format 
# # ab.cd.efpm
# # invalid format passed 

# # time = input("enter time in hh:mm:ssFF format : ")
# # if len(time) == 10 :
# # 	hh = time[:2]
# # 	mm = time[3:5]
# # 	ss = time[6:8]
# # 	if hh.isdigit() and mm.isdigit() and ss.isdigit():
# # 		if (time.lower()).endswith("pm"):
# # 			print("%d : %s : %s"%(int(hh)+12 , mm , ss))
# # 		else:
# # 			print("%s : %s : %s"%(hh , mm , ss))
# # else:
# # 	print("invalid format passed")

# # enter a first char 
# # "m"
# # enter a second char 
# # "p"
# # p occurs after m 

# # enter a first char 
# # "a"
# # enter a second char 
# # "m"
# # m occurs after a 

# # enter a first char 
# # "python"
# # enter a second char 
# # "p"
# # invalid inputs passed

# # enter a stmt 
# # python is easy 
# # enter a word/char 
# # p 
# # p is in stmt 
# # index of p is 0 

# # enter a stmt 
# # python is easy 
# # enter a word/char 
# # Python
# # python is in stmt 
# # index of python is 0 to 5  

# # enter a stmt 
# # python is easy 
# # enter a word/char 
# # x 
# # x not in stmt 

# loops 
# -----
# 	iterations / repetitions

# 	finite 
# 	infitnite 

# for  --> numbers , strings , collections
# while --> numbers 

# for --> finite 
# while --> finite , infitnite

# for --> numbers 
# range() 
# 	iterable 

# syntax
# ------ 
# range(<end>) 0 1 2 3 4 . . . . end-1
# range(7) 0 1 2 3 4 5 6

# range(<start> , <end>) start , start+1 , start+2 . . . . end-1
# range(2,15) 2 3 4 5 6 ..... 14

# range(<start>,<end>,<step>) start , start+step , start+2step . . . . end-1
# range(2,15,3) 2 5 8 11 14 

# range(<end>,<start>,-1)
# range(10,4,-1) 10 9 8 7 6 5 

# range(<end>,<start>,-<step>)
# range(20,4,-3) 20 17 14 11 8 5 

# 4 components
# 	initialisation ----> start
# 	limit / condition --> end 
# 	inc/dec  --> step (fashion)
# 	statements ---> executable lines

# syntax
# ------

# for <dummy> in range():
# 	<statements>

# for i in range(10):
# 	print(i)

# for i in range(3,10):
# 	print(i)

# for i in range(0,100,5):
# 	# print(i,end="") # py3 
# 	print(i)

# for i in range(10,1,-1):
# 	print(i)

# for i in range(100,1,-10):
# 	print(i)

# patterns 
# n ---> 5 
n = 5 

# *
# **
# ***
# ****
# *****

# print("*" * 1
# print("*" * 2)
# print("*" * 3)
# print("*" * 4)
# print("*" * 5)

# for i in range(1,n+1):
# 	print("*" * i)

# n = 5 
# 1
# 22
# 333
# 4444
# 55555

# for i in range(1,n+1):
# 	print(str(i) * i)

n = 5 
# a
# bb 
# ccc 
# dddd
# eeeee

# alpha = "abcdefghijk"
# for i in range(n):
# 	print(alpha[i] * (i+1))

# for i in range(ord("a"),ord("a")+n): # 97 --> 102
# 	print(chr(i)*(i-96))

n = 5 

000 000 000 
001 001 001
002 004 008 
003 009 027
004 016 064
005 025 125 













