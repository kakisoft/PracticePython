import sys

for i, arg in enumerate(sys.argv):
    print("{}:{}".format(i, arg))


# python command_line.py value1 value2 value3
# ⇒
# 0:command_line.py
# 1:value1
# 2:value2
# 3:value3

sum = 0
for i in range(1, len(sys.argv)):
    sum += float(sys.argv[i])

print("total:{}".format(sum))

# python command_line.py 1 2 3
# ⇒ total:6.0