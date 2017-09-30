import requests
import doctest

TARGET_URL = "http://google.co.jp/"

#r = requests.get(TARGET_URL)
#print(r.text)


print("aaa")

def sample(query):
    """ requests sample that use qiita search api
    >>> 'title' in sample('python')
    True
    >>> 'totle' in sample('python')
    False
    """
    q = {'q':  query}
    r = requests.get('https://qiita.com/api/v1/search', params=q)
    return list(r.json()[0].keys())

if __name__ == "__main__":
    doctest.testmod()


print("bbb")
