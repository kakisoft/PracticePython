"""
コマンドライン引数
実行時引数

python command_line_arg.py a b c
 #=> 第1引数：a  第2引数：b  第3引数：c
"""
import sys

args = sys.argv

print(args)
print("第1引数：" + args[1])
print("第2引数：" + args[2])
print("第3引数：" + args[3])