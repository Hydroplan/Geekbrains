def type_logger(func):
    def wrapper(*args, **kwargs):
        func_name = str(func)[10:str(func).find(' at ')]
        for el in args:
            args_type = f'({el}: {type(el)})'
            print(func_name + str(args_type))

        for el in kwargs:
            
            kwargs_type = f'({kwargs[el]}: {type(kwargs[el])})'
            print(func_name + str(kwargs_type))

    return wrapper


@type_logger
def calc_cube(x, y, z=1, w=1):
    return (x * y + z + w) ** 3


calc_cube(4, 6, z=10, w=32)
