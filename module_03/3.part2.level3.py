d = {'name1': 'id1', 'name2': 'id2', 'name3': 'id3'}
revert_d = {}

for i in d:
    revert_d[d[i]] = i

print(revert_d)