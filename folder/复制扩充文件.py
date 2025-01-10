# srcfile 需要复制、移动的文件
# dstpath 目的地址

import os
import shutil
from glob import glob


filename = os.listdir("ori_data/")
count = 0

for i in range(30):
    for file in filename:

        houzui = file.split(".")[-1]
        qianzui = file.split(".")[0]
        if houzui == "jpg":
            count = count + 1

            #  print(file)
            print(qianzui)
            shutil.copy("ori_data/"+ str(qianzui) + '.jpg', "kuochong_data/" + str(count) + '.jpg')  # 复制文件
            shutil.copy("ori_data/" + str(qianzui) + '.xml', "kuochong_data/" + str(count) + '.xml')  # 复制文件

#
# shutil.copy(srcfile, dstpath + fname)  # 复制文件
# print("copy %s -> %s" % (srcfile, dstpath + fname))
#

