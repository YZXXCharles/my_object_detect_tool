import cv2
import numpy as np

cap = cv2.VideoCapture('D:\\python\\roi\\test.mp4') #读入视频文件
c = 1  
time = 500

while(1):
	ret, frame = cap.read()
	if(c%time == 0):
		img_roi = frame[300:400,500:700]
		cv2.imwrite('D:\\python\\roi\\'+str(int(c/500)) + '.jpg',img_roi) #存储为图像  
	c = c+1
	if cv2.waitKey(100) & 0xFF == ord('q'):
		break

cap.release()
