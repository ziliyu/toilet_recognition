
import cv2
import os
import numpy as np



path = 'D:/datajihe/wash/'
dpath = 'D:/datajihe/toilt/'
filelist = os.listdir(path)
print(filelist)
for item in filelist:
    if item.endswith('.jpg'):
        cx=item.split('.')
        dx=cx[0]+'.jpg'
        src = os.path.join(path, item)
        dst = os.path.join(dpath, dx)
        ax = cv2.imread(src)
        bx = cv2.resize(ax, (200, 200))
        cv2.imwrite(dst, bx)









