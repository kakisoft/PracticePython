import re

# search - 第一引数に指定された正規表現を、第二引数の文字列から検索する。
#          マッチすると、Matchオブジェクトを返す。
#   rを先頭に付けると、"" 内は、エスケープ展開をしない。（raw文字列と言うそうな。）
print(re.search(r"abc","def")) #=> None
print(re.search(r"abc","abc")) #=> <_sre.SRE_Match object; span=(0, 3), match='abc'>

s = "defghijaaaaaaaaaaaaaabc"
m = re.search(r"a+bc", s)
print(m) #=> <_sre.SRE_Match object; span=(7, 23), match='aaaaaaaaaaaaaabc'>

print(m.span) #=> <built-in method span of _sre.SRE_Match object at 0x000002CEA5859238>
print(s[m.span()[0]:m.span()[1]]) #=> aaaaaaaaaaaaaabc