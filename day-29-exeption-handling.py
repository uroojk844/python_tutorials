a = "1"
b = 1

isLoading = False


def waiting():
    if isLoading:
        print("Loading...")
    else:
        print("Loaded")


try:
    isLoading = True
    waiting()

    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        print(a / b)
    else:
        raise TypeError
except TypeError:
    print("Number should be int or float")
except NameError:
    print("Welcome, User")
except ZeroDivisionError:
    print("Number must be greater than 0")
except:
    print("Some error")
else:
    print("Completed")
finally:
    print("Finally block")
    isLoading = False

    waiting()
