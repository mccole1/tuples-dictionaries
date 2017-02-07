#Tuples Exercises
my_tuple = (1, 2, "kitten", 4, "five")

#1. How would I access the third element in the tuple?
my_tuple[2]

#2. How would I access the element at the third index?
my_tuple[3]

# 3. What would I get if I did my_tuple[1]?
2

# 4. What are three ways I could access the last element of the tuple? (HINT: Look up the len method for Python tuples.)
my_tuple[4]
my_tuple[-1]
my_tuple[len(mytuple)-1]

# 5. How would I find the length of the tuple?
len(my_tuple)

# 6. How would I add the number 6 to the end of the my_tuple array? (Hint: look through the tuple lecture slides)
my_tuple + (6,)

# 7. Use the tuple below to complete the following seven problems:
my_tuple[0] # 1
my_tuple[2:3] # "kiten"
my_tuple[1:5] # 2, "kitten", 4, "five"
my_tuple[1:10] # 2, "kitten", 4, "five"
my_tuple[-1] # "five"
my_tuple[-1:-4] # []
my_tuple[-4:] # 2, "kitten", 4, "five"

#Dictionaries Exercises
# 1. Create a dictionary called vocabulary_words that contains 4 vocabulary words from this course as keys and their definitions as values.
vocabulary_words = {
    "tuple":"A sequence of immutable objects.", 
    "dictionary":"An unordered collection of key:value pairs that map one thing to another.",
    "loop":"a shortcut that allows you to perform the same set of tasks over and over again.",
    "list":"a type data structure used to store data."
    }

# 2. Given a dictionary of items and their prices, write a program that returns the most expensive item. Hint: Look at the Dictionary lecture to figure out how to iterate over a dictionary!
prices = { "banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
for my_key, my_value in prices.items():
    if my_value == max(prices.values()):
        print my_key


#3. Employee Dictionary
#a. Create an empty dictionary called Employee.
#b. Add some key:value pairs with the keys: name, age, and height and fill in values. For height, get user input.
Employee = {
    "name": "Molly",
    "age": "28",
    "height": raw_input("How tall are you?: ")}

#c. Update the age with a different value.
Employee["age"] = 22

#d. Check if the key 'name' exists. If it exists print the key and its value. Print dictionary if it doesn't exist.
"name" in Employee

#e. Check if the key 26 exists. If it exists print the key and its value. Print dictionary if it doesn't exist.
26 in Employee

#f. Iterate over the keys and print each one out.
for my_key in Employee:
    print my_key

#g. What is another way to get the list of keys?
Employee.keys()

#h. Iterate with key:value pairs and print them.
for my_key, my_value in Employee.items():
    print my_key, my_value

#i. What is another way to print all the key:value pairs?
Employee.items()

















