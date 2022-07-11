import os
import time

w = True
file = "exit"
leave = "^C"

while w:
	os.system("clear")
	os.system("cat ascii.txt")
	try :
		q = input(">>>")
		os.system(q)
		time.sleep(2)
	except:
		print("salut, a plus tard")
		break


	if q == file :
		break

