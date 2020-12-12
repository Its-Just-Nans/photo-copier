import sys
import socket
import time
import os
import tkinter as tk
import string
import tkinter.filedialog
import tkinter.scrolledtext
from PIL import ImageTk, Image

global app # tkinter
import shutil
import datetime
import time

global info
info = {}
info['taillePolice'] = 15
info['police'] = 'Segoe UI'
    
if '-log' in sys.argv:
    info['log'] = True
else:
    info['log'] = False


global allPhotos
allPhotos = []

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
        try:
            app.frame.text = tk.Label(app.frame, text='Choisir le dossier de destination', font=(info['police'], info['taillePolice']),)
            app.frame.text.grid(row=0, column=0, columnspan=3, sticky="nesw")
            app.frame.buttonAuto = tk.Button(app.frame, text="Choix auto par le logiciel", font=(info['police'], info['taillePolice']), fg="blue", command=lambda:choixDest())
            app.frame.buttonAuto.grid(row=1, column=0)
            app.frame.buttonManu = tk.Button(app.frame, text="Choix Manuel", font=(info['police'], info['taillePolice']), fg="blue", command=lambda:choixFenetre('fileDest', 2))
            app.frame.buttonManu.grid(row=1, column=2)
            app.frame.buttonBefore = tk.Button(app.frame, text="Précédent", font=(info['police'], info['taillePolice']), fg="red", command=lambda:transfer(0))
            app.frame.buttonBefore.grid(row=2, column=0, columnspan="3")
        except KeyError:
            transfer(0)
    elif step == 2:
        try:
            if info['fileDest'] != '':
                app.frame.text = tk.Label(app.frame, text='Choisir le dossier où sont les photos', font=(info['police'], info['taillePolice']))
                app.frame.text.grid(row=0, column=0, columnspan=3, sticky="nesw")
                app.frame.buttonAuto = tk.Button(app.frame, text="Choix auto par le logiciel", font=(info['police'], info['taillePolice']), fg="blue", command=lambda:choixSrc())
                app.frame.buttonAuto.grid(row=1 ,column=0)
                app.frame.buttonManu = tk.Button(app.frame, text="Choix Manuel", font=(info['police'], info['taillePolice']), fg="blue", command=lambda:choixFenetre('fileSrc', 3))
                app.frame.buttonManu.grid(row=1, column=2)
                app.frame.buttonBefore = tk.Button(app.frame, text="Précédent", font=(info['police'], info['taillePolice']), fg="red", command=lambda:transfer(1))
                app.frame.buttonBefore.grid(row=2, column=0, columnspan="3")
        except KeyError:
            transfer(1)
    elif step == 3:
        try:
            if info['fileSrc'] != '':
                #Ecrire ce qu'il va faire
                app.frame.text = tk.Label(app.frame, text='Copier', font=(info['police'], info['taillePolice']))
                app.frame.text.grid(row=0, column=0, columnspan=3, sticky="nesw")
                app.frame.buttonAuto = tk.Button(app.frame, text="Copier les fichiers", font=(info['police'], info['taillePolice']), fg="blue", command=lambda:copy())
                app.frame.buttonAuto.grid(row=1 ,column=0, columnspan=3)
                app.frame.buttonBefore = tk.Button(app.frame, text="Précédent", font=(info['police'], info['taillePolice']), fg="red", command=lambda:transfer(2))
                app.frame.buttonBefore.grid(row=2, column=0, columnspan="3")
            else :
                transfer(2)
        except KeyError:
            transfer(2)
    elif step == 5:
        app.frame.text = tk.Label(app.frame, text='OK', font=(info['police'], info['taillePolice']))
        app.frame.text.grid(row=0, column=0, columnspan=3, sticky="nesw")
        app.frame.buttonNext = tk.Button(app.frame, text="Recommencer", font=(info['police'], info['taillePolice']), fg="blue", command=lambda:transfer(0))
        app.frame.buttonNext.grid(row=2, column=0, columnspan="3")

def choixFenetre(attribut, nextStep):
    global info
    x = 0
    if attribut == 'fileSrc':
        x=0
        app.filename = tkinter.filedialog.askdirectory(title='Choose file')
    else:
        x=2
        app.filename = tkinter.filedialog.askdirectory(initialdir='C:\\', title='Choose file')
    if app.filename != '':
        app.filename = app.filename.replace("/", "\\")
        info[attribut] = app.filename + '\\'
        addToLog('Dossier choisi : "' + info[attribut] + '"', True, True)
        app.schema.label = tk.Label(app.schema, text=info[attribut], font=(info['police'], info['taillePolice']), bg='white')
        app.schema.label.grid(row=2, column=x, sticky="nesw")
        transfer(nextStep)
    else:
        pass

