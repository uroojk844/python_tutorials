f = None
try:
    f = open("README.m")

    # def next(size=64):
    #     print(f.read(64), end="")

    # next()
    # next()
    # next()

    # print(f.readline())
    # print(f.readline())
    # print(f.readline())

    # print(f.readlines())

    print(f.readable())
except FileNotFoundError:
    print("File not found! Please check filename.")
except:
    print("Something went wrong!")
finally:
    if f is not None:
        f.close()
