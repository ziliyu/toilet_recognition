# coding=UTF-8
import cv2
import numpy as np

img = cv2.imread("./test3.jpg")
img=cv2.resize(img,(512,512)) #改变输入图片大小
#img2=img[0:490,0:352]
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #灰度变换
tr,img4=cv2.threshold(gray,80,200,cv2.THRESH_BINARY)
k1=np.ones((3,3),np.uint8)
k2=np.ones((5,5),np.uint8)
k3=np.ones((3,3),np.uint8)
#img5=cv2.morphologyEx(img4,cv2.MORPH_OPEN,k1)
#img5=cv2.morphologyEx(img4,cv2.MORPH_CLOSE,k2)
edge = cv2.Canny(img,70,240) #边缘提取
#edge =cv2.morphologyEx(edge ,cv2.MORPH_OPEN,k1)
#edge=cv2.erode(edge,k3,iterations=3)
image, contours, hier  = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)#检测轮廓
print(len(contours))
#for i in range(len(contours)):
    #img6 = cv2.drawContours(img, contours[i], -1, (0, 0, 255), 5)
    #cv2.imshow("2", img6)
    #cv2.waitKey()

img6 = cv2.drawContours(img, contours[0], -1, (0, 0, 255), 5)
img6 = cv2.drawContours(img, contours[1], -1, (0, 0, 255), 5)
img6 = cv2.drawContours(img, contours[2], -1, (0, 0, 255), 5)
img6 = cv2.drawContours(img, contours[3], -1, (0, 0, 255), 5)
img6 = cv2.drawContours(img, contours[4], -1, (0, 0, 255), 5)
img6 = cv2.drawContours(img, contours[5], -1, (0, 0, 255), 5)
img6 = cv2.drawContours(img, contours[6], -1, (0, 0, 255), 5)
img6 = cv2.drawContours(img, contours[7], -1, (0, 0, 255), 5)
img6 = cv2.drawContours(img, contours[8], -1, (0, 0, 255), 5)
img6 = cv2.drawContours(img, contours[9], -1, (0, 0, 255), 5)
img6 = cv2.drawContours(img, contours[10], -1, (0, 0, 255), 5)
img6 = cv2.drawContours(img, contours[11], -1, (0, 0, 255), 5)
img6 = cv2.drawContours(img, contours[12], -1, (0, 0, 255), 5)
img6 = cv2.drawContours(img, contours[14], -1, (0, 0, 255), 5)
img6 = cv2.drawContours(img, contours[17], -1, (0, 0, 255), 5)
img6 = cv2.drawContours(img, contours[18], -1, (0, 0, 255), 5)
img6 = cv2.drawContours(img, contours[19], -1, (0, 0, 255), 5)
img6 = cv2.drawContours(img, contours[20], -1, (0, 0, 255), 5)
img6 = cv2.drawContours(img, contours[21], -1, (0, 0, 255), 5)
cv2.imshow("1", img6)
#cv2.imshow("2", img6)
cv2.waitKey()


#cv2.imshow("1", edge)
#cv2.imshow("2", img6)

#cv2.waitKey()
#cv2.imshow("1",edge)
#cv2.imshow("2",img6)
#cv2.imshow("3",edge)
#cv2.imshow("2",gray)
#cv2.imshow("2",line_img)
#cv2.waitKey()
