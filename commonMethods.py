from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle, Line
from collections import deque
from sympy import preview
from cv2 import imread, bitwise_not, imwrite
from PIL import ImageFont, ImageDraw

def niceLayout(width,filename,path = ''):
    file = open(path+filename)
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
    while i < len(lines[1:]):
        lines[i] = lines[i][:-1]
        if len(lines[i]) > 0 and lines[i][0] == '$' and lines[i][-1] == '$':
            preview(lines[i], viewer='file', filename=path+filename+str(index)+'.png', euler=False)
            image = imread(path+filename+str(index)+'.png')
            invert = bitwise_not(image)
            imwrite(path+filename+str(index)+'.png',invert)
            new_label = Image(source=path+filename+str(index)+'.png')
            new_label.size_hint_y = None
            new_label.height = 20
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
                    table_element.height = max_height
                    new_label.add_widget(table_element)
                label_height += max_height
                i += 1
                print(i)
                lines[i] = lines[i][:-1]
            new_label.height = label_height
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
