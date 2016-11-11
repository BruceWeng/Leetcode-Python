users = [
    {'id': 1, 'name': 'Olivia'},
    {'id': 2, 'name': 'Gloria'},
    {'id': 3, 'name': 'Bruce'}
]

compareById = sorted(users, key = lambda user : user['id'])
compareByName = sorted(users, key = lambda user : user['name'])

print 'Sort By Id: ' + str(compareById)
print 'Sort By Name: ' + str(compareByName)
