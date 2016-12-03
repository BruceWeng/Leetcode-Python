def f():
    n = 42

    def get(n):
        return n

    def next():
        n += 1
        return

    return {'get': get, 'next': next}

o = f()
print o['get'](1) # 1
o['next']
print o['get'] # get function reference
