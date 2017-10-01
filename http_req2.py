import requests
import doctest

TARGET_URL = "http://challenge-your-limits.herokuapp.com/"

print("aaa")

def req_sample2():
    # q = {'q':  query}
    # r = requests.get('https://qiita.com/api/v1/search', params=q)
    r1 = requests.get(TARGET_URL)
    r2 = requests.post("http://httpbin.org/post", data = {"key":"value"})
    r3 = requests.put("http://httpbin.org/put", data = {"key":"value"})
    r4 = requests.delete("http://httpbin.org/delete")
    r5 = requests.head("http://httpbin.org/get")
    r6 = requests.options("http://httpbin.org/get")
    print(r1.text)

if __name__ == "__main__":
    # doctest.testmod()
    #doctest.testmod()
    req_sample2()


print("bbb")
