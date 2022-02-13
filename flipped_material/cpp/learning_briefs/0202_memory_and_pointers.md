# Memory and Pointers

## Learning Goals

*By the end of this module you should be able to answer the following:*

* What happens when you store data in your computer?
* What happens when you pass primitive data from a function to a second function?
* Why changing a local variable only changes the local variable and not the referenced variable?
* How we can use pointers and reference addresses to access memory?

## Code

*It is important to practice code and challenge our brain in new ways. Do all of the problems below, including the example problems. They will make you a better programmer.*

### Example Problems

*Example problems are best if you code them up yourself and store them. Don't just copy and paste, code them in and make them work. If you are really smart about it, you'll remake them slightly differently to really establish your learning.*

#### Problem: You need to find the memory address of where memory is stored

You can access the address by using the `&` operator.

```cpp
int foo = 2;
printf("foo has a value of %i is stored here: %p\n", foo, &foo);
```

#### Problem: You need to access the value of a variable through it's address

We can create a pointer for the address that stores the value.

```cpp
int foo = 2;
int *address_of_foo = &foo;
printf("The value of foo is %d and it is store here %p\n", *address_of_foo, &address_of_foo);
```

`&` gets the memory address
`*` accesses the value stored at the memory address

#### Problem: I need to change the value of a variable I have a pointer to

```cpp

We can access the value through the `*` operator. 

int foo = 2;
int *address_of_foo = &foo;
int foo2 = *address_of_foo;
printf("The value of foo is %d and it is store here %p\n", *address_of_foo, &address_of_foo);
*address_of_foo = 495;
printf("%d %d.\n", foo, foo2);
```

#### Problem: I've passed multiple variables to a function and I kind of want to return them both

You can pass the memory address for your variables into the function. Then use the memory deference operator to retrieve the actual variables.

```cpp
void foobar(int *a, int *b){
  *a = *a + 1;
  *b = *b -1;
}

int main(){
  int a = 10;
  int b = 10;
  foobar(&a, &b);
  printf("%d %d", a, b);
}
```

### Practice Problems

*Practice questions are essential to mastering a skill. Often, you will be asked to do things you haven't exactly done yet, or not at all. Be challenged by it and see if you can get Google, the person next to you, or the teacher, to help before you stop working.*

#### Practice 1: Terrible Calculator

Create a terrible calculator that doesn't return the answer but manipulates it in memory. Use the following code as a starting point. (NOTE: Change the _ to the right operators)

```cpp
void terribleAdd(int a, int b, int _answer){
  _answer = a + b;
}

int main(){
  int a = 10;
  int b = 10;
  int answer;
  
  terribleAdd(a, b, _answer);
  printf("%d %d %d", a, b, answer);
}
```

#### Practice 2: Swapping variables

Write a program that swaps two numbers using pointers.

```cmd
Example

Input

Input num1: 10
Input num2: 20
Output

Values after swapping:
Num1 = 20
Num2 = 10
```
