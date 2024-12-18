friend_ages = {'Rolf': 24, 'Adam': 30, 'Anne': 24}

friend_ages['Rolf'] = 20

print(friend_ages['Adam'])




friends = [
    {'name': 'Rolf', 'age': 24},
    {'name': 'Adam', 'age': 54},
    {'name': 'Anne', 'age': 34},
]

#print(friends)
print(friends[1]['name'],friends[1]['age'])


########################################33
student_attendence = {'Rolf': 96, 'Bob':80, 'Anne': 100}

for student ,attendence in student_attendence.items():
    print( f"{student}: {attendence}")

