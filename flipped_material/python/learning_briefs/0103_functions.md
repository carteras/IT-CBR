# Functions

## Learning Goals

*By the end of this module you should be able to answer the following:*

* What are functions?
* How do we define functions in python?
* How do we print to STD:Console in a function?
* How do functions accept arguments?
* How can we return from a function back to the main code?
* and a sneaky peak into string functions ;)

## Code

*It is important to practice code and challenge our brain in new ways. Do all of the problems below, including the example problems. They will make you a better programmer.*

### Example Problems

*Example problems are best if you code them up yourself and store them. Don't just copy and paste, code them in and make them work. If you are really smart about it, you'll remake them slightly differently to really establish your learning.*

#### Problem: You keep copying and pasting some pretty simple code together. (simple function)

```python
def greet_user():
    print("hello!")
greet_user()
```

### Problem: You need to pass a variable into a function

```python
def greet_user(username):
    print(f"Hello, {username}")

user_to_greet = "Ada"
greet_user(user_to_greet)
```

### Problem: Your teacher keeps complaining that functions should return something

```python
def greet_user(username):
    return f"Hello, {username}"

user_to_greet = "Ada"
print(greet_user(user_to_greet))
```

### Problem: For clarity, I want to be very precise on how variables are used in a function

```python
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")

describe_pet(animal_type='dog', pet_name='sam')
```

```python
def describe_pet(animal_type, pet_name):
    return f"I have a {animal_type}. My {animal_type}'s name is {pet_name}."

print(describe_pet(animal_type='dog', pet_name='sam'))
```

#### Problem: I need default variables sometimes, like the first time I am calling a function

```python
def describe_pet(pet_name, animal_type=dog):
    return f"I have a {animal_type}. My {animal_type}'s name is {pet_name}."

print(describe_pet(pet_name='sam'))
print(describe_pet(animal_type='cat', pet_name='kaylee'))

```

### Practice Problems

*Practice questions are essential to mastering a skill. Often, you will be asked to do things you haven't exactly done yet, or not at all. Be challenged by it and see if you can get Google, the person next to you, or the teacher, to help before you stop working.*

#### Practice Question 1

Write a function called `display_message()`. This function will print a string telling everyone what you are learning about in this brief. 

#### Practice Question 2

Write a function called `best_friend(name)`. This function accepts one parameter, name. The function should print return a string such as "my best friend is Timmy". Call this function, making sure to include a name in the function call, and make sure you print the return string.  

#### Practice Question 3

Write a function called `make_shirt(...)`. This function accepts a size and the text of the message that should be printed on the shirt. The function will return a string that summarises the size of the shirt and the message printed on it.

* Call this function once using positional arguments (foo("blah", 18))
* Call this function a second time using keyword arguments foo(name="blah", age=18)
* call this function a third time, this time using the keyword arguments out of positional order foo(age=18, name="blah")

#### Practice Question 4

Create a 3 functions `s_shirts(...)`, `m_shirts(...)`, `l_shirts(...)`. These functions only accept one parameter, the words that are on the shirt. From inside these functions, you must call `make_shirt(...)` with the appropriate arguments.

#### Practice Question 5

Write a function called `describe_city(...)`. This function accepts the name of a city and its country. The function should return a simple sentence such as "Sydney is in Australia". This function defaults the country code to Australia. Make sure you print the return string from this function.

* Call your function 3 times using cities in Australia
* Call your function 3 times using cities that aren't in Australia
* Ensure that all city and country names will print with a capital letter!

NOTE: python has a bunch of string functions (which we will get too soon) but you should be aware of them. Here is an example, but I highly recommend that you start reading documentation sooner rather than later.

**str.title()**

Return a titlecased version of the string where words start with an uppercase character and the remaining characters are lowercase.

For example:

```python
>>> 'hello world'.title()
'Hello World'
```

https://docs.python.org/3/library/stdtypes.html

### Meaty question (not a challenge :))

Write a program that takes the following function calls: 

```python
print(formatted_name(given_name="augusta", middle_name="ada", family_name="lovelace"))
print(formatted_name(given_name="bob", family_name="bobbington"))
print(formatted_name(given_name="charles", family_name="babbage"))
```

and outputs the following:

```cmd
Lovelace, Augusta Ada
Bobbington, Bob
Babbage, Charles
```
