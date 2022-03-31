<style>
  table {width: 100%;}
</style>

# Practice Python Exam

NOTE: The exam next week is scheduled for 50 minutes. The time limit is a part of the challenge for scaling purposes. The end result will be scaled. So, if the average mark in the class is say 35% that is a C result.

NOTE 2: The exam is scheduled in the second session of our double. If you are in line 2 Cyber Security we can either attempt to do it in line 2 or you can schedule to do it in any of my teaching lines between Monday and Wednesday. I am happy to get you excused from a different class. 

Scores calculation: 

1 point questions: 

0 points | 1 point
:-- | :--
Answer was not submitted or was not able to be assessed | Answer is given and meet expectations for knowledge or understanding on the topic

2 point questions: 

0 | 1 | 2
:--|:--|:--
Answer was not submitted or was not able to be assessed |  Answer is given but does not meet expectations for knowledge or understanding on the topic | Answer is given and meet expectations for knowledge or understanding on the topic

4 point questions: 

0 | 1 | 2 | 3 | 4
:--|:--|:--|:--|:--
Answer was not submitted or was not able to be assessed | Answer was incomplete and showed a limited understanding of the topic space (1 or 2 of 5 (simple) bugs found) | The answer submitted was a partial response however it showed a growing understanding of the topic space (>2 bugs found ) | The answer submitted was a partial response but answered the majority of the question (>=4 bugs found) | Answer submitted is complete (>=5 bugs found)

## Scope of questions: 

* Variables and conditions
* Functions
* Iteration and Data Structures 
* Files and Exceptions

### MC: What is the result of the following code? (1 mark)

```python

a = (8-3)/(5**2/4)
print(f"{a}")

```

1. 0.8
2. 7.97
3. "5/2.5"
4. 2

### MC: Consider the following code block and select the most accurate answer (1 mark)

```python
def hit(attacker, defender, weapon, damage=1):
    return f"{attacker.title()} hit {defender.title()} with a {weapon} for {damage} points of damage"

print(hit("ada", 'bob', 'sword', 8))
print(hit("charles", 'erin', 'mace', 4))
print(hit("fred", 'georgia', 'sharp stick'))
```

1. ```text
Ada hit Bob with a sword for 8 points of damage
Charles hit Erin with a mace for 4 points of damage
Fred hit Georgia with a sharp stick for 1 points of damage
```

2. ```text
ada hit bob with a sword for 8 points of damage
charles hit erin with a mace for 4 points of damage
fred hit georgia with a sharp stick for 1 points of damage
```

3. This code will not work as intended because lines 4 and 5 have integers and they should be strings
4. This code will not compile because line 6 does not have a damage

### Short Answer: What is the likely output of the following code and why? (2 marks)

```python
j = 1
c = j
while c > 0:
    print("*" * c)
    if c == 5: 
        j = 0 - 1
    c+= j
```

1. This is clearly the work of witchcraft
2. This will likely have an exception due to the `print("*" * c)` being nonsense
3. This code attempts to create a triangle that is 9 high and 5 across but it is broken by the while condition
4. This code attempts to create a triangle that is 9 high and 5 across and is successful

### Long answer: There are at least 5 errors in the following code. (4 marks)

```text

print("List of months: [January, February, March, April, May, June, July, August, September, October, November, December]")
month_name = input("Input the name of Month: "):

if month_name == "February"
	print("No. of days: 28/29 days")
elif month_name in ("April", "June', "September", "November"):
	print("No. of days: 30 days")
elif month_name in ("January", "March", "May". "July", "August", "October", "December"):
	print("No. of days: 31 day")
print("Wrong month name") 

```

```text

answer1: 


answer2: 


answer3:


answer4:



answer5:



```
