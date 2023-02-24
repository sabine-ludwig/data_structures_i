'''Task 1: Dictionary, Set and Tuple
Given the following three scenarios, choose the best data structure 
(between a dictionary, set, or tuple) to efficiently store the data. 
Each scenario ties directly to one data structure. 
Each data structure will be used only once. 
You will need to determine which data structure is best for which scenario, 
and then implement the data structure in Python.
'''

'''
1. Store the months of the year as strings. 
Determine the month in the data structure in which National Pi Day exists 
and print that month to the console. 
HINT: The number for Pi, when converted to an Integer, 
is related to the stored location of the correct month.
'''

# tuple (months will not change)

months_of_year = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
pi = int(3.14)
# print(months_of_year[pi - 1]) #index for month 3 is 2

'''
2. Store five fruits or vegetables.
a. Add two of your favorite fruits and two of your favorite vegetables to the collection.
b. Iterate over the collection and print each one to the console. 
'''

# set (can change based on mood/person/etc but there will never be duplicates)

fruits_and_veggies = {'strawberry', 'mango', 'avocado', 'spinach', 'broccoli'}
fruits_and_veggies.update(['cauliflower', 'raspberry'])
# fruits_and_veggies.add('raspberry')

# print(fruits_and_veggies)
# for item in fruits_and_veggies:
#     print(item)

'''
3. Store information about a user profile. 
Use literal string interpolation to print the users profile information to the console. 
The profile should consist of the following information:
a. First Name
b. Last Name
c. Email Address
d. Phone Number
'''

# dictionary 

user = {
    "first_name": "Sabine",
    "last_name": "Ludwig",
    "email_address": "sabinemichelle@",
    "phone_number": "(xxx) xxx-xxxx"
}

# print(user["first_name"])
# print(user.get("last_name"))

# for key, value in user.items():
#     print()
#     print(f"The key {key} has a value of {value}.")
    

'''Task 2: List of Dictionaries
Use a list to store the dictionary of your immediate family members, 
with each index of the list storing its own dictionary. 
Dictionary should contain the following keys:
First name
Last name
Relation to you
'''

family_members = [
    {
        "first_name": "Sue",
        "last_nanem": "Ludwig",
        "relation": "mother"
    },
    {
        "first_name": "Francis",
        "last_name": "Ludwig",
        "relation": "father"
    },
    {
        "first_name": "Oliver",
        "last_name": "Ludwig",
        "relation": "sibling"
    },
    {
        "first_name": "Koll",
        "last_name": "Roberts",
        "relation": "spouse"
    }
]

# print(family_members[0]["first_name"])
# print(f'{family_members[0]["first_name"].title()} is my {family_members[0]["relation"]}.')

def display_fam(list):
    for member in family_members:
        print(f'{member["first_name"].title()} is my {member["relation"]}.')

