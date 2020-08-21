import os
import pyttsx3 as tlk
import time
import calendar


tlk.speak('hello, i am sims, How can i help?')
while True:
	print('You:', end='')
	x = input()
	if ('run' in x) and ('notepad' in x): #notepad
		tlk.speak("Launching Notepad....")
		print("sism:Launched Notepad....")
		os.system('notepad')	

	elif (('run' in x) and ('chrome' in x)): #chrome
		tlk.speak("Launching chrome....")
		print("sism:Launched Chrome....")
		os.system('chrome')

	elif (('run' in x) and ('paint' in x)): #paint
		tlk.speak("Launching paint....")
		print("sism:Launched Paint....")
		os.system('mspaint')

	elif (('dir' in x) or ('list' in x)): #Dir to show all files in current directory
		os.system('dir')

	elif (('run' in x) and ('cmd' in x)): #cmd
		tlk.speak("Launching command prompt....")
		print("sism:Launched Cmd....")
		os.system('cmd')

	elif (('run' in x) and (('virtual box' in x) or ('virtualbox' in x))): #virtualbox
		tlk.speak("Launching virtaul box....")
		print("sism:Launched VirtualBox....")
		os.system('VirtualBox')

	elif (('run' in x) and ('telegram' in x) ): #Telegram
		tlk.speak("Launching telegram....")
		print("sism:Launched Telegram....")
		os.system('telegram')

	elif (('run' in x) and ('android studio' in x) ): #android studio
		tlk.speak("Launching android studio....")
		print("sism:Launched Aandroid Studio....")
		os.system('studio64')		

	elif (('time' in x) or ('date' in x)): #date
		localtime = time.asctime( time.localtime(time.time()) )
		print ("Local current time :",localtime)

	elif ('calendar' in x):  #calendar
		tlk.speak("which year's calendar you want to see, enter year ....")
		yr = input("sism:Enter year-")
		tlk.speak("which month you want to see in "+yr+", enter month ....")
		mn = input("sism:Enter month-")
		cal = calendar.month(int(yr),int(mn))
		print ("sism:Here is the calendar of "+mn+"th month from "+yr+" year:\n",cal)
		tlk.speak("Here is the calendar of "+mn+"th month from "+yr+" year ....")	

	elif (('say' in x) or ('talk' in x) ): #Telegram
		tlk.speak("What you want to hear from me? Enter here")
		spk = input("sism:Enter here-")		
		tlk.speak(spk)

	elif (('exit' in x) or ('quit' in x) or ('end' in x) or ('bye' in x)):  #exit
		tlk.speak("Bye Bye! It was great experince with you, come soon")
		break
	
	else:
		tlk.speak("You entered, "+x+", i can't to anything for this")
