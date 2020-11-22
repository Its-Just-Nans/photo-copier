import sys
import socket
import time
import os
import tkinter as tk
import turtle
import string
import tkinter.filedialog

global app # tkinter
import shutil
import datetime
import time

global info
info = {}
info['taillePolice'] = 15
info['police'] = 'Segoe UI'
info['log'] = ''
def dispMenu():
	global app
	

def transfer(step):
	global app
	app.frame.destroy()
	app.frame = tk.Frame(app, height = 50, borderwidth = 1,relief="ridge")
	app.frame.grid(row=1, rowspan=1, column=1)
	if step == 0:
		app.frame.start = tk.Button(app.frame, text="Transférer des photos", font=(info['police'], info['taillePolice']), fg="blue", command=lambda: transfer(1))
		app.frame.start.grid(row=1, column=1)
	elif step == 1:
		app.frame.text = tk.Label(app.frame, text='Choisir le dossier de destination', font=(info['police'], info['taillePolice']),)
		app.frame.text.grid(row=1, column=1, columnspan=2)
		app.frame.buttonAuto = tk.Button(app.frame, text="Choix auto par le logiciels", font=(info['police'], info['taillePolice']), fg="blue", command=lambda:choixDest())
		app.frame.buttonAuto.grid(row=2,column=1)
		app.frame.buttonManu = tk.Button(app.frame, text="Choix Manuel", font=(info['police'], info['taillePolice']), fg="blue", command=lambda:choixFenetre('fileDest', 2))
		app.frame.buttonManu.grid(row=2,column=2)
		app.frame.buttonNext = tk.Button(app.frame, text="Suivant", font=(info['police'], info['taillePolice']), fg="blue", command=lambda:transfer(2))
		app.frame.buttonNext.grid(row=3,column=2)
		app.frame.buttonBefore = tk.Button(app.frame, text="Précédent", font=(info['police'], info['taillePolice']), fg="blue", command=lambda:transfer(0))
		app.frame.buttonBefore.grid(row=3, column=1)
	elif step == 2:
		try:
			if info['fileDest'] != '':
				print(info['fileDest'])
				app.frame.text = tk.Label(app.frame, text='Choisir le dossier où  sont les photos', font=(info['police'], info['taillePolice']))
				app.frame.text.grid(row=1, column=1, columnspan=2)
				app.frame.buttonAuto = tk.Button(app.frame, text="Choix auto par le logiciels", font=(info['police'], info['taillePolice']), fg="blue", command=lambda:dispPhoto())
				app.frame.buttonAuto.grid(row=2,column=1)
				app.frame.buttonManu = tk.Button(app.frame, text="Choix Manuel", font=(info['police'], info['taillePolice']), fg="blue", command=lambda:choixFenetre('fileSrc', 3))
				app.frame.buttonManu.grid(row=2,column=2)
				app.frame.buttonNext = tk.Button(app.frame, text="Suivant", font=(info['police'], info['taillePolice']), fg="blue", command=lambda:transfer(3))
				app.frame.buttonNext.grid(row=3,column=2)
				app.frame.buttonBefore = tk.Button(app.frame, text="Précédent", font=(info['police'], info['taillePolice']), fg="blue", command=lambda:transfer(1))
				app.frame.buttonBefore.grid(row=3, column=1)
		except KeyError:
			transfer(1)
	elif step == 3:
		try:
			if info['fileSrc'] != '':
				print(info['fileSrc'])
				app.frame.text = tk.Label(app.frame, text='Choisir le nom du dossier', font=(info['police'], info['taillePolice']))
				app.frame.text.grid(row=1, column=1, columnspan=2)
				app.frame.fichierAppareil = tk.Entry(app.frame, width=20, font=(info['police'], info['taillePolice']))
				app.frame.fichierAppareil.grid(row=2, column=1, columnspan=2)
				app.frame.buttonNext = tk.Button(app.frame, text="Suivant", font=(info['police'], info['taillePolice']), fg="blue", command=lambda:setNameOfDir())
				app.frame.buttonNext.grid(row=3, column=2)
				app.frame.buttonBefore = tk.Button(app.frame, text="Précédent", font=(info['police'], info['taillePolice']), fg="blue", command=lambda:transfer(2))
				app.frame.buttonBefore.grid(row=3, column=1)
			else:
				transfer(2)
		except KeyError:
			transfer(2)
	elif step == 4:
		try:
			if info['dirName'] != '':
				#Ecrire ce qu'il va faire
				app.frame.text = tk.Label(app.frame, text='Choisir le nom du dossier', font=(info['police'], info['taillePolice']))
				app.frame.text.grid(row=1, column=1, columnspan=2)
				app.frame.buttonAuto = tk.Button(app.frame, text="Copier les fichiers", font=(info['police'], info['taillePolice']), fg="blue", command=lambda:copy())
				app.frame.buttonAuto.grid(row=2, column=1, columnspan=2)
				app.frame.buttonNext = tk.Button(app.frame, text="Recommencer", font=(info['police'], info['taillePolice']), fg="blue", command=lambda:transfer(0))
				app.frame.buttonNext.grid(row=3, column=2)
				app.frame.buttonBefore = tk.Button(app.frame, text="Précédent", font=(info['police'], info['taillePolice']), fg="blue", command=lambda:transfer(3))
				app.frame.buttonBefore.grid(row=3, column=1)
			else :
				transfer(3)
		except KeyError:
			transfer(3)

