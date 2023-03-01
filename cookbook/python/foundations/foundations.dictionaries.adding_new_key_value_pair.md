# How do you add new key-value pairs?

## Learning Goals

*By the end of this recipe you should be able to answer the following:*

* How can you add a new key-value pair to a dictionary?


## Concepts

In a dictionary, you can put lots of different pieces of information together. When you want to add more information to the dictionary, you put it in with a special name and a special value. You can do this as many times as you want, until your computer can't hold any more information. You can even start with an empty dictionary and add information to it as you go!

```python
monster = {'color': 'purple', 'points': 10}
monster['x_location'] = 3
monster['y_location'] = 15
monster['speed'] = 2.0
print(f"The value of speed is {monster['speed']}")
```

```shell
The value of speed is 2.0
```

## Practice Question

### Problem

Chad the wannabe hacker is on an adventure, and he needs your help to keep track of his progress. Chad wants to store information about the competitions he has participated, including the name of the competition, the number of participants, and the number of flags he found there.

Write a Python program that creates an empty dictionary called `flag_progress`, and then asks the user to enter the name of a competition Chad has participated in, the number of participants, and the number of flags he found there. Your program should add this information to the `flag_progress` dictionary as a new key-value pair.

Your program should then ask the user if they want to enter information about another competition. If they do, your program should repeat the process. If they don't, your program should print out the `flag_progress` dictionary with all the information.

### Hint

Use a while loop to keep asking the user for input until they don't want to enter any more information.

To add a new key-value pair to the `flag_progress` dictionary, you can use the name of the competition as the key.

You can use the input() function to ask the user for input.