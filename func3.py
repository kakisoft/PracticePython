
def func1(host=None, port=None, debug=None):
    if host is None:
        host = '127.0.0.1'
    print(host)


func1()
func1(host='0.0.0.0')





