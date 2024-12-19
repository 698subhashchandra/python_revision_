# def add(x, y):
#     return x + y
#
# print(add(5, 7))
#
#add = lambda x, y: x + y

#print (add(5, 7))



def double(x):
    return x * 2


sequence = [1, 3, 5, 6]
double = [(lambda x : x * 2)(x) for x in sequence]
double = list(map(double, sequence))