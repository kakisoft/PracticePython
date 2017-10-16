import os

FILE_PATH_1 = "tmp1/"
FILE_PATH_2 = "tmp2/tmp3/tmp4/"

os.mkdir(FILE_PATH_1)
#os.mkdir(FILE_PATH_2)  #=> error （サブフォルダを含めて作成できない。）

os.makedirs(FILE_PATH_2) # サブフォルダも合わせて作成。何で 「mkdirs」じゃないんだよ。。。

