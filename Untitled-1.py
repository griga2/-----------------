
from itertools import count
from re import S
from tkinter import BROWSE
import PySimpleGUI as sg
from PIL import Image,ImageFilter

class StartForm():
    def UploadDataBase():
        print("Uploat DateBase is started")

class ImageManager():
    
    def GetFileCount():
        count = 0
        return count

    def ImageManager():
        print('Filemagager worked')

    def OpenFile(path):
        img = Image.open(path)
        print('File open ',path)
        img.save(GetFileCount(BaseName))
        
class BaseManager():
    def OpenBase():
        if os.path.exists(BaseName):
            print("Base is find")
        else :
            print("Base is create")
            os.mkdir(BaseName)
            counter = open(BaseName+'/Counter.txt', "w+")
            counter.write('0')




StartMenuForm = [
    [
        sg.Frame( 'Create and upload imagebase',[
            [sg.Text('New imagebase ?'),
            sg.Checkbox('', key = '-СANCREATE-'), 
            ],

            [sg.Text('New base name'),
            sg.InputText(size=(13,1), 
            key = '-BASENAME-'), 
            ],

            [sg.Text('New imagebase path'),
            sg.InputText(size=(13,1), key='-NEWBASEPATH-'),
            sg.FileBrowse()
            ],

            [sg.Text('Upload base'), 
            sg.Button('Do something',key='-UPLOADBASE-',
            size=(15,1))
            ],

        ],size = (250,150)),
    
        sg.Frame('Image base',[
            [sg.Text('Imagebase path'),
            sg.InputText(size=(13,1), key='-BASEPATH-'),
            ],
            [sg.Text('Open base'), 
            sg.Button('Do something',key='-NULL-',
            size=(15,1))
            ],

        ],size = (250,150)),  

        sg.Frame('Export image',[
            [sg.Text('Image'),
            sg.InputText(size=(13,1), key='-FILEPATH-'),
            sg.FileBrowse(),
            ],
            [sg.Text('Upload image'), 
            sg.Button('Export',key='-UPLOADIMAGE-',
            size=(15,1))
            ],
        ],size = (250,150))
    ],
    
    [sg.Frame('Image base info',[
            [sg.Text('Image quantity:0')
            ],
        ],size = (770,70)
    )],

    [sg.Frame('Graf raspred',[ 

    ], size=(770,400)
    )],
    #[sg.Output()]
]


window = sg.Window('File Compare', StartMenuForm,size=(800, 650))
while True:                             

    event, values = window.read()

    if event in (None, 'Exit', 'Cancel'):
        break

    if event == '-OPENFORMBUTTON-':
        print('MainForm is opened')
        StartForm.OpenMainForm()

    if event == '-UPLOADBASE-':
       if  values['-NEWBASEPATH-'] != ' ':
            if values['-CANCREATE-'] == True:
                StartForm.UploadDataBase()
                BaseName=values['-BASENAME-']

    if event == '-UPLOADIMAGE-':
        if values['-FILEPATH-'] != ' ':
            filepath = values['-FILEPATH-']
            ImageManager.OpenFile(filepath)


BaseName = "NewBase"

import os


# check for base exists

