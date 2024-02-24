# Notes From Class


# list change positions

first = input('Enter first numnber: ')
second = input('Enter second number: ')
print('Before swapping:', first, second)
first, second = second, first
print('After swapping', first, second)


top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Pheonix']
top_cities[0], top_cities[4] = top_cities[4], top_cities[0]
print(top_cities)

# sort alphabetically 
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Pheonix']
top_cities.sort()
print(top_cities)

# sort numbers lowest to greatest
random_numbers = [2, 5, 0, -3, 4]
random_numbers.sort()
print(random_numbers)

# sort greatest to lowest or reverse alphabetical
random_numbers = [2, 5, 0, -3, 4]
random_numbers.sort(reverse=True)
print(random_numbers)

# temporary sorting but keeping original
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Pheonix']
print(sorted(top_cities))
print(top_cities)

list_name.sort() # sorts original list 
sorted(list_name) # gives a new sorted list but keeps original unchanged


# list checking presence

invited_guests = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Marie']
name = input('What is your name? ')
if name in invited_guests:
    print('Welcome!')
else:
    print('Your are not invited!')


invited_guests = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Marie']
name = input('What is your name? ')
if name not in invited_guests:
    print('You are not invited!')
else:
    print('Welcome!')
    

# copying lists

list_original = [1, 2, 3]
list_new = list_original
list_original[0] = -5 # changes the index space 0 to -5
print('Original:', list_original, '\nNew:', list_new) # both lists modifyed


# copying lists with slicing - allows two separate lists variables

list_original = [1, 2, 3]
list_new = list_original[:] # copies all elements
list_original[0] = -5  
print('Original:', list_original, '\nNew:', list_new) 


list_original = [1, 2, 3]
list_new = list_original[:2] # copies only first 2 - 0,1
list_original[0] = -5  
print('Original:', list_original, '\nNew:', list_new) 


#list comprehensions

numbers = []
for i in range(1, 101):   # generates numbers 1-100
    numbers.append(i)
print(numbers)


numbers = [i for i in range(1, 101)] # easier way to generate 1-100
print(numbers)


#omit numbers divisable by 3

numbers = [i for i in range(1, 101) if i % 3 != 0] 
print(numbers)


# nested lists

cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
print(cells[0]) # prints entire first set of 3 as that whole thing is index 1

print(cells[0][0]) # will print the single value within the pointed index: A1

print(cells[1][2]) # will print B3


# iterate list and print elements
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']] 
for x in cells:
    print('Element:', x)
  
    
# access individual elements in sublists

cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]

for x in cells:
    for y in x:
        print('Element: ', y)


table = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]

for row in table:
    for cell in row:
        print('Element: ', cell)
        
        
# prints in a way resembling a table        
        
table = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]

for row in table:
    for cell in row:
        print(cell, '', end='')
    print()
    

# Create a list that looks like the following

#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5

table = [i for i in range(1, 6)]  #creates a single list of 1-5
print(table)


table = [[i for i in range(1, 6)] for j in range(4)] # prints 4 lists of 1-5
print(table)


# multiply lists

list_numbers = [0, 1] * 10
print(list_numbers) # print the list above 10 times


# further string features

fav_band = 'Green Day'
print(fav_band[6]) # prints D

print(fav_band[:6]) # prints Green

text = 'please capitalize me'
text_cap = text.upper()
print(text_cap)


# String methods to return true or false

user_number= input('Please provide a number: ')
if user_number.isnumeric():
    print('Thank you, that\'s a correct number!')
else:
    print('Sorry', user_number, 'is not a number!')
    
    
# Intro Tuples

empty_tuple = ()

one_el_tuple_a = (1,)

one_el_tuple_b = 1, 

three_el_tuple = 1, 2, 3

# When you first create a tuple it stays that way forever (immutable)

# Tuple operations

user_data = ('John', 'American', 1964)
print(len(user_data)) # prints number of elements "length" of tuple


user_data = ('John', 'American', 1964)
if 'American' in user_data:
    print('This person comes from the US')
    
    
user_data = ('John', 'American', 1964)
for element in user_data: # prints each element of tupple on separate line
    print(element)
    
user_data = ('John', 'American', 1964) + ('teacher', 'male')

numbers = (0, 1) * 10


# Lists vs tuples

# Lists used when you want to have multiple values of same data type
# Male names, Temperatures - (strings, floats, int)

# tuples used to combine values of multiple types that form bigger data and are related


# Tuples in lists or vice versa


city_1 = ('London', 'UK', 8.98)
city_2 = ('Canberra', 'Australia', 0.4)
city_3 = ('Algiers', 'Algeria', 3.9)

capitals = [('London', 'UK', 8.98), ('Canberra', 'Australia', 0.4), ('Algiers', 'Algeria', 3.9)]
for capital in capitals:
    print("Name:", capital[0], 'Country:', capital[1], 'Population', capital[2])
    

user_data = ('John', 'American', 1964, [77.0, 79.2, 77.5])

user_data[3].append(79.6)


