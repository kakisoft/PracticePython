# 文字コード

## Python3では、文字列に関する型は2種類ある。
 - str型(Unicode専用)
 - byte型(任意のエンコーディング)


Windowsの標準出力では、CP932というエンコーディングが採用されている。このため、str文字列を標準出力したりファイルに書き出したりする場合は、標準ではCP932への変換が自動的に動作する。  

Pythonは明示的に変換しなくても、標準出力等をする場合、自動的にシステムのエンコーディングに変換してから出力しようとする。  

Windowsの場合は、CP932へ変換しようとするため、CP932に変換出来ない場合は、UnicodeEncodeError例外が発生する。  

fileOpen時にキャスト。

```py
import json

f = open(r'C:\Users\UserName\Desktop\test.json','r',encoding="utf-8")
data = json.load(f)
print(data)
```


## UTF-8ではBOMが付くものとそうでないものがある
```py
import json

f = open(r'C:\Users\UserName\Desktop\test.json','r',encoding="utf-8_sig")
data = json.load(f)
print(data)
```

## 旧記法
```
# coding: utf-8

Python2 までは、ソースに日本語が含まれていた場合、１行目か2行目に↑の
奇術が必要だった。Python3からは不要。
```