def addToLog(text, sautLigne, render):
    if info['log']:
        print(text)
    if sautLigne:
        text = text + '\n'
    if render:
        time.sleep(0.05)
    app.frameLog.logtTXT.configure(state='normal')
    app.frameLog.logtTXT.insert(tkinter.END, text)
    app.update_idletasks()
    app.frameLog.logtTXT.configure(state='disabled')
    app.frameLog.logtTXT.see(tk.END)


def choixDest():
    username = os.getlogin()
    pathToScript = os.path.realpath(__file__).split('\\')

    info['fileDest'] = pathToScript[0]+'\\'
    if os.path.exists(info['fileDest'] + 'Users\\'):
        info['fileDest'] = info['fileDest'] + 'Users\\'
        if os.path.exists(info['fileDest'] + username + '\\'):
            info['fileDest'] = info['fileDest'] + username + '\\'
            if os.path.exists(info['fileDest'] + 'Pictures' + '\\'):
                info['fileDest'] = info['fileDest'] + 'Pictures' + '\\'

    else:
        print("error ?")
    addToLog('Dossier choisi : "' + info['fileDest'] + '"', True, True)
    app.schema.label = tk.Label(app.schema, text=info['fileDest'], font=(info['police'], info['taillePolice']), bg='white')
    app.schema.label.grid(row=2, column=2, sticky="nesw")
    transfer(2)

def choixSrc():
    allLetter = string.ascii_uppercase
    allLetter = allLetter.replace('C', '')
    drives = []
    for l in allLetter:
        if os.path.exists(l+':\\'):
            drives.append(l)
            print('Il y a un appareil connecté avec ' + l + ':\\')
    allLetter = len(drives)
    if allLetter == 0:
        addToLog('Pas d\'appareil trouvé', True, True)
    elif allLetter == 1:
        findPhotos(drives[0]+':\\')
        if len(allPhotos) > 0:
            addToLog('Photos trouvés dans "'+ drives[0]+':\\"', True, True)
            info['fileSrc'] = drives[0]+':\\'
            addToLog('Dossier choisi dans "' + info['fileSrc'] + '"', True, True)
            app.schema.label = tk.Label(app.schema, text=info['fileSrc'], font=(info['police'], info['taillePolice']), bg='white')
            app.schema.label.grid(row=2, column=0, sticky="nesw")
            transfer(3)
        else:
            addToLog('Pas de photos dans "'+ drives[0]+':\\"', True, True)
    else :
        addToLog('Il y a plusieurs appareils connectés, veuillez choisir le bon appareil', True, True)
        time.sleep(2)
        choixFenetre('fileSrc', 3)


def chooseNameOfFile():
    global nom
    try:
        try:
            app.frame.text.destroy()
            app.frame.buttonAuto.destroy()
            app.frame.buttonBefore.destroy()
            app.frame.buttonNext.destroy()
        except Exception as e:
            pass
        app.frame.text = tk.Label(app.frame, text='Choisir le nom du dossier de destination correspondant à la visualisation', font=(info['police'], info['taillePolice']))
        app.frame.text.grid(row=0, column=0, columnspan=3, sticky="nesw")
        app.frame.fichierAppareil = tk.Entry(app.frame, width=20, font=(info['police'], info['taillePolice']))
        app.frame.fichierAppareil.grid(row=1 ,column=0, columnspan=3)
        app.frame.buttonNext = tk.Button(app.frame, text="Choisir", font=(info['police'], info['taillePolice']), fg="green", command=lambda:next())
        app.frame.buttonNext.grid(row=2, column=0, columnspan=3)
        app.frame.mainloop()
        return nom
    except KeyError:
        transfer(2)

def next():
    global nom
    app.frame.quit()
    nom = app.frame.fichierAppareil.get()
    if nom != '':
        app.frame.text.destroy()
        app.frame.fichierAppareil.destroy()
        app.frame.buttonNext.destroy()
        



def findPhotos(path):
    elements = os.listdir(path)
    for oneElement in elements:
        newPath = path+oneElement
        if os.path.isdir(newPath):
            photos = findPhotos(newPath + '\\')
            if photos:
                allPhotos.append(newPath + '\\')
        else:
            if checkIfImg(newPath):
                #print(newPath)
                return True


