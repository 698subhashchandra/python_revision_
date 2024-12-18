

def user_age_in_seconds():
    user_age = int(input("Enter Your age: "))
    age_seconds = user_age * 365* 24 * 60 * 60
    print(f"Your age in seconds is {age_seconds}.")


print("Welcome to the age in seconds program!")

user_age_in_seconds()

print("GOODBYE!")

friends = []

def add_friend():
    friends.append("Rolf")


add_friend()
add_friend()
add_friend()

print(friends)