import locale

print(locale.getdefaultlocale()) #=> ('ja_JP', 'cp932')　※例

print("あ".encode("sjis"))   #=> b'\x82\xa0'
print("あ".encode("euc-jp")) #=> b'\xa4\xa2'
print("あ".encode("utf-8"))  #=> b'\xe3\x81\x82'

print(b'\x82\xa0'.decode("sjis"))      #=> あ
print(b'\xa4\xa2'.decode("euc-jp"))    #=> あ
print(b'\xe3\x81\x82'.decode("utf-8")) #=> あ

FILE_NAME_FULL_PATH_1 = "resources/sample1.txt"

