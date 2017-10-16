import os
import os.path

FILE_PATH_1 = "tmp1/"
FILE_PATH_2 = "tmp2/tmp3/tmp4/"
FILE_NAME_FULL_PATH_1 = "resources/sample1.txt"

with open(FILE_PATH_2 + "dymmyfile1.txt", "w") as f:
    f.write("this is dummy")

# os.walkは３種類のイテレータを返す。
for root, dirs, files, in os.walk("tmp2"):
    print(root, dirs, files)
#=>
# tmp2 ['tmp3'] []
# tmp2\tmp3 ['tmp4'] []
# tmp2\tmp3\tmp4 [] ['dymmyfile1.txt']


for root, dirs, files, in os.walk("tmp2"):
    for d in dirs:
        print("dir:" + root + "/" + d)
        #=> dir:tmp2/tmp3
        #   dir:tmp2\tmp3/tmp4
    for f in files:
        print("file:" + root + "/" + ｆ)
        #=> file:tmp2\tmp3\tmp4/dymmyfile1.txt



print(os.getcwd()) # カレントディレクトリ出力（例：f:\Python\PracticePython）

print(os.path.join("a","b","c")) #=> a\b\c
print(os.path.split("a/b/c"))    #=> ('a/b', 'c')　　※渡された引数を、環境に合わせたパス区切り文字で結合。
print(os.path.split("a/b/c/"))   #=> ('a/b/c', '')

print(os.path.dirname(FILE_NAME_FULL_PATH_1))  #=> resources（親ディレクトリ名）
print(os.path.basename(FILE_NAME_FULL_PATH_1)) #=> sample1.txt（ファイル名）



