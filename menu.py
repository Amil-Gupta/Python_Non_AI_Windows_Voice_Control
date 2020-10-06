import os
import pyaudio
import speech_recognition as sr
import pyttsx3

r=sr.Recognizer()
r.dynamic_energy_threshold = False 
def saykube():
    with sr.Microphone() as source:
        print('Say the command')
        command=r.recognize_google(r.listen(source,timeout=5)) 
        print('Command heard')

    command=command.lower()
    print(command)
    os.system(command)

def typekube():
    command=input("Enter the command: ")
    os.system(command)

def typeeks():
    command=input("Enter the command: ")
    os.system(command)

def sayeks():
    with sr.Microphone() as source:
        print('Say the command')
        command=r.recognize_google(r.listen(source,timeout=5)) 
        print('Command heard')

    command=command.lower()
    print(command)
    os.system(command)

def main(): 
	username=""
	command=""
	loc=""
	name=""
	valid=False  
	engine= pyttsx3.init()
	engine.setProperty('voice',engine.getProperty('voices')[1].id) 
	engine.setProperty('rate',engine.getProperty('rate')-10)  
	os.system("cls")
	pyttsx3.speak("good day")
	pyttsx3.speak("what should i call you")
	print("Your name?")  
	username=input()
	pyttsx3.speak("okay")
	pyttsx3.speak(username)
	os.system("cls")
	while(True):
		valid=False
		pyttsx3.speak("what do you want me to do")
		with sr.Microphone() as source:
			print('What do you want me to do?')
			command=r.recognize_google(r.listen(source,timeout=5)) 
			print('Command heard')
		command=command.lower()
		if not (("don't" in command) or ("do not" in command)):
			if "curl" in command:
				pyttsx3.speak("Enter url")
				print("Enter URL",end=':')
				loc=input()
				pyttsx3.speak("Browsing via curl")
				os.system('curl '+loc)
				valid=True
			if "terminal" in command or "prompt" in command:
				pyttsx3.speak("enter the name of the terminal")
				name=input()
				pyttsx3.speak("opening new command terminal")
				os.system('start "'+name+'"')
				valid=True
			if "github" in command:
				pyttsx3.speak("opening github")
				os.system('start chrome "github.com"')
				valid=True
			if "whatsapp" in command:
				pyttsx3.speak("opening whatsapp web")
				os.system('start chrome "web.whatsapp.com"')
				valid=True
			if "facebook" in command:
				pyttsx3.speak("opening facebook")
				os.system('start chrome "facebook.com"')
				valid=True
			if "linkedin" in command or "linked in" in command:
				pyttsx3.speak("opening linked in")
				os.system('start chrome "linkedin.com"')
				valid=True
			if "nothing" in command or "talk" in command:
				pyttsx3.speak("sorry")
				pyttsx3.speak("i cannot converse yet")
				continue
			if "note" in command or "edit" in command or (("create" in command or "make" in command or "view" in command or "open" in command) and ("file" in command)) :
				print("Enter filename or address(for untitled file in current directory,just press enter)",end=':')
				pyttsx3.speak("Enter filename or address")
				loc=input()
				pyttsx3.speak("opening notepad")
				os.system("start notepad "+loc)
				valid=True
			if ("chrome" in command) or ("browser" in command) or ("browse" in command):
				print("Enter url(For no url,just press enter)",end=':')
				pyttsx3.speak("Enter site address")
				loc=input()
				pyttsx3.speak("opening google chrome")
				os.system("start chrome "+loc)
				valid=True
			if ("paint" in command) or ("draw" in command):
				pyttsx3.speak("opening microsoft paint")
				os.system("start mspaint")
				valid=True
			if ("wmp" in command) or ("player" in command):
				pyttsx3.speak("opening windows media player")
				os.system("start wmplayer")
				valid=True
			if ("date" in command):
				pyttsx3.speak("the date details are")
				os.system("date /t")
				valid=True
			if ("time" in command):
				pyttsx3.speak("the time details are")
				os.system("time")
				valid=True
			if ("list" in command) or ("dir" in command) or ("directory" in command) or ("go" in command):
				print("Enter target location",end=':')
				loc=input()
				pyttsx3.speak("listing contents")
				os.system("dir "+loc)
				valid=True
			if ("del" in command) or ("remove" in command) or ("rm" in command):
				pyttsx3.speak('Enter target file name')
				print("Enter target file name",end=':')
				loc=input()
				pyttsx3.speak("deleting file")
				os.system("del "+loc)
				valid=True
			if (("create" in command or "make" in command) and ("folder" in command or "directory" in command)):
				print("Enter location")
				loc=input()
				print("Enter folder/directory name")
				name=input()
				pyttsx3.speak("creating folder")
				os.system("mkdir "+name)
				valid=True
			if "camera" in command:
				pyttsx3.speak("opening the camera")
				os.system("start microsoft.windows.camera:")
				valid=True
			if "setting" in command:
				pyttsx3.speak("opening settings")
				os.system("start ms-settings:")
				valid=True
			if "note" in command or "edit" in command or "create" in command or "view" in command or "open" in command:
				if "image" in command or "img" in command or "pic" in command:
					pyttsx3.speak("these are the files available in the current folder")
					os.system("dir")
					pyttsx3.speak("Enter image name or address")
					print("\n\nEnter image name or address",end=':')
					loc=input()
					pyttsx3.speak("opening image")
					os.system(loc+name)
					valid=True
				if "audio" in command or "sound" in command or "music" in command or "listen" in command or "play" in command:
					pyttsx3.speak("these are the files available in the current folder")
					os.system(dir)
					pyttsx3.speak("enter the name of the audio file")
					print("Enter audio file name",end=':')
					loc=input()
					pyttsx3.speak("opening audio")
					os.system(name)
					valid=True
			if "execute" in command or "command" in command or "run" in command:
				pyttsx3.speak("which command do you want to execute")
				print("Enter command",end=':')
				name=input()
				os.system(name)
				valid=True
			if "explore" in command or "goto" in command or "go to" in command:
				pyttsx3.speak("opening file explorer")
				os.system("explorer")
				valid=True
			if (('minikube' in command) or ('mini cube' in command)) and ('start' in command):
				os.system("minikube start")
				valid=True

			if (('minikube' in command) or ('mini cube' in command)) and ('dashboard' in command):
				os.system("minikube dashboard")
				valid=True

			if (('minikube' in command) or ('Mini cube' in command)) and ('IP' in command):
				os.system("minikube ip")
				valid=True
        
			if ('kubectl' in command) or ('kubernetes' in command):
				print("Do you want to type the command or say it?")
				pyttsx3.speak("Do you want to type the command or say it?")
				while True:
					with sr.Microphone() as source:
						command=r.recognize_google(r.listen(source,timeout=5)) 
						print('Command heard')
					command=command.lower()
					if 'type' in command:
						print("Type it:")
						pyttsx3.speak("Type it")
						typekube()
						break

					elif 'say' in command:
						print("Say it:")
						pyttsx3.speak("Say it")
						saykube()
						break

					else:
						print("Please say it again...")
						pyttsx3.speak("Please say it again...")
				valid=True

			if ('IP' in command) or ('IP' in command and 'configuration' in command):
			    os.system("ipconfig")
			    valid=True

			elif ('eks' in command) or ('eksctl' in command) or ('Elastic Kubernetes Service' in command):
				print("Do you want to type the command or say it?")
				pyttsx3.speak("Do you want to type the command or say it?")
				while True:
					with sr.Microphone() as source:
						command=r.recognize_google(r.listen(source,timeout=5)) 
						print('Command heard')
					if 'type' in command:
						print("Type it:")
						pyttsx3.speak("Type it")
						typeeks()
						break

					elif 'say' in command:
						print("Say it:")
						pyttsx3.speak("Say it")
						sayeks()
						break

					else:
						print("Please say it again...")
						pyttsx3.speak("Please say it again...")

			if ("exit" in command) or ("stop" in command) or ("bye" in command):
				pyttsx3.speak("bye")
				pyttsx3.speak(username)
				pyttsx3.speak("have a great day ahead")
				break
			if not valid:
				pyttsx3.speak("sorry,i did not understand the command")
				pyttsx3.speak("please try again")
				continue
			pyttsx3.speak("will that be all")
			with sr.Microphone() as source:
    				print('Will that be all?')
    				command=r.recognize_google(r.listen(source))
    				print('Command heard')
			if "yes" in command or command=="y":
				pyttsx3.speak("bye")
				pyttsx3.speak(username)
				pyttsx3.speak("have a great day ahead")
				break
			elif "no" in command or command=="n":
				pyttsx3.speak("okay")
			else:
				pyttsx3.speak("I did not understand that command")
				pyttsx3.speak("but i am optimistic")
			pyttsx3.speak("lets go again")
	os.system("cls")


if __name__ == "__main__":
	main()