friends = {'Bob', 'Rolf', 'Anne'}
abroad = {'Bob','Anne'}

local_friends  = friends.difference(abroad)
print(local_friends)

local_friends  = abroad.difference(friends)
print(local_friends)


local = {'Rolf'}
abroad = {'Bob', 'Anne'}

friends = local.union(abroad)
print(friends)



art = {'Bob', 'Jen', 'Rolf', 'Charlie'}
science = {'Bob', 'Jen', 'Adam', 'Anne'}

both = art.intersection(science)
print(both)

both = art.union(science)
print(both)
