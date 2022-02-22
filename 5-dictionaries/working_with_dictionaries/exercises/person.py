# 6-1. Person: Use a dictionary to store information about a person you
# know. Store their first name, last name, age, and the city in which
# they live. Youshould have keys such as first_name, last_name, age,
# and city. Print eachpiece of information stored in your dictionary.
person = {
    'first_name': 'fabricio',
    'last_name': 'santiago',
    'age': 21,
    'city': 'timoteo',
    }

for key in person:
    print(person[key])
