import cv2
import numpy as np

img = cv2.imread("./test2.jpg")
img=cv2.resize(img,(512,512)) #改变输入图片大小
img2=img[180:260,200:330]
img3 = cv2.GaussianBlur(img2,(3,3),0,0) #高斯模糊
gray = cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY) #灰度变换
tr,img4=cv2.threshold(gray,100,230,cv2.THRESH_BINARY_INV)
edge = cv2.Canny(img4,50,150) #边缘提取
image, contours, hier  = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)#检测轮廓
for i in range(len(contours)):
    if len(contours[i])>20:#过滤掉线型轮廓
        cx=contours[i]
        cutarea = cv2.contourArea(cx) #计算盒子轮廓的像素面积
        print(cutarea)

cv2.imshow("1",img)
cv2.imshow("2",img2)
cv2.imshow("3",edge)
#cv2.imshow("2",gray)
#cv2.imshow("2",line_img)
cv2.waitKey()