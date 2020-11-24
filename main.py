import sys
import socket
import time
import os
import tkinter as tk
import turtle
import string
import tkinter.filedialog
import tkinter.scrolledtext

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
	app.frame = tk.Frame(app, height = 50, borderwidth = 1, relief="ridge", bg="white")
	app.frame.grid(row=0, column=0, sticky="nesw")
	app.frame.grid_columnconfigure(0, weight=1)
	app.frame.grid_columnconfigure(1, weight=1)
	app.frame.grid_columnconfigure(2, weight=1)
	app.frame.grid_rowconfigure(0, weight=1)
	app.frame.grid_rowconfigure(1, weight=1)
	app.frame.grid_rowconfigure(2, weight=1)
	if step == 0:
		app.frame.start = tk.Button(app.frame, text="Transférer des photos", font=(info['police'], info['taillePolice']), fg="blue", command=lambda: transfer(1))
		app.frame.start.grid(row=0, column=0, rowspan="3", columnspan="3", sticky="nesw")
	elif step == 1:
		app.frame.text = tk.Label(app.frame, text='Choisir le dossier de destination', font=(info['police'], info['taillePolice']),)
		app.frame.text.grid(row=0, column=0, columnspan=3, sticky="nesw")
		app.frame.buttonAuto = tk.Button(app.frame, text="Choix auto par le logiciels", font=(info['police'], info['taillePolice']), fg="blue", command=lambda:choixDest())
		app.frame.buttonAuto.grid(row=1, column=0, sticky="nesw")
		app.frame.buttonManu = tk.Button(app.frame, text="Choix Manuel", font=(info['police'], info['taillePolice']), fg="blue", command=lambda:choixFenetre('fileDest', 2))
		app.frame.buttonManu.grid(row=1, column=2, sticky="nesw")
		app.frame.buttonBefore = tk.Button(app.frame, text="Précédent", font=(info['police'], info['taillePolice']), fg="blue", command=lambda:transfer(0))
		app.frame.buttonBefore.grid(row=2, column=0, sticky="nesw")
		app.frame.buttonNext = tk.Button(app.frame, text="Suivant", font=(info['police'], info['taillePolice']), fg="blue", command=lambda:transfer(2))
		app.frame.buttonNext.grid(row=2, column=2, sticky="nesw")
	elif step == 2:
		try:
			if info['fileDest'] != '':
				print(info['fileDest'])
				app.frame.text = tk.Label(app.frame, text='Choisir le dossier où  sont les photos', font=(info['police'], info['taillePolice']))
				app.frame.text.grid(row=0, column=0, columnspan=3, sticky="nesw")
				app.frame.buttonAuto = tk.Button(app.frame, text="Choix auto par le logiciels", font=(info['police'], info['taillePolice']), fg="blue", command=lambda:choixSrc())
				app.frame.buttonAuto.grid(row=1 ,column=0, sticky="nesw")
				app.frame.buttonManu = tk.Button(app.frame, text="Choix Manuel", font=(info['police'], info['taillePolice']), fg="blue", command=lambda:choixFenetre('fileSrc', 3))
				app.frame.buttonManu.grid(row=1, column=2, sticky="nesw")
				app.frame.buttonBefore = tk.Button(app.frame, text="Précédent", font=(info['police'], info['taillePolice']), fg="blue", command=lambda:transfer(1))
				app.frame.buttonBefore.grid(row=2, column=0, sticky="nesw")
				app.frame.buttonNext = tk.Button(app.frame, text="Suivant", font=(info['police'], info['taillePolice']), fg="blue", command=lambda:transfer(3))
				app.frame.buttonNext.grid(row=2, column=2, sticky="nesw")
		except KeyError:
			transfer(1)
	elif step == 3:
		try:
			if info['fileSrc'] != '':
				print(info['fileSrc'])
				app.frame.text = tk.Label(app.frame, text='Choisir le nom du dossier', font=(info['police'], info['taillePolice']))
				app.frame.text.grid(row=0, column=0, columnspan=3, sticky="nesw")
				app.frame.fichierAppareil = tk.Entry(app.frame, width=20, font=(info['police'], info['taillePolice']))
				app.frame.fichierAppareil.grid(row=1 ,column=0, columnspan=3)
				app.frame.buttonBefore = tk.Button(app.frame, text="Précédent", font=(info['police'], info['taillePolice']), fg="blue", command=lambda:transfer(2))
				app.frame.buttonBefore.grid(row=2, column=0, sticky="nesw")
				app.frame.buttonNext = tk.Button(app.frame, text="Suivant", font=(info['police'], info['taillePolice']), fg="blue", command=lambda:setNameOfDir())
				app.frame.buttonNext.grid(row=2, column=2, sticky="nesw")
			else:
				transfer(2)
		except KeyError:
			transfer(2)
	elif step == 4:
		try:
			if info['dirName'] != '':
				#Ecrire ce qu'il va faire
				app.frame.text = tk.Label(app.frame, text='Choisir le nom du dossier', font=(info['police'], info['taillePolice']))
				app.frame.text.grid(row=0, column=0, columnspan=3, sticky="nesw")
				app.frame.buttonAuto = tk.Button(app.frame, text="Copier les fichiers", font=(info['police'], info['taillePolice']), fg="blue", command=lambda:copy())
				app.frame.buttonAuto.grid(row=1 ,column=0, columnspan=3)
				app.frame.buttonNext = tk.Button(app.frame, text="Recommencer", font=(info['police'], info['taillePolice']), fg="blue", command=lambda:transfer(0))
				app.frame.buttonNext.grid(row=2, column=0, sticky="nesw")
				app.frame.buttonBefore = tk.Button(app.frame, text="Précédent", font=(info['police'], info['taillePolice']), fg="blue", command=lambda:transfer(3))
				app.frame.buttonBefore.grid(row=2, column=2, sticky="nesw")
			else :
				transfer(3)
		except KeyError:
			transfer(3)
	elif step == 5:
		app.frame.text = tk.Label(app.frame, text='OK', font=(info['police'], info['taillePolice']))
		app.frame.text.grid(row=0, column=0, columnspan=3, sticky="nesw")
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
	if sautLigne:
		text = text + '\n'
	if render:
		pass
	app.frameLog.logtTXT.insert(tkinter.END, text)
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
	username = os.getlogin()
	pathToScript = os.path.realpath(__file__).split('\\')

	info['fileDest'] = pathToScript[0]+'/'
	if os.path.exists(info['fileDest'] + 'Users/'):
		info['fileDest'] = info['fileDest'] + 'Users/'
		if os.path.exists(info['fileDest'] + username + '/'):
			info['fileDest'] = info['fileDest'] + username + '/'
			if os.path.exists(info['fileDest'] + 'Pictures' + '/'):
				info['fileDest'] = info['fileDest'] + 'Pictures' + '/'
	else:
		print("error ?")
	addToLog(info['fileDest'], True, True)
	transfer(2)

