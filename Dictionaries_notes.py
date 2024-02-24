# Dictionaries

# Collection used to store key value pairs

email = {
        'Anne Stahl': 'astahl@gmail.com',
        'Peter Small': 'peters@yandex.com',
        'Mark Steel': 'mark@steel.com'
}

print(emails['Mark Steel']) # prints value of the key - in this case email

# lists cannot be keys but can be values

# Strings, Integers, Floats and Tuples can be Keys

# Dictionary Operations

grades = {}
grades['John'] = 'A-'  # Adding key and value to empty dictionary
grades['Anne'] = 'B'

print(grades)


grades.update(['John':'A'])

print(len(grades)) # shows length of the dictionary

if 'John' in grades:
    print('John got:', grades['John'])
    
    
del grades['John']


# Iterate on Dictionaries

grades = {}
grades['John'] = 'A-'  # Adding key and value to empty dictionary
grades['Anne'] = 'B'

for el in grades:
    print(el)

for el in grades.keys():
    print(el)

for el in grades.values():
    print(el)
    
for person, grade in grades.items()
    print(person, 'got', grade)
    