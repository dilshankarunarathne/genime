const=1
#import simplejson   
while const==1:

	""" getTerminalSize()
	 - get width and height of console
	 - works on linux,os x,windows,cygwin(windows)
	"""
	# import only system from os 
	from os import system, name 
	# import sleep to show output for some time period 
	from time import sleep 
	import time
	import datetime
	ts1 = int(time.time())
	st1 = datetime.datetime.fromtimestamp(ts1).strftime('%Y-%m-%d %H:%M:%S')
	# define our clear function 
	def clear(): 
	  
	    # for windows 
	    if name == 'nt': 
	        _ = system('cls') 
	  
	    # for mac and linux(here, os.name is 'posix') 
	    else: 
	        _ = system('clear') 

	#clearing interpriter console
	sleep(0.1)
	clear()

	__all__=['getTerminalSize']


	def getTerminalSize():
	   import platform
	   current_os = platform.system()
	   tuple_xy=None
	   if current_os == 'Windows':
	       tuple_xy = _getTerminalSize_windows()
	       if tuple_xy is None:
	          tuple_xy = _getTerminalSize_tput()
	          # needed for window's python in cygwin's xterm!
	   if current_os == 'Linux' or current_os == 'Darwin' or  current_os.startswith('CYGWIN'):
	       tuple_xy = _getTerminalSize_linux()
	   if tuple_xy is None:
	       print ("default")
	       tuple_xy = (80, 25)      # default value
	   return tuple_xy

	def _getTerminalSize_windows():
	    res=None
	    try:
	        from ctypes import windll, create_string_buffer

	        # stdin handle is -10
	        # stdout handle is -11
	        # stderr handle is -12

	        h = windll.kernel32.GetStdHandle(-12)
	        csbi = create_string_buffer(22)
	        res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
	    except:
	        return None
	    if res:
	        import struct
	        (bufx, bufy, curx, cury, wattr,
	         left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
	        sizex = right - left + 1
	        sizey = bottom - top + 1
	        return sizex, sizey
	    else:
	        return None

	def _getTerminalSize_tput():
	    try:
	       import subprocess
	       proc=subprocess.Popen(["tput", "cols"],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
	       output=proc.communicate(input=None)
	       cols=int(output[0])
	       proc=subprocess.Popen(["tput", "lines"],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
	       output=proc.communicate(input=None)
	       rows=int(output[0])
	       return (cols,rows)
	    except:
	       return None


	def _getTerminalSize_linux():
	    def ioctl_GWINSZ(fd):
	        try:
	            import fcntl, termios, struct, os
	            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,'1234'))
	        except:
	            return None
	        return cr
	    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
	    if not cr:
	        try:
	            fd = os.open(os.ctermid(), os.O_RDONLY)
	            cr = ioctl_GWINSZ(fd)
	            os.close(fd)
	        except:
	            pass
	    if not cr:
	        try:
	            cr = (env['LINES'], env['COLUMNS'])
	        except:
	            return None
	    return int(cr[1]), int(cr[0])

	if __name__ == "__main__":
	    sizex,sizey=getTerminalSize()
	#    print  ('width =',sizex,'height =',sizey)



	# main system

	# key generator

	fi=[]
	# letter/number/symbol lists
	l=[]
	#lower case letters
	ll=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	#number
	nu=['1','2','3','4','5','6','7','8','9','0']
	#upper case letters
	ul=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

	print (" ")
	print (" ")
	print (" ")
	print (" ")
	print (" ")

	print ("          How many characters should be in your wordlist? (3/4/5/6/7/8) ")
	o4=int(input("                    >   "))
	print (" ")
	print ("          Do you want to add lower case letters? (y/n)")
	o5=str(input("                    >   "))
	print (" ")
	print ("          Do you want to add upper case letters? (y/n)")
	o6=str(input("                    >   "))
	print (" ")
	print ("          Do you want to add numbers? (y/n)")
	o7=str(input("                    >   "))
	print (" ")

	#generating one character list
	if o5=="y" or o5=="Y":
		l=l+ll
	if o6=="y" or o6=="Y":
		l=l+ul
	if o7=="y" or o7=="Y":
		l=l+nu

	# getting to work

	if o4==3:
		for i1 in l:
			for i2 in l:
				for i3 in l:
					f=i1+i2+i3
					fi.append(f)
	elif o4==4:
		for i1 in l:
			for i2 in l:
				for i3 in l:
					for i4 in l:
						f=i1+i2+i3+i4
						fi.append(f)
	elif o4==5:
		for i1 in l:
			for i2 in l:
				for i3 in l:
					for i4 in l:
						for i5 in l:
							f=i1+i2+i3+i4+i5
							fi.append(f)
	elif o5==6:
		for i1 in l:
			for i2 in l:
				for i3 in l:
					for i4 in l:
						for i5 in l:
							for i6 in l:
								f=i1+i2+i3+i4+i5+i6
								fi.append(f)
	elif o5==7:
		for i1 in l:
			for i2 in l:
				for i3 in l:
					for i4 in l:
						for i5 in l:
							for i6 in l:
								for i7 in l:
									f=i1+i2+i3+i4+i5+i6+i7
									fi.append(f)
	elif o5==8:
		for i1 in l:
			for i2 in l:
				for i3 in l:
					for i4 in l:
						for i5 in l:
							for i6 in l:
								for i7 in l:
									for i8 in l:
										f=i1+i2+i3+i4+i5+i6+i7+i8
										fi.append(f)

	# anime function

	for item in fi:
		f1=" "
		f2=" "
		f3=" "
		f4=" "
		f5=" "
		f6=" "
		f7=" "
		f8=" "
		f9=" "
		f0=" "

		nn=len(item)

		for i in range (nn):

			le=item[i]
			if le=="a":
					l1="          "                  
					l2="          "      
					l3=" .oooo.   "     
					l4="`P  )88b  "       
					l5=" .oP\"888  "       
					l6="d8(  888  "       
					l7="`Y888\"\"8o "       
					l8="          "   
					l9="          "   
					l0="          "
			elif le=="b": 
					l1=" .o8         "      
					l2="\"888         "      
					l3=" 888oooo.    "       
					l4=" d88\' `88b   "      
					l5=" 888   888   "      
					l6=" 888   888   "      
					l7=" `Y8bod8P\'   "      
					l8="             "      
					l9="             "      
					l0="             "
			elif le=="c":

					l1="            "     
					l2="            "      
					l3=" .ooooo.    "      
					l4="d88\' `\"Y8   "      
					l5="888         "      
					l6="888   .o8   "      
					l7="`Y8bod8P\'   "      
					l8="            "      
					l9="            "      
					l0="            " 
			elif le=="d":
					                   
					l1="      .o8    "      
					l2="     \"888    "      
					l3=" .oooo888    "      
					l4="d88\' `888    "      
					l5="888   888    "      
					l6="888   888    "      
					l7="`Y8bod88P\"   "      
					l8="             "      
					l9="             "     
					l0="             "
			elif le=="e":
					                   
					l1="            "        
					l2="            "      
					l3=" .ooooo.    "      
					l4="d88\' `88b   "      
					l5="888ooo888   "      
					l6="888    .o   "      
					l7="`Y8bod8P\'   "      
					l8="            "      
					l9="            "      
					l0="            "  
			elif le=="f":
					                   
					l1=" .o88o.   "         
					l2=" 888 `\"   "         
					l3="o888oo    "         
					l4=" 888      "         
					l5=" 888      "         
					l6=" 888      "         
					l7="o888o     "         
					l8="          "         
					l9="          "         
					l0="          "  
			elif le=="g":
					                   
					l1="             "     
					l2="             "     
					l3=" .oooooooo   "     
					l4="888\' `88b    "     
					l5="888   888    "     
					l6="`88bod8P\'    "     
					l7="`8oooooo.    "     
					l8="d\"     YD    "     
					l9="\"Y88888P\'    "     
					l0="             "
			elif le=="h":
					                   
					l1="oooo          "    
					l2="`888          "    
					l3=" 888 .oo.     "    
					l4=" 888P\"Y88b    "    
					l5=" 888   888    "    
					l6=" 888   888    "    
					l7="o888o o888o   "    
					l8="              "    
					l9="              "      
					l0="              "
			elif le=="i":
					                   
					l1=" o8o    "         
					l2=" `\"\'    "         
					l3="oooo    "         
					l4="`888    "         
					l5=" 888    "         
					l6=" 888    "         
					l7="o888o   "         
					l8="        "         
					l9="        "         
					l0="        "
			elif le=="j":
					                   
					l1="    o8o   "         
					l2="    `\"\'   "         
					l3="   oooo   "         
					l4="   `888   "         
					l5="    888   "         
					l6="    888   "         
					l7="    888   "         
					l8="    888   "         
					l9=".o. 88P   "         
					l0="`Y888P    " 
			elif le=="k":
					 
					l1="oooo          "    
					l2="`888          "    
					l3=" 888  oooo    "    
					l4=" 888 .8P\'     "    
					l5=" 888888.      "    
					l6=" 888 `88b.    "    
					l7="o888o o888o   "    
					l8="              "    
					l9="              "    
					l0="              "
			elif le=="l":
					                   
					l1="oooo    "          
					l2="`888    "          
					l3=" 888    "          
					l4=" 888    "          
					l5=" 888    "          
					l6=" 888    "          
					l7="o888o   "          
					l8="        "          
					l9="        "          
					l0="        " 
			elif le=="m":
					                   
					l1="                    "
					l2="                    "
					l3="ooo. .oo.  .oo.     "
					l4="`888P\"Y88bP\"Y88b    "
					l5=" 888   888   888    "
					l6=" 888   888   888    "
					l7="o888o o888o o888o   "
					l8="                    "
					l9="                    "
					l0="                    "
			elif le=="n":
					                   
					l1="              "    
					l2="              "    
					l3="ooo. .oo.     "    
					l4="`888P\"Y88b    "    
					l5=" 888   888    "    
					l6=" 888   888    "    
					l7="o888o o888o   "    
					l8="              "    
					l9="              "    
					l0="              "
			elif le=="o":
					                   
					l1="            "      
					l2="            "      
					l3=" .ooooo.    "      
					l4="d88\' `88b   "      
					l5="888   888   "      
					l6="888   888   "      
					l7="`Y8bod8P\'   "      
					l8="            "      
					l9="            "      
					l0="            "
			elif le=="p":
					                   
					l1="             "    
					l2="             "    
					l3="oo.ooooo.    "    
					l4=" 888\' `88b   "    
					l5=" 888   888   "    
					l6=" 888   888   "    
					l7=" 888bod8P\'   "    
					l8=" 888         "    
					l9="o888o        "    
					l0="             "
			elif le=="q":
					                   
					l1="             "     
					l2="             "     
					l3=" .ooooo oo   "     
					l4="d88\' `888    "     
					l5="888   888    "     
					l6="888   888    "     
					l7="`V8bod888    "     
					l8="      888.   "     
					l9="      8P\'    "     
					l0="      \"      "     
			elif le=="r":
					 
					l1="           "       
					l2="           "       
					l3="oooo d8b   "       
					l4="`888\"\"8P   "       
					l5=" 888       "       
					l6=" 888       "       
					l7="d888b      "       
					l8="           "       
					l9="           "       
					l0="           "
			elif le=="s":
					                   
					l1="           "       
					l2="           "       
					l3=" .oooo.o   "       
					l4="d88(  \"8   "       
					l5="`\"Y88b.    "      
					l6="o.  )88b   "       
					l7="8\"\"888P\'   "       
					l8="           "       
					l9="           "       
					l0="           "
			elif le=="t":
					                   
					l1="    .     "        
					l2="  .o8     "        
					l3=".o888oo   "        
					l4="  888     "        
					l5="  888     "        
					l6="  888 .   "        
					l7="  \"888\"   "        
					l8="          "        
					l9="          "        
					l0="          "
			elif le=="u":
					                   
					l1="             "     
					l2="             "     
					l3="oooo  oooo   "     
					l4="`888  `888   "     
					l5=" 888   888   "     
					l6=" 888   888   "     
					l7=" `V88V\"V8P\'  "     
					l8="             "     
					l9="             "     
					l0="             "
			elif le=="v":
					                   
					l1="              "    
					l2="              "    
					l3="oooo    ooo   "    
					l4=" `88.  .8\'    "    
					l5="  `88..8\'     "    
					l6="   `888\'      "    
					l7="    `8\'       "    
					l8="              "    
					l9="              "    
					l0="              "
			elif le=="w":
					                   
					l1="                  "
					l2="                  "
					l3="oooo oooo    ooo  "
					l4=" `88. `88.  .8\'   " 
					l5="  `88..]88..8\'    "
					l6="   `888\'`888\'     "
					l7="    `8\'  `8\'      "
					l8="                  "
					l9="                  "
					l0="                  "
			elif le=="x":
					                   
					l1="              "    
					l2="              "    
					l3="oooo    ooo   "    
					l4=" `88b..8P\'    "    
					l5="   Y888\'      "    
					l6=" .o8\"\'88b     "    
					l7="o88\'   888o   "   
					l8="              "   
					l9="              "   
					l0="              "
			elif le=="y":
					                   
					l1="              "    
					l2="              "    
					l3="oooo    ooo   "     
					l4=" `88.  .8\'    "     
					l5="  `88..8\'     "     
					l6="   `888\'      "     
					l7="    .8\'       "     
					l8=".o..P\'        "     
					l9="`Y8P\'         "     
					l0="              " 
			elif le=="z":
					                   
					l1="             "     
					l2="             "     
					l3="  oooooooo   "     
					l4=" d\'\"\"7d8P    "     
					l5="   .d8P\'     "     
					l6=" .d8P\'  .P   "     
					l7="d8888888P    "     
					l8="             "     
					l9="             "     
					l0="             "
			elif le=="A":
					                                        
					l1="      .o.         "       
					l2="     .888.        "       
					l3="    .8\"888.       "       
					l4="   .8\' `888.      "       
					l5="  .88ooo8888.     "       
					l6=" .8\'     `888.    "       
					l7="o88o     o8888o   "       
					l8="                  "       
					l9="                  "       
					l0="                  "
			elif le=="B":
					                            
					l1="oooooooooo.    "          
					l2="`888\'   `Y8b   "          
					l3=" 888     888   "          
					l4=" 888oooo888\'   "          
					l5=" 888    `88b   "          
					l6=" 888    .88P   "          
					l7="o888bood8P\'    "          
					l8="               "          
					l9="               "          
					l0="               "
			elif le=="C":
					                            
					l1="  .oooooo.    "           
					l2=" d8P\'  `Y8b   "           
					l3="888           "           
					l4="888           "           
					l5="888           "           
					l6="`88b    ooo   "           
					l7=" `Y8bood8P\'   "           
					l8="              "           
					l9="              "           
					l0="              "
			elif le=="D":
					                            
					l1="oooooooooo.     "         
					l2="`888\'   `Y8b    "         
					l3=" 888      888   "         
					l4=" 888      888   "         
					l5=" 888      888   "         
					l6=" 888     d88\'   "         
					l7="o888bood8P\'     "         
					l8="                "         
					l9="                "         
					l0="                "
			elif le=="E":
					                            
					l1="oooooooooooo  "           
					l2="`888\'     `8  "           
					l3=" 888          "           
					l4=" 888oooo8     "           
					l5=" 888    \"     "           
					l6=" 888       o  "           
					l7="o888ooooood8  "           
					l8="              "           
					l9="              "           
					l0="              "
			elif le=="F":
					                            
					l1="oooooooooooo   "          
					l2="`888\'     `8   "          
					l3=" 888           "          
					l4=" 888oooo8      "          
					l5=" 888    \"      "          
					l6=" 888           "          
					l7="o888o          "          
					l8="               "          
					l9="               "          
					l0="               "
			elif le=="G":
					                            
					l1="  .oooooo.     "          
					l2=" d8P\'  `Y8b    "          
					l3="888            "          
					l4="888    oooooo  "          
					l5="888    opoooo  "          
					l6="`88.     88    "          
					l7=" `Y8bood8P\'    "          
					l8="               "          
					l9="               "          
					l0="               "
			elif le=="H":
					                            
					l1="ooooo   ooooo  "          
					l2="`888\'   `888\'  "          
					l3=" 888     888   "          
					l4=" 888ooooo888   "          
					l5=" 888     888   "          
					l6=" 888     888   "          
					l7="o888o   o888o  "          
					l8="               "          
					l9="               "          
					l0="               "
			elif le=="I":
					                            
					l1="ooooo   "                 
					l2="`888\'   "                 
					l3=" 888    "                 
					l4=" 888    "                 
					l5=" 888    "                 
					l6=" 888    "                 
					l7="o888o   "                 
					l8="        "                 
					l9="        "                 
					l0="        "  
			elif le=="J":
				                            
					l1="   oooo   "
					l2="   `888   "              
					l3="    888   "              
					l4="    888   "              
					l5="    888   "              
					l6="    888   "              
					l7=".o. 88P   "              
					l8="`Y888P    "              
					l9="          "              
					l0="          "
			elif le=="K":
				                            
					l1="oooo    oooo  "           
					l2="`888   .8P\'   "           
					l3=" 888  d8\'     "           
					l4=" 88888[       "           
					l5=" 888`88b.     "           
					l6=" 888  `88b.   "           
					l7="o888o  o888o  "           
					l8="              "           
					l9="              "           
					l0="              "    
			elif le=="L":
				                            
					l1="ooooo          "          
					l2="`888\'          "          
					l3=" 888           "          
					l4=" 888           "          
					l5=" 888           "          
					l6=" 888       o   "          
					l7="o888ooooood8   "          
					l8="               "          
					l9="               "          
					l0="               "
			elif le=="M":
					                            
					l1="ooo        ooooo   "      
					l2="`88.       .888\'   "      
					l3=" 888b     d\'888    "      
					l4=" 8 Y88. .P  888    "      
					l5=" 8  `888\'   888    "      
					l6=" 8    Y     888    "      
					l7="o8o        o888o   "      
					l8="                   "      
					l9="                   "      
					l0="                   "
			elif le=="N":
					                            
					l1="ooooo      ooo   "        
					l2="`888b.     `8\'   "        
					l3=" 8 `88b.    8    "        
					l4=" 8   `88b.  8    "        
					l5=" 8     `88b.8    "        
					l6=" 8       `888    "        
					l7="o8o        `8    "        
					l8="                 "        
					l9="                 "        
					l0="                 "
			elif le=="O":
					                            
					l1="  .oooooo.     "          
					l2=" d8P\'  `Y8b    "          
					l3="888      888   "          
					l4="888      888   "          
					l5="888      888   "          
					l6="`88b    d88\'   "          
					l7=" `Y8bood8P\'    "          
					l8="               "          
					l9="               "          
					l0="               "
			elif le=="P":
					                            
					l1="ooooooooo.     "          
					l2="`888   `Y88.   "          
					l3=" 888   .d88\'   "          
					l4=" 888ooo88P\'    "          
					l5=" 888           "          
					l6=" 888           "          
					l7="o888o          "          
					l8="               "          
					l9="               "          
					l0="               "
			elif le=="Q":
					                            
					l1="  .oooooo.        "       
					l2=" d8P\'  `Y8b       "       
					l3="888      888      "       
					l4="888   qq 888      "       
					l5="888    qq888      "       
					l6="`88b    qd88b     "       
					l7=" `Y8bood8P\'Ybd\'   "       
					l8="                  "       
					l9="                  "       
					l0="                  "
			elif le=="R":
					                            
					l1="ooooooooo.    "          
					l2="`888   `Y88.  "           
					l3=" 888   .d88\'  "           
					l4=" 888ooo88P\'   "           
					l5=" 888`88b.     "           
					l6=" 888  `88b.   "           
					l7="o888o  o888o  "           
					l8="              "           
					l9="              "           
					l0="              "
			elif le=="S":
					                            
					l1=" .oooooo..o  "            
					l2="d8P\'    `Y8  "            
					l3="Y88bo.       "            
					l4=" `\"Y8888o.   "            
					l5="     `\"Y88b  "            
					l6="oo     .d8P  "            
					l7="8\"\"88888P\'   "            
					l8="             "            
					l9="             "            
					l0="             " 
			elif le=="T":
					                            
					l1="ooooooooooooo  "          
					l2="8\'   888   `8  "          
					l3="     888       "          
					l4="     888       "          
					l5="     888       "          
					l6="     888       "          
					l7="    o888o      "          
					l8="               "          
					l9="               "          
					l0="               "
			elif le=="U":
					                            
					l1="ooooo     ooo  "          
					l2="`888\'     `8\'  "          
					l3=" 888       8   "          
					l4=" 888       8   "          
					l5=" 888       8   "          
					l6=" `88.    .8\'   "          
					l7="   `YbodP\'     "          
					l8="               "          
					l9="               "          
					l0="               "
			elif le=="V":
					                            
					l1="oooooo     oooo  "        
					l2=" `888.     .8\'   "        
					l3="  `888.   .8\'    "        
					l4="   `888. .8\'     "        
					l5="    `888.8\'      "        
					l6="     `888\'       "        
					l7="      `8\'        "        
					l8="                 "        
					l9="                 "        
					l0="                 "
			elif le=="W":
					                            
					l1="oooooo   oooooo     oooo "
					l2=" `888.    `888.     .8\'  "
					l3="  `888.   .8888.   .8\'   "
					l4="   `888  .8\'`888. .8\'    "
					l5="    `888.8\'  `888.8\'     "
					l6="     `888\'    `888\'      "
					l7="      `8\'      `8\'       "
					l8="                         "
					l9="                         "
					l0="                         "
			elif le=="X":
					                            
					l1="ooooooo  ooooo  "         
					l2=" `8888    d8\'   "         
					l3="   Y888..8P     "         
					l4="    `8888\'      "         
					l5="   .8PY888.     "         
					l6="  d8\'  `888b    "         
					l7="o888o  o88888o  "         
					l8="                "         
					l9="                "         
					l0="                "
			elif le=="Y":
					                            
					l1="oooooo   oooo  "           
					l2=" `888.   .8\'   "           
					l3="  `888. .8\'    "           
					l4="   `888.8\'     "           
					l5="    `888\'      "           
					l6="     888       "           
					l7="    o888o      "           
					l8="               "           
					l9="               "           
					l0="               "
			elif le=="Z":
					                            
					l1=" oooooooooooo  "          
					l2="d\'\"\"\"\"\"\"d888\'  "          
					l3="      .888P    "          
					l4="     d888\'     "          
					l5="   .888P       "          
					l6="  d888\'    .P  "          
					l7=".8888888888P   "            
					l8="               "             
					l9="               "            
					l0="               "
			elif le=="1":
				   
					l1="     .o      "    
					l2="   o888      "    
					l3="    888      "    
					l4="    888      "    
					l5="    888      "    
					l6="    888      "    
					l7="   o888o     "    
					l8="             "    
					l9="             "    
					l0="             " 
			elif le=="2":
					   
					l1="  .oooo.     "    
					l2=".dP\"\"Y88b    "    
					l3="      ]8P\'   "    
					l4="    .d8P\'    "    
					l5="  .dP\'       "    
					l6=".oP     .o   "    
					l7="8888888888   "    
					l8="             "    
					l9="             "    
					l0="             "    
			elif le=="3":
					   
					l1="  .oooo.     "    
					l2=".dP\"\"Y88b    "    
					l3="      ]8P\'   "    
					l4="    <88b.    "    
					l5="     `88b.   "    
					l6="o.   .88P    "    
					l7="`8bd88P\'     "    
					l8="             "    
					l9="             "    
					l0="             "
			elif le=="4":
					   
					l1="      .o     "    
					l2="    .d88     "    
					l3="  .d\'888     "    
					l4=".d\'  888     "    
					l5="88ooo888oo   "    
					l6="     888     "    
					l7="    o888o    "    
					l8="             "    
					l9="             "    
					l0="             "    
			elif le=="5":
					   
					l1="  oooooooo   "    
					l2=" dP\"\"\"\"\"\"\"   "    
					l3="d88888b.     "    
					l4="    `Y88b    "    
					l5="      ]88    "    
					l6="o.   .88P    "    
					l7="`8bd88P\'     "    
					l8="             "    
					l9="             "    
					l0="             "    
			elif le=="6":
					   
					l1="    .ooo     "    
					l2="  .88\'       "    
					l3=" d88\'        "    
					l4="d888P\"Ybo.   "    
					l5="Y88[   ]88   "    
					l6="`Y88   88P   "    
					l7=" `88bod8\'    "    
					l8="             "    
					l9="             "    
					l0="             "    
			elif le=="7":
					   
					l1=" ooooooooo   "    
					l2="d\"\"\"\"\"\"\"8\'   "   
					l3="      .8\'    "    
					l4="     .8\'     "    
					l5="    .8\'      "    
					l6="   .8\'       "    
					l7="  .8\'        "    
					l8="             "    
					l9="             "    
					l0="             "    
			elif le=="8":
					   
					l1=" .ooooo.     "    
					l2="d88\'   `8.   "    
					l3="Y88..  .8\'   "    
					l4=" `88888b.    "    
					l5=".8\'  ``88b   "    
					l6="`8.   .88P   "    
					l7=" `boood8\'    "    
					l8="             "    
					l9="             "    
					l0="             "    
			elif le=="9":
					   
					l1=" .ooooo.     "    
					l2="888\' `Y88.   "    
					l3="888    888   "    
					l4=" `Vbood888   "    
					l5="      888\'   "    
					l6="    .88P\'    "    
					l7="  .oP\'       "    
					l8="             "    
					l9="             "    
					l0="             "    
			elif le=="0":
					   
					l1="  .oooo.     "
					l2=" d8P\'`Y8b    "  
					l3="888    888   "  
					l4="888    888   "  
					l5="888    888   "  
					l6="`88b  d88\'   "  
					l7=" `Y8bd8P\'    "  
					l8="             "   
					l9="             "    
					l0="             "

			f1=f1+l1
			f2=f2+l2
			f3=f3+l3
			f4=f4+l4
			f5=f5+l5
			f6=f6+l6
			f7=f7+l7
			f8=f8+l8
			f9=f9+l9
			f0=f0+l0

			lp=len(f1)

		sy=int(((sizey-14)/2)-5)
		for i in range (sy):
			print (" ")

		sx=int((sizex-lp-6)/2)

		ts = int(time.time())
		st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
		mx=int(sizex-88)

		et=str(ts-ts1)
		mq=(int(sizex)-(len(et)+26))
		mp=(int(sizex)-(len(et)+39))
		oo=int(mq/2)
		op=int(mp/2)

		print ("    Started processing at - ", st1, (" ")*(mx), "Now Time - ", st)
		print (" ")
		print (" ")
		print (" ")
		print (" ")
		print (" ")
		print ((" ")*sx, "  ", ("█")*(lp+6))
		print ((" ")*sx, " ██  ", (" ")*lp, "  ██       ")
		print ((" ")*sx, (" ██  "), f1, ("  ██ "))
		print ((" ")*sx, (" ██  "), f2, ("  ██ "))
		print ((" ")*sx, (" ██  "), f3, ("  ██ "))
		print ((" ")*sx, (" ██  "), f4, ("  ██ "))
		print ((" ")*sx, (" ██  "), f5, ("  ██ "))
		print ((" ")*sx, (" ██  "), f6, ("  ██ "))
		print ((" ")*sx, (" ██  "), f7, ("  ██ "))
		print ((" ")*sx, (" ██  "), f8, ("  ██ "))
		print ((" ")*sx, (" ██  "), f9, ("  ██ "))
		print ((" ")*sx, (" ██  "), f0, ("  ██ "))
		print ((" ")*sx, " ██  ", (" ")*lp, "  ██       ")
		print ((" ")*sx, "  ", ("█")*(lp+6))
		print ("  ")
		print ("  ")
		print (" ")
		print (" ")
		print (" ")

		etm=int(int(et)/60)
		ets=int(int(et)-etm*60)
		if etm==0:
			print (((" ")*oo), " Elapsed Time  :  ", ets, " seconds")
		elif etm>0:
			print (((" ")*op), " Elapsed Time  :  ", etm, " minutes and ", ets, " seconds")

		sleep(0.001)
		clear()
	
	ts2 = int(time.time())
	st2 = datetime.datetime.fromtimestamp(ts2).strftime('%Y-%m-%d %H:%M:%S')
	
	print ("      Started Time  :  ", st1, )
	print ("      Ended Time    : ", st2)
	print ("      Elapsed Time  :  ", et, " seconds")

	print("      Do you want to save this list into a text file?")
	q1=input("            >   ")
	if q1=="y" or q1=="yes" or q1=="Y" or q1=="Yes" or q1=="YES":
		f = open('generated.txt', 'w')
		for items in fi:
			simplejson.dump(items, f)
		f.close()

	# ending program
	const=0
