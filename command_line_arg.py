"""
コマンドライン引数
実行時引数

python command_line_arg.py a b c
 #=> 実行ファイル名：command_line_arg.py  
 #   第1引数：a  
 #   第2引数：b  
 #   第3引数：c
 #   要素数：4
"""
import sys

args = sys.argv

print(args)
print("実行ファイル名：" + args[0])
print("第1引数：" + args[1])
print("第2引数：" + args[2])
print("第3引数：" + args[3])
print("要素数：" + str(len(args)))
