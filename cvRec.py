import cv2
import numpy as np
import math
#读取图片
img1 = cv2.imread("D:\\python\\test0.jpg")
img2 = cv2.imread("D:\\python\\test1.jpg")
#切割份数
g = 2
h = 2
#图片大小
sp1 = img1.shape
sp2 = img2.shape
height1 = sp1[0]
width1 = sp1[1]
height2 = sp2[0]
width2 = sp2[1]
print ('图片1的高为 %s'%height1)
print ('图片1的宽为 %s'%width1)
print ('图片2的高为 %s'%height2)
print ('图片2的宽为 %s'%width2)
#切割后大小
split_h11= height1/g
split_w11 = width1/h
split_h12= height2/g
split_w12 = width2/h
split_h1 = int(split_h11)
split_w1 = int(split_w11)
split_h2 = int(split_h12)
split_w2 = int(split_w12)
print ('切割后每张图片1的宽为 %s'%split_w1)
print ('切割后每张图片1的高为 %s'%split_h1)
print ('切割后每张图片2的宽为 %s'%split_w2)
print ('切割后每张图片2的高为 %s'%split_h2)
#切割操作
image_save_path_head1  = "D:\\python\\split\\P1_"
image_save_path_head2  = "D:\\python\\split\\P2_"
image_save_path_tail  = ".jpg"  
for m in range(g):
    for n in range(h):
	    a1 = n * split_w1
	    b1 = m * split_h1
	    a2 = n * split_w2
	    b2 = m * split_h2
	    print ('%d,%d,%d,%d'%(a1,b1,split_w1,split_h1))
	    print ('%d,%d,%d,%d'%(a2,b2,split_w2,split_h2))
	    img_roi1 = img1[a1:a1+split_w1,b1:b1+split_h1]
	    img_roi2 = img2[a2:a2+split_w2,b2:b2+split_h2]
	    cv2.namedWindow("[ROI_Img]",cv2.WINDOW_AUTOSIZE)  
	    cv2.imshow("[ROI_Img]",img_roi1)  
	    cv2.waitKey(500)  
	    cv2.destroyWindow("[ROI_Img]")
	    cv2.namedWindow("[ROI_Img]",cv2.WINDOW_AUTOSIZE)  
	    cv2.imshow("[ROI_Img]",img_roi2)  
	    cv2.waitKey(500)  
	    cv2.destroyWindow("[ROI_Img]")
	    image_save_path = "%s%d_%d%s"%(image_save_path_head1,m,n,image_save_path_tail)
	    cv2.imwrite(image_save_path,img_roi1)
	    image_save_path = "%s%d_%d%s"%(image_save_path_head2,m,n,image_save_path_tail)
	    cv2.imwrite(image_save_path,img_roi2)
#差值感知算法
def dHash(img):
    #缩放8*8
    img=cv2.resize(img,(9,8),interpolation=cv2.INTER_CUBIC)
    #转换灰度图
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    hash_str=''
    #每行前一个像素大于后一个像素为1，相反为0，生成哈希
    for i in range(8):
        for j in range(8):
            if   gray[i,j]>gray[i,j+1]:
                hash_str=hash_str+'1'
            else:
                hash_str=hash_str+'0'
    return hash_str
#Hash值对比
def cmpHash(hash1,hash2):
    n=0
    #hash长度不同则返回-1代表传参出错
    if len(hash1)!=len(hash2):
        return -1
    #遍历判断
    for i in range(len(hash1)):
        #不相等则n计数+1，n最终为相似度
        if hash1[i]!=hash2[i]:
            n=n+1
    return n	
#读取每一块图片，比较每一块的相似度，并存入数组
j = 0
D = []
for m1 in range(g):
	for n1 in range(h):
		img_cut1 = cv2.imread("%s%d_%d%s"%(image_save_path_head1,m1,n1,image_save_path_tail))
		img_cut2 = cv2.imread("%s%d_%d%s"%(image_save_path_head2,m1,n1,image_save_path_tail))
		hash1= dHash(img_cut1)
		hash2= dHash(img_cut2)
		D.append(cmpHash(hash1,hash2))
		print('坐标为%d,%d的差值哈希算法相似度：%d'%(m1+1,n1+1,D[j]))
		j = j+1
print ('坐标为%d,%d的方块是角标'%(math.ceil((D.index(min(D))+1)/h),(D.index(min(D))+1)%h))