import tesserocr
import os
from PIL import Image


os.chdir('d:/pythonStudy/Study/python3网络爬虫/验证码识别/')
print(os.getcwd())
image = Image.open('CheckCode.png')
image = image.convert('L')
threshold = 127
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table, '1')
