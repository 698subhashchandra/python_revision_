friends = ['Rolf', 'Bob', 'Jen']
print('Jen' in friends)


movies_watched = {'The Matrix', 'Green Book', 'Her'}
user_movie = input('Enter something you have watched recently: ')

print(user_movie in movies_watched)


###############################3
movies_watched = {'The Matrix', 'Green Book', 'Her'}
user_movie = input('Enter something you have watched recently: ')

if user_movie in movies_watched:
    print(f'I have not watched {user_movie} too!')

else:
    print('I have not watched that yet.')

##################################################
number = 7
user_input = input("Enter 'y' if you would like to play: ").lower()

if user_input  == "y":
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) == 1:
        print("You were off by one.")
    else:
        print("Sorry, it's wrong!")