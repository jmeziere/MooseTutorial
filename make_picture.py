from sympy import preview
import os
from cv2 import imread, bitwise_not, imwrite

os.system('find . -name "*.png" -type f -delete')

def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.txt'): # Get all txt files
                paths.append(os.path.join(path,filename))
    return paths

extra_files = package_files('.') # Walk through the current directory
for file in extra_files:
    read_file = open(file) # Needs the correct filepath
    lines = read_file.readlines()
    i = 1
    index = 0
    while i < len(lines):
        lines[i] = lines[i][:-1]
        if len(lines[i]) > 0 and lines[i][0] == '$' and lines[i][-1] == '$':
            preview(lines[i], viewer='file', filename=file[:-4]+str(index)+'.png', euler=False)
            image = imread(file[:-4]+str(index)+'.png')
            invert = bitwise_not(image)
            imwrite(file[:-4]+str(index)+'.png',invert)
            index += 1
        i += 1
