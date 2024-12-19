def say_hello(name, surname):
    print(f"Hello, {name} {surname}")

say_hello(surname="Bob", name="Smith")



def divide(divided, divisor):
    if divisor != 0:
        print(divided / divisor)
    else:
        print("You Fool!")

divide(15, 5)