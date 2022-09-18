import cv2
import numpy as np
import glob
import os
import sys
import time
import re
args=sys.argv


starts=int(args[3])
step=int(args[2])
flname=args[1]
def my_imread(filename):
    try:
        n = np.fromfile(filename, np.uint8)
        img = cv2.imdecode(n, cv2.IMREAD_COLOR)
        return img
    except Exception as e:
        print(e)
        return None
def my_imwrite(filename, img):
    try:
        ext = os.path.splitext(filename)[1]
        result, n = cv2.imencode(ext, img)
        if result:
            with open(filename, mode='w+b') as f:
                n.tofile(f)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False
def main(starts,step,flname):
    os.chdir(flname)
    for i,sep in enumerate(glob.glob("*.png")):
        if re.search(r".*\.j?pe?n?g$", str(i), re.I):
            #print(i,sep)
            if (i-starts)%step==0:
                #print(i,starts,step)
                img=my_imread(sep)

                ####-------------------------------------####
                img = cv2.Laplacian(img, cv2.CV_32F, ksize=5)
                my_imwrite(sep,img)
                ####-------------------------------------####


    os.chdir("..")
#start_time = time.perf_counter()
main(starts,step,flname)
#end_time = time.perf_counter()
 
# 経過時間を出力(秒)
#elapsed_time = end_time - start_time
#print(elapsed_time,"秒")