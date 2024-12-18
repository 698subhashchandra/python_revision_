friends = ['Sam', 'Sam1', 'Shubh']
starts_s = [friend for friend in friends if friend.startswith("S")]

print(starts_s)
print(starts_s)
print(friends is starts_s)
print('friends: ', id(friends), 'start_s:', id(starts_s))
