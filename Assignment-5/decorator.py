# decorator- function that takes another function as an argument
# and extends the behavior of the latter function without explicitly modifying it

import time

def profiling_decorator(Parameter):
    print(Parameter)

    def inner1(func):
        def inner(*args, **kwargs):
            before = time.time()

            func(*args, **kwargs)

            diff = time.time() - before

            print(f"time taken: {diff}")

        return inner

    return inner1


@profiling_decorator("demo")
def print_function():
    for i in range(5):
        time.sleep(1)
        print("Hello world")


print_function()


# Assignment

def output_decorator(Parameter):

    def inner1(func):
        def inner(*args, **kwargs):

            result = func(*args, **kwargs)

            print("##########################")
            print("#", Parameter)
            print("# input:", *args)
            print("# output:", result)
            print("##########################")

        return inner

    return inner1


@output_decorator("Adding")
def add(a, b):
    return a + b


add(4, 3)
