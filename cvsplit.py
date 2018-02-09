import cv2
import numpy as np
#读取图片
img = cv2.imread("D:\\python\\test.jpg")
#切割份数
m = 2
n = 2
#图片大小
sp = img.shape
height = sp[0]
width = sp[1]
print ('图片的高为 %s'%height)
print ('图片的宽为 %s'%width)
#切割后大小
split_h1= height/m
split_w1 = width/n
split_h = int(split_h1)
split_w = int(split_w1)
print ('切割后图片的宽为 %s'%split_w)
print ('切割后每张图片的高为 %s'%split_h)
#切割操作
image_save_path_head  = "D:\\python\\split\\P_"
image_save_path_tail  = ".jpg"  
for i in range(m):
 for j in range(n):
  a = j * split_w
  b = i * split_h
  print ('%d,%d,%d,%d'%(a,b,split_w,split_h))
  img_roi = img[a:a+split_w,b:b+split_h]
  cv2.namedWindow("[ROI_Img]",cv2.WINDOW_AUTOSIZE)  
  cv2.imshow("[ROI_Img]",img_roi)  
  cv2.waitKey(500)  
  cv2.destroyWindow("[ROI_Img]")
  image_save_path = "%s%d_%d%s"%(image_save_path_head,i,j,image_save_path_tail)
  cv2.imwrite(image_save_path,img_roi)  
