def add (x, y):
    print(x + y)

add(5, 6)


default_y = 3

def add(x, y=default_y):
    sum = x + y
    print(sum)


add(2)

default_y = 4
add(2)