# Strings, Variables, and Operations in C 

### Learning Goals

*By the end of this module you should be able to answer the following:*

* In C, how do you print a string to the console?
* How would you format a string so variables join neatly?
* If you had to, how would you store something to memory?
* How do you join two strings together?
* How would you capture user input?
* What other primitive data types are there? 
* How do you add/subtract/multiply/divide numbers together?

## Examples

### Problem: We want to print a simple string.

We can use the print function to print most data types to the standard console. 

```cpp
int main(void){
    printf("hello world\n");
    return 0;
}
```

### Problem: we need to store something in a variable and then print it.

You can store your data in a variable.

```cpp
int main(void){
    int foo = 5;
    printf("foo is %d\n", foo);
    return 0;
}
```

A variable acts as a label so you can tell the computer what block of memory to get. 


### Problem: I want to put a variable in a complex string. Can I format variables into strings? This could also be used as "I want to store strings!"

```cpp
int main(void){
    char givenName[] = "Ada";
    char familyName[] = "Lovelace";
    printf("The first programmer's name was %s %s\n", givenName, familyName);
    return 0;
}
```
### Problem: How can I do some maths calculations? 

The true maths games!

```cpp
#include <math.h>
int main(void){
    printf("%d\n", 3+2); // 3 + 2 = 5
    printf("%d\n",3-2); // 3 - 2 = 1
    printf("%d\n",3*2); // 3 * 2 = 6
    printf("%d\n",3/2); // 3 / 2 = 1.5 (be careful of old versions)
    printf("%g\n",pow(3, 2)));// 3^2 = 3*3 = 9
    printf("%d\n",3%2); // 3%2 = 1 (3/2 = 1 with 1 remaining
    return 0;
}
```

NERD ALERT! What's going on with that `%g` has the teacher lost the plot? 

NERD ALERT! What's going on with that % operator? It's weird, right? 

Maybe you should google to check this stuff out!

### Problem: I want to get a users input? 

You can use the scanf function. 

```cpp
int main(void){
    float foo; 
    printf("guess a number\n");
    scanf("%g", &foo);
    printf("You guessed %g", foo);
    return 0;
}
```

## Practice Questions

You can do all of these in the same piece of code on replit

### Create a code block that prints out the following text:

1. "Hello world"
2. "Hello again"
3. "Printing is fun!"
4. "Yay! Printing"

### Given the following variables produce the required output

```cpp
hens = 25 + 30/6  
roosters = 100 - 25 * 3  
```

print the following output  

```bash
"I will now count my chickens"
"I have 30.0 hens and 25 Rosters" 
```

### Create a program with the following variables:

```cpp
cars = 100
space_in_cars = 4  # excluding the driver
drivers = 30 
passengers = 90
```

The program must calculate:

1. How many cars, if any, are left over
2. The maximum car pool capacity (based on both driver capacity and total car capacity)
3. The average number of passengers per car

### Calendar wonder land

You are to create a program that can accept user input and display it. The program that you ask to write asks a user for the following input:

* Their given name
* The day of their birth
* The month of their birth
* The year of their birth

Your program must calculate an approximation* of how many days that person has been alive and then output it in the following format: 

`"Hi {given_name}, you have been alive for approximately {n_days}"`
e.g., `"Hi Adam, you have been alive for approximately 9999 days"`

NOTE: calculating the exact number of days isn't trivial. An approximation is fine. Don't over think it. Or do, there is glory and fame for those who can do it.