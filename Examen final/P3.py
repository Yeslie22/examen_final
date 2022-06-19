import time
def mesureTime(function):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = function(*args, **kwargs)

        total = time.time() - start
        print("La demora de ejecución es de: {}".format(total))

        return result

    return wrapper

@mesureTime
def Resta(a, b):
    time.sleep(1)
    s = a-b
    return s


print(Resta(22,10))
print(Resta(2,1))