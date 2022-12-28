import glob
import os
import re
import sys
import time

import cv2
import numpy as np

"""
ハッシュmd5名でリネームする
"""
args = sys.argv


starts = int(args[3])
step = int(args[2])
flname = args[1]


def my_imread(filename):
    try:
        n = np.fromfile(filename, np.uint8)
        img = cv2.imdecode(n, cv2.IMREAD_COLOR)
        return img
    except Exception as e:
        print(e)
        return None


def main(starts, step, flname):
    os.chdir(flname)
    aldf = glob.glob("*.*")
    hash_func = cv2.img_hash.PHash_create()
    time.sleep(1)
    for i, sep in enumerate(aldf):
        if re.search(r".*\.j?pe?n?g$", str(sep), re.I):
            # print(i,sep)
            if (i - starts) % step == 0:
                sample_image01 = my_imread(sep)
                tem = hash_func.compute(sample_image01)[0]
                a = "".join([hex(i)[2:] for i in tem])
                _, ext = os.path.splitext(sep)
                if os.path.exists(a + ext):
                    os.remove(sep)
                else:
                    os.rename(sep, a + ext)

                # ###-------------------------------------####

    os.chdir("..")


# start_time = time.perf_counter()
try:
    main(starts, step, flname)
except Exception as e:
    with open(f"{starts}_error.txt", "w") as f:
        f.write(str(e))
# end_time = time.perf_counter()

# 経過時間を出力(秒)
# elapsed_time = end_time - start_time
# print(elapsed_time,"秒")