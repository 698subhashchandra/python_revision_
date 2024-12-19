def named(**kwargs):
    print(kwargs)

named(name="Bob", age=25)

#####################
def named(**kwargs):
    print(kwargs)

details = {"name": "Bob", "age": 25}

named(**details)

###########################
def named(**kwargs):
    print(kwargs)

def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

print_nicely(name="Bob", age=25)

############################3
def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1, 3, 5, 7 , name="Bob", age=25)