# How does something work?

## Learning Goals

*By the end of this recipe you should be able to answer the following:*

* Why might you want to store dictionaries in a list. 
* How can you create a list of dictionaries?
* How can you access individual dictionaries in a list of dictionaries?

## Concepts

Sometimes we want to keep many dictionaries together, and we can do this by putting them in a list. This is called nesting and can be helpful.

```python
# Start with an empty list.
programmers = []

# Make a new programmer and add her to the list.
new_programmer = {
    'last': 'Hopper',
    'first': 'Grace',
    'username': 'ghopper',
}
programmers.append(new_programmer)

# Make another new programmer, and add her to the list.
new_programmer = {
    'last': 'Holberton',
    'first': 'Frances',
    'username': 'fholberton',
}
programmers.append(new_programmer)

for programmer in programmers:
  for key in programmer:
    print(f"{key}: {programmer[key]}")
  print()
```

## Practice Question

From the following list find:

* The names and ages of the youngest student
* The mean age of all students (bonus if you can round to two decimal points)
* The mode age of students (hold off on using the statistics library)

```python
students = [{'given_name': 'Joyce', 'family_name': 'Reed', 'age': 17}, {'given_name': 'Ada', 'family_name': 'Lovelace', 'age': 14}, {'given_name': 'Albert', 'family_name': 'Lorino', 'age': 15}, {'given_name': 'Justin', 'family_name': 'Otero', 'age': 16}, {'given_name': 'Wyatt', 'family_name': 'Limerick', 'age': 16}, {'given_name': 'Bobby', 'family_name': 'Ward', 'age': 18}, {'given_name': 'Jeffrey', 'family_name': 'Winters', 'age': 16}, 
{'given_name': 'Adela', 'family_name': 'Gray', 'age': 16}, {'given_name': 'Susan', 'family_name': 'Hicks', 'age': 18}, {'given_name': 'Pauline', 'family_name': 'Posey', 'age': 17}, {'given_name': 'Christopher', 'family_name': 'Miller', 'age': 18}, {'given_name': 'William', 'family_name': 'Calkins', 'age': 15}, {'given_name': 'Charles', 'family_name': 'Williams', 'age': 15}, {'given_name': 'Jason', 'family_name': 'Dennehy', 'age': 17}, {'given_name': 'Daniel', 'family_name': 'Christopherso', 'age': 17}, {'given_name': 'Thomas', 'family_name': 'Becnel', 'age': 15}, {'given_name': 'Claudia', 'family_name': 'Jennings', 'age': 16}, {'given_name': 'Dane', 'family_name': 'Lorino', 'age': 16}, {'given_name': 'Jason', 'family_name': 'Guthrie', 'age': 17}, {'given_name': 'Jose', 'family_name': 'Bushnell', 'age': 15}, {'given_name': 'Ronald', 'family_name': 'Lang', 'age': 17}, {'given_name': 'Rickie', 'family_name': 'Catlett', 'age': 16}, {'given_name': 'Brad', 'family_name': 'Hokula', 'age': 16}, {'given_name': 'Glenn', 'family_name': 'Cintron', 'age': 16}, {'given_name': 'Donald', 'family_name': 'Williams', 'age': 15}, {'given_name': 'Mark', 'family_name': 'Bilger', 'age': 15}, {'given_name': 'Jona', 'family_name': 'Buchanan', 'age': 15}, {'given_name': 'Angelo', 'family_name': 
'Melendez', 'age': 18}, {'given_name': 'Jeffrey', 'family_name': 'Dyson', 'age': 16}, 
{'given_name': 'Dennis', 'family_name': 'Burlett', 'age': 18}, {'given_name': 'Robert', 'family_name': 'Gregory', 'age': 15}, {'given_name': 'Grace', 'family_name': 'Dennis', 'age': 18}, {'given_name': 'Sherrie', 'family_name': 'Owen', 'age': 16}, {'given_name': 'Gary', 'family_name': 'Sims', 'age': 16}, {'given_name': 'Christopher', 'family_name': 'Walsh', 'age': 15}, {'given_name': 'Steven', 'family_name': 'Bianchi', 'age': 
17}, {'given_name': 'David', 'family_name': 'Wilson', 'age': 17}, {'given_name': 'Ann', 'family_name': 'Reichert', 'age': 15}, {'given_name': 'Charles', 'family_name': 'Richardson', 'age': 18}, {'given_name': 'Mary', 'family_name': 'Hickman', 'age': 18}, {'given_name': 'Richard', 'family_name': 'Delgado', 'age': 17}, {'given_name': 'Russell', 'family_name': 'Fountain', 'age': 17}, {'given_name': 'Mary', 'family_name': 'Norwood', 'age': 18}, {'given_name': 'Mildred', 'family_name': 'Hedgepeth', 'age': 18}, {'given_name': 'Thomas', 'family_name': 'Evans', 'age': 18}, {'given_name': 'Jose', 'family_name': 'Smith', 'age': 15}, {'given_name': 'Robert', 'family_name': 'Rice', 'age': 18}, {'given_name': 'Jessica', 'family_name': 'Monteros', 'age': 15}, {'given_name': 'Karen', 'family_name': 'Simmons', 'age': 17}, {'given_name': 'Ada', 'family_name': 'Lovelace', 'age': 14}, {'given_name': 'Elizabeth', 'family_name': 'Cook', 'age': 17}, {'given_name': 'Tammy', 'family_name': 'Meister', 'age': 18}, {'given_name': 'Franklin', 'family_name': 'Streets', 'age': 18}, {'given_name': 'Debra', 'family_name': 'Sanders', 'age': 15}, {'given_name': 'Brian', 'family_name': 'Edwards', 'age': 16}, {'given_name': 'Lonnie', 'family_name': 'Parks', 'age': 17}, {'given_name': 'Caren', 'family_name': 'Willis', 'age': 17}, {'given_name': 'Karan', 'family_name': 'Reed', 'age': 15}, {'given_name': 'Edna', 'family_name': 'Burke', 'age': 15}, {'given_name': 'Rhona', 'family_name': 'Ouimet', 'age': 17}, {'given_name': 'Dana', 'family_name': 'Ali', 'age': 15}, {'given_name': 'Pamela', 'family_name': 'Stafford', 'age': 15}, {'given_name': 'Phillip', 'family_name': 'Weaver', 'age': 16}, {'given_name': 'Thomas', 'family_name': 'Warmbier', 'age': 16}, {'given_name': 'Patricia', 'family_name': 'Gonzalez', 'age': 18}, {'given_name': 'Eugene', 'family_name': 'Reed', 'age': 15}, {'given_name': 'Harry', 
'family_name': 'Naef', 'age': 15}, {'given_name': 'Mary', 'family_name': 'Knight', 'age': 18}, {'given_name': 'Darnell', 'family_name': 'Filippini', 'age': 17}, {'given_name': 'Gerald', 'family_name': 'Williams', 'age': 17}, {'given_name': 'Gerald', 'family_name': 'Matthews', 'age': 15}, {'given_name': 'Kathy', 'family_name': 'Adens', 'age': 
15}, {'given_name': 'Lonny', 'family_name': 'Oros', 'age': 18}, {'given_name': 'Allen', 'family_name': 'Cornett', 'age': 15}, {'given_name': 'Diane', 'family_name': 'Peters', 'age': 18}, {'given_name': 'Jennifer', 'family_name': 'Kelly', 'age': 16}, {'given_name': 'Michael', 'family_name': 'Sollie', 'age': 16}, {'given_name': 'Michael', 'family_name': 'Abron', 'age': 15}, {'given_name': 'Shawnee', 'family_name': 'Lamb', 'age': 17}, {'given_name': 'Terresa', 'family_name': 'Swanson', 'age': 18}, {'given_name': 'Joe', 'family_name': 'Jacobs', 'age': 17}, {'given_name': 'Anne', 'family_name': 'Williams', 'age': 18}, {'given_name': 'Cathy', 'family_name': 'Caravati', 'age': 18}, {'given_name': 'Michael', 'family_name': 'Gaudet', 'age': 16}, {'given_name': 'Rosanna', 'family_name': 'Sanchez', 'age': 15}, {'given_name': 'Kristina', 'family_name': 'Skinner', 'age': 16}, {'given_name': 'John', 'family_name': 'Lundberg', 'age': 17}, {'given_name': 'Samantha', 'family_name': 'Wood', 'age': 15}, {'given_name': 'Leslie', 'family_name': 'Garcia', 'age': 17}, {'given_name': 'Theodore', 'family_name': 'Parker', 'age': 15}, {'given_name': 'Gertrude', 'family_name': 'Rudish', 'age': 18}, {'given_name': 'Kevin', 'family_name': 'Baxter', 'age': 18}, {'given_name': 'George', 'family_name': 'Ulberg', 'age': 16}, {'given_name': 'Tonya', 'family_name': 'Hawkins', 'age': 18}, {'given_name': 'Michael', 'family_name': 'Bannerman', 'age': 15}, {'given_name': 'James', 'family_name': 'Slocum', 'age': 15}, {'given_name': 'Thomas', 'family_name': 'Nichols', 'age': 16}, {'given_name': 'Ada', 'family_name': 'Lovelace', 'age': 14}, {'given_name': 'Roger', 'family_name': 'Cotton', 'age': 16}, {'given_name': 'Christi', 'family_name': 'Morales', 'age': 17}, {'given_name': 'William', 'family_name': 'Chrostowski', 'age': 15}, {'given_name': 'Miguel', 'family_name': 'Wood', 'age': 18}, {'given_name': 'Ella', 'family_name': 'Diaz', 'age': 16}]

# your code goes here
# your code goes here
# your code goes here
# your code goes here
# your code goes here
# your code goes here
print(f"The lowest age is {...} and it is {...}")
print(f"The mean age of the student body is {...}")
```