def checkIfImg(path):
    extension = os.path.splitext(path)[1]
    extension = extension.lower()
    extensionPhotos = ['.png', '.raw', '.jpg', '.gif', '.svg']
    for oneExtension in extensionPhotos:
        if oneExtension == extension:
            return True

def setNameOfDir(fileToTransfer, nameToCreate):
    global info
    date = getDate(os.path.getmtime(fileToTransfer))
    newNamePath = info['fileDest'] + date + '_' + nameToCreate + '\\'
    try:
        if not os.path.exists(newNamePath):
            os.mkdir(newNamePath)
            addToLog("Le dossier '" + newNamePath + "' a été crée ", True, True)
            if os.path.exists(newNamePath):
                return newNamePath
            else:
                return ' '
        else:
            addToLog("Le dossier '" + newNamePath + "' éxiste  deja", True, True)
            return ' '
    except FileExistsError:
        addToLog("Le dossier '" + newNamePath + "' éxiste  deja", True, True)
        return ' '
    except OSError:
        addToLog("Le nom du dossier '" + newNamePath + "' a posé problème", True, True)
        return ' '

def listPictOfFile(path):
    elements = os.listdir(path)
    tab = []
    for oneElement in elements:
        newPath = path + oneElement
        if not os.path.isdir(newPath):
            if checkIfImg(newPath):
                tab.append(newPath)
    return tab

