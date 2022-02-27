# What are binary numbers and why should I care? 

## Learning Goals

By the end of this module you should be able to answer the following:

* What is Binary?
* How is it used in Computing?
* How to to be able to count in binary
* Translate a binary number to decimal 
* How to translate a denary IP number to binary 
* How to translate a binary IP number to denary
* What hexadecimal is and how it relates to computing
* How binary and denary relate to hexadecimal

## Dictionary Corner

To be able to answer a question, you need to be able to answer it. Pay special attention to Dictionary Corner because it arms you with the language to express yourself in this space. 

* Bit: a bit represents a logical state with one of two possible values 
* Byte: a group of 8 adjacent binary digits (8 bits) on which a computer uses as a unit
* Binary: The number system in an expression of base 2 notation
* Denary: The number system in an expression of base 10 notation
* Hexadecimal: The number system in an expression of base 16 notation


## Lesson

## Binary 

## What is Binary

Binary is a number system that uses 0 and 1. 

## How does it work? 

Converting to denary from binary is straight forward. Simply put each number into it's corresponding point and add them all together. 

For example: 

Example 1: `00000001` 

|128|64|32|16|8|4|2|1|
|---|---|---|---|---|---|---|---|
|0|0|0|0|0|0|0|1|
`00000001 -> 1 = 1`

Example 2: `10000000`

|128|64|32|16|8|4|2|1|
|---|---|---|---|---|---|---|---|
|1|0|0|0|0|0|0|0|

`10000000 -> 128 -> 128`

Example 3: 

`00000101`

|128|64|32|16|8|4|2|1|
|---|---|---|---|---|---|---|---|
|0|0|0|0|0|1|0|1|

`00000101 -> 4 + 1 -> 5`


Example 4: 
`10101010`

|128|64|32|16|8|4|2|1|
|---|---|---|---|---|---|---|---|
|1|0|1|0|1|0|1|0|

`10101010 -> 128 + 32 + 8 + 2 -> 70`

## Why do computers use binary? 

The short answer is hardware and the laws of physics. Every number (and everything is secretly a number) you give a computer is really an electrical signal. 

In the early days of computing it was very difficult to measure and control electrical signals with any precision. So, a decision was made to only distinguish if things were turned on or off. 


## How Binary relates to other number systems

We've already seen how to represent integers in binary. But because of the way we group memory together (8 bits make 1 byte) and working in binary is difficult we often use other base notation to work with them. 

Primarily, we use hexadecimal. What is hexadecimal, well it is a number system that goes from 0 to 15. 

|Hexadecimal|Decimal|
|--|--|
|0|0|
|1|1|
|2|2|
|3|3|
|4|4|
|5|5|
|6|6|
|7|7|
|8|8|
|9|9|
|A|10|
|B|11|
|C|12|
|D|13|
|E|14|
|F|15|

How do count to numbers higher than 15? Easy, you increment the "tens" or in this case the hexadecimal.  

|Hexadecimal|Decimal|
|--|--|
|10|16|
|11|17|
|12|18|


### Converting from decimal to Hex

You can use your calculator. Seriously. 
If you really want to learn how to do it, you can check out this awesome tutorial. 

https://learn.sparkfun.com/tutorials/hexadecimal/all 




### How is this useful? 

It just so happens that Hexadecimal is a neat way of talking about bits and bytes. For example: 

|hex|dec|bin|
|--|--|--|
00|00 |00000000
01|01 |00000001
0A|10 |00001010
0F|15 |00001111
40|64 |01000000
80|128|10000000
FF|255|11111111

### Why do we care? 

Because computers explicitly use base-2 number systems, we are often required to break groups of numbers up into chunks that are useful for computers. For example consider a subnet: `255.255.255.0` (we've used this a lot). 

|hex|dec|bin|
|--|--|--|
FF.FF.FF.00|255.255.255.0|11111111.11111111.11111111.11111111

## Technical Literacy 

 You should understand terms like bit, byte, binary, denary, hexadecimal. 

 You should also be able to convert binary to decimal and decimal to binary and be comfortable in using hex to represent basic binary and decimal numbers and the scientific calculator (or google) to convert complicated numbers to or from hex

# Practice and Challenges

## Questions

* What is a bit? 
* What is a byte? 
* What is binary?
* What is denary? 
* What is a hexadecimal number?
* Why do we use hexadecimal numbers in computing? 
* Why might binary and hexadecimal numbers be useful?

## Practice

* Convert 94 to binary and hex

|128|64|32|16|8|4|2|1|
|---|---|---|---|---|---|---|---|
|0|0|0|0|0|0|0|0|

* Convert 25 to binary and hex

|128|64|32|16|8|4|2|1|
|---|---|---|---|---|---|---|---|
|0|0|0|0|0|0|0|0|

* Convert 00111000 to decimal

|128|64|32|16|8|4|2|1|
|---|---|---|---|---|---|---|---|
|0|0|0|0|0|0|0|0|

* Convert 00000010 00111000 to decimal

|128|64|32|16|8|4|2|1|
|---|---|---|---|---|---|---|---|
|0|0|0|0|0|0|0|0|

|128|64|32|16|8|4|2|1|
|---|---|---|---|---|---|---|---|
|0|0|0|0|0|0|0|0|


* Convert 25 to decimal and binary

|128|64|32|16|8|4|2|1|
|---|---|---|---|---|---|---|---|
|0|0|0|0|0|0|0|0|

* Convert DC to decimal and binary

|128|64|32|16|8|4|2|1|
|---|---|---|---|---|---|---|---|
|0|0|0|0|0|0|0|0|

## Challenge

Represent the following IP numbers (and subnets) in both binary and Hex. Include working out. 

1. 192.168.1.1
2. 128.0.0.5
3. 255.255.255.128
4. 255.255.255.252
5. 255.255.255.0
6. 255.255.128.0



