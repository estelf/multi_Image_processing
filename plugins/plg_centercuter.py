import glob
import os
import re
import sys

from PIL import Image
import time

args = sys.argv

"""
画像が正方形になるように両側もしくは上下から切り取る
"""
starts = int(args[3])
step = int(args[2])
flname = args[1]


def crop_center(img, crop_width, crop_height):
    img_width, img_height = img.size
    return img.crop(
        (
            (img_width - crop_width) // 2,
            (img_height - crop_height) // 2,
            (img_width + crop_width) // 2,
            (img_height + crop_height) // 2,
        )
    )


def filereader():
    with open("master.csv", "r", encoding="utf-8") as f:
        a = [i.strip() for i in f.readlines()]
    return a


def main(starts, step, flname):
    aldf = filereader()
    os.chdir(flname)
    time.sleep(1)
    for i, sep in enumerate(aldf):
        if re.search(r".*\.j?pe?n?g$", str(sep), re.I):
            # print(i,sep)
            if (i - starts) % step == 0:
                # print(i,starts,step)
                img = Image.open(sep)

                # ###-------------------------------------####
                img_crop_square = crop_center(img, min(img.size), min(img.size))
                img_crop_square.save(sep)
                # ###-------------------------------------####

    os.chdir("..")


# start_time = time.perf_counter()
try:
    main(starts, step, flname)
except Exception as e:
    with open(f"{starts}_error.txt", "w") as f:
        f.write(str(e))
    exit(1)
# end_time = time.perf_counter()

# 経過時間を出力(秒)
# elapsed_time = end_time - start_time
# print(elapsed_time,"秒")