def viewerController(nextPict):
    global info
    index = info['listPict'].index(info['pictName'])
    total = len(info['listPict'])
    linkToImage = ''
    if nextPict and ( 0 <= (index+1) < total):
        linkToImage = info['listPict'][index+1]
    elif not nextPict and ( 0 <= (index-1) < total):
        linkToImage = info['listPict'][index-1]
    if linkToImage != '':
        try:
            img = Image.open(linkToImage)
            zoom = 0.15
            pixels_x, pixels_y = tuple([int(zoom * x)  for x in img.size])
            img = img.resize((pixels_x, pixels_y), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            app.preview.img.destroy()
            app.preview.img = tk.Label(app.preview , image=img)
            app.preview.img.photo = img
            app.preview.img.grid(row=1, column=0, columnspan="2")
            info['pictName'] = linkToImage
            app.update_idletasks()
        except Exception as e:
            print(e)

def copy():
    global allPhotos
    allPhotos = []
    if findPhotos(info['fileSrc']):
        allPhotos.append(info['fileSrc'])
    for filePhoto in allPhotos:
        #get the name of the file
        try:
            info['listPict'] = listPictOfFile(filePhoto)
            info['pictName'] = info['listPict'][0]
            img = Image.open(info['pictName'])
            zoom = 0.15
            pixels_x, pixels_y = tuple([int(zoom * x)  for x in img.size])
            img = img.resize((pixels_x, pixels_y), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            app.preview.img = tk.Label(app.preview , image=img)
            app.preview.img.photo = img
            app.preview.img.grid(row=1, column=0, columnspan="2")
            app.preview.buttonNext1 = tk.Button(app.preview, text="Photo précédente", font=(info['police'], info['taillePolice']), fg="green", command=lambda:viewerController(False))
            app.preview.buttonNext1.grid(row=2, column=0)
            app.preview.buttonNext2 = tk.Button(app.preview, text="Photo suivante", font=(info['police'], info['taillePolice']), fg="green", command=lambda:viewerController(True))
            app.preview.buttonNext2.grid(row=2, column=1)
        except Exception as e:
            print(e.__class__.__name__)
        newNameOfFile = chooseNameOfFile()
        app.preview.img.destroy()
        app.preview.buttonNext1.destroy()
        app.preview.buttonNext2.destroy()
        error = False
        if ' ' in newNameOfFile:
            newNameOfFile = newNameOfFile.replace(' ', '_')
        if '/' in newNameOfFile:
            newNameOfFile = newNameOfFile.replace('/', '_')
        if '\\' in newNameOfFile:
            newNameOfFile = newNameOfFile.replace('\\', '_')
        longueur = len(newNameOfFile)
        if longueur > 120:
            error = True
        destination = setNameOfDir(filePhoto, newNameOfFile)
        while destination == ' ' or error:
            newNameOfFile = chooseNameOfFile()
            destination = setNameOfDir(filePhoto, newNameOfFile)
        newLinkToSrc = filePhoto
        dateOfFile = getDate(os.path.getmtime(newLinkToSrc))
        count = 0
        listOfFile = os.listdir(filePhoto)
        for element in listOfFile:
            extensionOfFile = element[-3]
            if element[-3] == '.':
                extensionOfFile = element[-3:]
            elif element[-4] == '.':
                extensionOfFile = element[-4:]
            elif element[-5] == '.':
                extensionOfFile = element[-5:]
            count = count + 1
            newLinkToSrc = filePhoto + element
            dateOfFile = getDate(os.path.getmtime(newLinkToSrc))
            newLinkToDest = destination + dateOfFile + "_" + newNameOfFile + "_{:00004d}".format(count) + extensionOfFile.lower()
            #print('We are going to copy '+newLinkToSrc+' > '+newLinkToDest)
            try:
                addToLog("[Copy] '"+ newLinkToSrc + "' -> '" + newLinkToDest + "'", False, False)
                if not os.path.exists(newLinkToDest):
                    shutil.copy2(newLinkToSrc, newLinkToDest)
                    addToLog(" [OK]", True, False)
                else :
                    addToLog("\n[KO]", True, False)
                    addToLog("[Error] '" + newLinkToDest + "' existe déjà", True, False)
            except Exception as e:
                addToLog("\n[KO]", False, False)
                addToLog(e.__class__.__name__, True, False)
            addToLog('', False, True)
    transfer(5)

def destroyTkinter():
    app.quit()
    app.destroy()
    sys.exit(1)


def getDate(timestamp):
    date = datetime.datetime.fromtimestamp(timestamp)
    return date.strftime("%Y-%m-%d")


app = tk.Tk()
app.attributes("-fullscreen", True)
app.title('PhotoCopy')
app.geometry('900x600')
app.configure(bg='white')
app.grid_columnconfigure(0, weight=1, minsize="200")
app.grid_columnconfigure(1, weight=1, minsize="400")
app.grid_rowconfigure(0, weight=3, minsize="400")
app.grid_rowconfigure(1, weight=4, minsize="100")
app.grid_rowconfigure(2, weight=1, minsize="32")
app.quitter = tk.Button(app, text="Quitter", fg="red", command=lambda :destroyTkinter())
app.quitter.grid(row=2, column=0, columnspan=2)

app.preview = tk.Frame(app, bg='red', width=200, borderwidth = 1, relief="ridge")
app.preview.grid(row=1, column=0, sticky="nesw")
app.preview.grid_rowconfigure(0, weight=2)
app.preview.grid_rowconfigure(1, weight=4)
app.preview.grid_rowconfigure(2, weight=1)
app.preview.grid_columnconfigure(0, weight=1)
app.preview.grid_columnconfigure(1, weight=1)
app.preview.label = tk.Label(app.preview, text='Visualisation', font=(info['police'], info['taillePolice']), bg='white')
app.preview.label.grid(row=0, column=0, sticky="nesw", columnspan="2")

app.schema = tk.Frame(app, bg='white', width=200, borderwidth = 1, relief="ridge")
app.schema.grid(row=1, column=1, sticky="nesw")
app.schema.grid_rowconfigure(0, weight=1)
app.schema.grid_rowconfigure(1, weight=1)
app.preview.grid_rowconfigure(2, weight=1)
app.schema.grid_columnconfigure(0, weight=1)
app.schema.grid_columnconfigure(1, weight=1)
app.schema.grid_columnconfigure(2, weight=1)
app.schema.label = tk.Label(app.schema, text='Schéma', font=(info['police'], info['taillePolice']), bg='white')
app.schema.label.grid(row=0, column=0, sticky="nesw", columnspan="3")

img = Image.open('.\\folder-ico.jpg')
zoom = 0.60
pixels_x, pixels_y = tuple([int(zoom * x)  for x in img.size])
img = img.resize((pixels_x, pixels_y), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
app.schema.img1 = tk.Label(app.schema , image=img)
app.schema.img1.photo = img
app.schema.img1.grid(row=1, column=0)

img = Image.open('.\\arrow.jpg')
zoom = 0.5
pixels_x, pixels_y = tuple([int(zoom * x)  for x in img.size])
img = img.resize((pixels_x, pixels_y), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
app.schema.img2 = tk.Label(app.schema , image=img)
app.schema.img2.photo = img
app.schema.img2.grid(row=1, column=1)

img = Image.open('.\\folder-ico.jpg')
zoom = 0.60
pixels_x, pixels_y = tuple([int(zoom * x)  for x in img.size])
img = img.resize((pixels_x, pixels_y), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
app.schema.img3 = tk.Label(app.schema , image=img)
app.schema.img3.photo = img
app.schema.img3.grid(row=1, column=2)

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
app.frame.grid(row=0, column=0, rowspan="2", sticky="nesw")
transfer(0)
app.mainloop()
        
sys.exit(0)