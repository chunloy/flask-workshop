# def shout(text):
#     return text.upper()


# def hello(func):
#     message = func("Hello World")
#     print(message)


# hello(shout)


def shout_decorator(func):
    def wrapper():
        return func().upper()

    return wrapper


@shout_decorator
def hello():
    return "Hello World"


print(hello())
