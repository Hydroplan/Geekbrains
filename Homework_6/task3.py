import sys
import json

users_file = open('users.csv', 'r', encoding='utf-8')
hobby_file = open('hobby.csv', 'r', encoding='utf-8')

users_plus_hobby = {}
list_of_users = users_file.read().split('\n')
list_of_hobby = hobby_file.read().split('\n')

if len(list_of_users) < len(list_of_hobby):
    sys.exit(1)

counter = 0
for el in list_of_users:

    if counter < len(list_of_hobby):
        hobby = list_of_hobby[counter]
    else:
        hobby = None

    if not hobby:
        users_plus_hobby[el.replace(',', ' ')] = None
        users = users_file.readline()
    else:
        users_plus_hobby[el.replace(',', ' ')] = hobby
        users = users_file.readline()
        counter += 1

users_file.close()
hobby_file.close()
print(users_plus_hobby)
with open('result.json', 'w') as f:
    json.dump(users_plus_hobby, f)

with open('result.json', 'r') as f:
    print(json.load(f))
