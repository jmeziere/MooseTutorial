from sympy import preview
from cv2 import imread, bitwise_not, imwrite
preview('$$\int_0^1 e^x\,dx$$', viewer='file', filename='test.png', euler=False)

image = imread('test.png')
invert = bitwise_not(image)
imwrite('test.png',invert)
