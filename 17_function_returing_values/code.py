# def add (x,y):
#     return x +y
#
#
# add(5,8)
# result = add(5,8)
# print(result)
# result = add(5, 8)
# print(result)


def add(x,y):
    print(x+y)
    return x+y

result = add(5, 8)
print(result)
#########################################

def add(x,y):
    return
    print(x+y)     #### NONE Result
    return x+y

result = add(5, 8)
print(result)

##########################################
def divide(dividend, divisor):
    if divisor != 0 :
        return dividend / divisor
    else:
        return " YOU FOOL!"   ## Both return function worked .Depends on condition

result = divide(15, 3)
print(result)