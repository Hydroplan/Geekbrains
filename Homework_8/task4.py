def val_checker(func):
    def function(argument):
        def wrapper(*args):

            if not func(args[0]):
                raise ValueError
            else:
                return argument(args[0])

        return wrapper

    return function


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(-4))
