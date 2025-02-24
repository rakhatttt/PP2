#nonlocal

def func():
    x="jane"
    def func2():
        nonlocal x
        x="hello"

        func2()
        return x
print(func())