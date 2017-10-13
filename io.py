import io

#FILE_NAME_FULL_PATH_1 = "resources/sample1.txt"
data = """ab
c
d
e
"""

out1 = io.StringIO(data)
print(out1.read(2))  #=> ab （2文字読出し）

out1.seek(0)
for line in out1:
    print(line)  #=> ab  \n c \n d \n e