def my_decorator(original_function):
    
    def replacement_function():
        print('Do stuff before')
        original_function()
        print('Do stuff after')

    return replacement_function

# @my_decorator
def hello_world():
    print('Hello world!')

f = my_decorator(hello_world)

