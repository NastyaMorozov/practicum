#Декораторы
DEBUG = True
def trace(function):
    if not DEBUG:
        print("Была вызвана функция")
        return function

    def wr(*args):
        print(f"Функция: '{function.__name__}' начиная с параметра: {args}")
        res = function(args)
        print(f"Время: (time.time()")
        print(f"Result: {res}")
        return res
    return wr
trace()
#Я постаралась сделать декоратор как смогла, надеюсь получилось то, что вы просили