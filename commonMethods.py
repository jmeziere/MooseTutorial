from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.stacklayout import StackLayout
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle, Line
from collections import deque
from PIL import ImageFont, ImageDraw
import os
from os.path import expanduser
import _thread

moose_file = open(os.path.join(os.path.dirname(__file__),'moosepath.txt'))
string = str(moose_file.read())
if(string[-1] == '\n'):
    string = string[:-1]
moosepath = expanduser(string)
print(moosepath)

def writeToFile(path, text):
    file = open(path,"w+")
    file.write(text)
    file.close()

def saveFile(instance, text):
    _thread.start_new_thread(writeToFile,(instance.filename,text))

def printFile(text):
    print(text)

def niceLayout(width,filename,path = ''):
    file = open(os.path.join(path,filename+'.txt'))
    lines = file.readlines()
    labels = []
    index = 0
    new_label = Label(text = lines[0][:-1])
    new_label.font_size = 40
    new_label.size_hint_y = None
    new_label.text_size = [width,None]
    new_label.halign = 'center'
    new_label.texture_update()
    labels.append(new_label)
    height = new_label.height
    i = 1
    while i < len(lines):
        if(lines[i][-1] == '\n'):
            lines[i] = lines[i][:-1]
        if len(lines[i]) > 0 and lines[i][0] == '$' and lines[i][-1] == '$':
            new_label = Image(source=os.path.join(path,filename+str(index)+'.png'))
            new_label.size_hint_y = None
            new_label.height = 25
            new_label.halign = 'left'
            height += new_label.height
            index += 1
            i += 1
        elif lines[i] == 'Table':
            i += 1
            new_label = StackLayout()
            new_label.orientation = 'lr-tb'
            new_label.size_hint = None, None
            new_label.width = width
            lines[i] = lines[i][:-1]
            label_height = 0
            while lines[i] != 'End':
                splits = lines[i].split('|')
                label_elements = []
                for j in range(len(splits)):
                    table_element = Label(text = splits[j])
                    table_element.size_hint = None, None
                    table_element.width = width/len(splits)
                    table_element.text_size = [width/len(splits),None]
                    table_element.halign = 'center'
                    table_element.valign = 'center'
                    table_element.texture_update()
                    label_elements.append(table_element)
                max_height = 0
                for table_element in label_elements:
                    max_height = max(max_height, table_element.texture_size[1])
                for table_element in label_elements:
                    if max_height == 0:
                        table_element.height = 15
                    else:
                        table_element.height = max_height
                    new_label.add_widget(table_element)
                if max_height == 0:
                    label_height += 15
                else:
                    label_height += max_height
                i += 1
                lines[i] = lines[i][:-1]
            new_label.height = label_height
            height += new_label.height
            i += 1
        elif lines[i][:4] == "File":
            new_line = lines[i].split(',')
            new_label = Label(text = new_line[1])
            new_label.font_size = 20
            new_label.size_hint_y = None
            new_label.text_size = [width,None]
            new_label.texture_update()
            labels.append(new_label)
            height += new_label.height
            try:
                sub_file = open(os.path.join(moosepath,new_line[2]))
                whole_text = sub_file.read()
            except:
                whole_text = "File not found.\nEither MOOSE is not installed or the path is incorrect!"
            new_label = Label(text = whole_text)
            new_label.size_hint_y = None
            new_label.text_size = [width,None]
            new_label.texture_update()
            new_label.height = new_label.texture_size[1]
            height += new_label.height
            i += 1
        elif lines[i][:9] == "InputFile":
            new_line = lines[i].split(',')
            new_label = Label(text = new_line[1])
            new_label.font_size = 20
            new_label.size_hint_y = None
            new_label.text_size = [width,None]
            new_label.texture_update()
            labels.append(new_label)
            height += new_label.height
            try:
                sub_file = open(os.path.join(moosepath,new_line[2]))
                whole_text = sub_file.read()
            except:
                whole_text = ""
            new_label = TextInput(text = whole_text)
            new_label.size_hint_y = None
            new_label.text_size = [width,None]
            new_label.height = 500
            new_label.filename = os.path.join(moosepath,new_line[2])
            new_label.bind(text = saveFile)
            height += new_label.height
            i += 1
        else:
            new_label = Label(text = lines[i])
            new_label.size_hint_y = None
            new_label.text_size = [width,None]
            new_label.texture_update()
            if new_label.texture_size[1] == 0:
                new_label.height = 15
            else:
                new_label.height = new_label.texture_size[1]
            height += new_label.height
            i += 1
        labels.append(new_label)
    return (labels,height)

def runSimulation(filename):
    sim_path = os.path.join(moosepath,filename)
    os.system('peacock -i '+sim_path)
