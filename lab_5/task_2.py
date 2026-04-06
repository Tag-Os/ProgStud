def decorator(func):
    def validation (x,y):
        if x > 0 and isinstance(y,str):
            return func(x, y)
        else:
            return func("incorrect")
    return validation

cheсk = decorator(print)
cheсk(1,"j")
cheсk(-4,"j")