def choixFenetre(attribut, nextStep):
	global info
	app.filename = tkinter.filedialog.askdirectory(initialdir='c:/', title='Choose file')
	if app.filename != '':
		info[attribut] = app.filename + '/'
		addToLog(info[attribut], True, True)
		transfer(nextStep)
	else:
		pass
def addToLog(text, sautLigne, render):
	info['log'] = info['log'] + text
	if sautLigne:
		info['log'] = info['log'] + '\n'
	if render:
		app.frameLog.logtTXT['text'] = info['log']
		app.update_idletasks()


def setNameOfDir():
	global info
	info['dirName'] = app.frame.fichierAppareil.get()
	if ' ' in info['dirName']:
		info['dirName'] = '_'.join(info['dirName'].split(' '))
	
	date = getDate(os.path.getmtime(info['fileSrc']))
	info['dateDirName'] =  date + '_' + info['dirName']
	info['pathDest'] = info['fileDest'] + info['dateDirName'] + '/'
	try:
		if not os.path.exists(info['pathDest']):
			os.mkdir(info['pathDest'])
			addToLog("Directory '" + info['pathDest'] + "' Created ", True, True)
	except FileExistsError:
		addToLog("Directory '" + info['pathDest'] + "' already exists", True, True)
	transfer(4)


def choixDest():
	#get user name
	# create file in desktop
	#info['fileDestination'] = final+'/'
	pass

def choixSrc():
	allLetter = string.ascii_uppercase
	allLetter = allLetter.replace('C', '')
	drives = []
	for l in allLetter:
		if os.path.exists(l+':\\'):
			drives.append(l)
			print('Il y a un appareil connecté avec ' + l + ':\\')
	if len(drives) == 1:
		files = os.listdir(drives[0]+':\\')

def copy():
	listOfFile = os.listdir(info['fileSrc'])
	count = 0
	for element in listOfFile:
		extensionOfFile = element[-3]
		if element[-3] == '.':
			extensionOfFile = element[-3:]
		elif element[-4] == '.':
			extensionOfFile = element[-4:]
		elif element[-5] == '.':
			extensionOfFile = element[-5:]
		count = count + 1
		newLinkToSrc = info['fileSrc'] + element
		dateOfFile = getDate(os.path.getmtime(newLinkToSrc))
		newLinkToDest = info['pathDest'] + dateOfFile + "_" + info['dirName'] + "_{:0003d}".format(count) + extensionOfFile
		#print('We are going to copy '+newLinkToSrc+' > '+newLinkToDest)
		try:
			addToLog("[Copy] '"+ newLinkToSrc + "' -> '" + newLinkToDest + "'", False, False)
			if not os.path.exists(newLinkToDest):
				shutil.copy2(newLinkToSrc, newLinkToDest)
				addToLog(" [OK]", True, False)
			else :
				addToLog(" [KO]", True, False)
				addToLog("[Error] '" + newLinkToDest + "' existe déjà", True, False)
		except Exception as e:
			addToLog(" [KO]", False, False)
			addToLog(e.__class__.__name__, True, False)
		addToLog('', False, True)

def destroyTkinter():
	app.destroy()


def getDate(timestamp):
	date = datetime.datetime.fromtimestamp(timestamp)
	return date.strftime("%Y-%m-%d")


app = tk.Tk()
app.title('PhotoCopy')
app.configure(bg='white')

app.quit = tk.Button(app, text="Quitter", fg="red", command=lambda :destroyTkinter())
app.quit.grid(row=2, column=1,columnspan=3)
app.frameLog = tk.Frame(app, height=50, bg='white', width=200, borderwidth = 1,relief="ridge")
app.frameLog.grid(row=1, column=2)
app.frameLog.log = tk.Label(app.frameLog, text='Log', font=(info['police'], info['taillePolice']), bg='white')
app.frameLog.log.grid(row=1, column=1)
app.frameLog.logtTXT = tk.Label(app.frameLog, text=info['log'], font=(info['police'], 10), bg='white', justify='left')
app.frameLog.logtTXT.grid(row=2, column=1)
app.frame = tk.Frame(app, height = 50, borderwidth = 1,relief="ridge")
app.frame.grid(row=1, column=1)
transfer(0)
app.mainloop()
		
sys.exit(0)