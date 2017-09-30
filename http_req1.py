import urllib.request

TARGET_URL = "http://hatenablog.com/"

with urllib.request.urlopen(TARGET_URL) as res:
   html = res.read().decode("utf-8")
   print(html)

