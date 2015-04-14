This function takes a member as an argument, and that first prints out all members who have 1 degree of separation from that member, then prints out all members that have 2 degrees of separation, then 3...  
Didn't print the same member twice.

petitions = {'a': [1,3,4,6], 'b': [2,3,4,6,7], 'c': [1,2,3,4,5,6]}
 
users = {1: ['a', 'b'], 2: ['b', 'c'], 3: ['a', 'b', 'c'], 4: ['a', 'b', 'c'], 5: ['c'], 6: ['c', 'b', 'c']}
 
def degree(user):
    degrees = {}
    checked = []
    for degree, petition in enumerate(petitions):
        Users = petitions[petition]
        if user in Users: Users.remove(user)
        _users_ = []
        for u in Users:
            if u not in checked:
                checked.append(u)
                _users_.append(u)
                degrees[degree] = _users_
    return degrees
degree(5)
{0: [1, 3, 4, 6], 1: [2], 2: [7]}
