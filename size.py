import cv2
import numpy as np

for i in range(34):
	image_read_path_head  = "D:\\python\\roi\\"
	image_read_path_tail  = ".jpg"
	image_read_path = "%s%d%s"%(image_read_path_head,i+1,image_read_path_tail)
	image_save_path_head  = "D:\\python\\pos\\"
	image_save_path_tail  = ".jpg"
	image_save_path = "%s%d%s"%(image_save_path_head,i+1,image_save_path_tail)  	
	img=cv2.imread(image_read_path)
	img1=cv2.resize(img,(60,28),interpolation=cv2.INTER_CUBIC)
	cv2.imwrite(image_save_path,img1)