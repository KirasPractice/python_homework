import logging

logger = logging.getLogger(__name__ + 'log-decorator')
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))


def logger_decorator(func):
    def wrapper(*args, **kwargs):
        logger.log(logging.INFO, f"Function: {func.__name__}" )
        logger.log(logging.INFO, f"Positional Parameters: { list(args) if args else 'none'}")
        logger.log(logging.INFO, f"Keyword Parmaters: { kwargs if kwargs else 'none'}")
        result = func(*args, **kwargs)
        logger.log(logging.INFO, f"Return: {result}")
        return result
    return wrapper

        
    wrapper

@logger_decorator
def no_params():
    print("Hello World")


@logger_decorator
def boolean(*args):
    return True


@logger_decorator
def kwordargs(**kwargs):
    return logger_decorator

no_params()
boolean("isGood")
kwordargs(first="Akira", last="Royal")

# def sprinkles_decrator(function):
# def wrapper(*args, **kwrags):
# print("Heres sprinkles")
# function(*args, **kwarsg)
# return wrapper

# def add_fudge(function):
#     def wrapper(*args, **kwargs):
#         print("You add fudge")
#         function(*args, **kwargs)
#     return wrapper

# @logger_decorator
# @add_fusge_decorator
# def get_icecream():
#     print("Heres ur icecream")
# get_icecream()