def choixSrc():
	popUp = tk.Tk()
	popUp.title('PhotoCopy')
	popUp.geometry('800x600')
	popUp.quitter = tk.Button(popUp, text="Quitter", fg="red", command=lambda : popUp.quit())
	popUp.quitter.grid(row=1, column=0, columnspan=2)
	popUp.mainloop()
	popUp.destroy()
	allLetter = string.ascii_uppercase
	allLetter = allLetter.replace('C', '')
	drives = []
	for l in allLetter:
		if os.path.exists(l+':\\'):
			drives.append(l)
			print('Il y a un appareil connecté avec ' + l + ':\\')
	allLetter = len(drives)
	if allLetter == 0:
		print('Pas d\'appareil trouvé')
	elif allLetter == 1:
		files = os.listdir(drives[0]+':\\')
		#found img
	else :
		choixFenetre('fileSrc', 3)


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
	transfer(5)

def destroyTkinter():
	app.destroy()


def getDate(timestamp):
	date = datetime.datetime.fromtimestamp(timestamp)
	return date.strftime("%Y-%m-%d")


app = tk.Tk()
app.title('PhotoCopy')
app.geometry('800x600')
app.configure(bg='white')
app.grid_columnconfigure(0, weight=1, minsize="200")
app.grid_columnconfigure(1, weight=1, minsize="400")
app.grid_rowconfigure(0, weight=3, minsize="100")
app.grid_rowconfigure(1, weight=1, minsize="32")
app.quitter = tk.Button(app, text="Quitter", fg="red", command=lambda :destroyTkinter())
app.quitter.grid(row=1, column=0, columnspan=2)

app.frameLog = tk.Frame(app, height=50, bg='blue', width=200, borderwidth = 1, relief="ridge")
app.frameLog.grid(row=0, column=1, sticky="nesw")
app.frameLog.grid_columnconfigure(0, weight=1)
app.frameLog.grid_rowconfigure(0, weight=2)
app.frameLog.grid_rowconfigure(1, weight=3)
app.frameLog.log = tk.Label(app.frameLog, text='Log', font=(info['police'], info['taillePolice']), bg='white')
app.frameLog.log.grid(row=0, column=0)
app.frameLog.logtTXT = tkinter.scrolledtext.ScrolledText(app.frameLog, font=(info['police'], 10), bg='white')
app.frameLog.logtTXT.grid(row=1, column=0, sticky="nesw")

app.frame = tk.Frame(app, height=50, borderwidth=1, relief="ridge")
app.frame.grid(row=0, column=0, sticky="nesw")
transfer(0)
app.mainloop()
		
sys.exit(0)