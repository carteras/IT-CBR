# Structural Pattern Matching

NOTE: Work in progress.

How can we use structural pattern matching to select logical statements?

**author:** [carteras](https://github.com/carteras)

## Topics covered

"At the end of this recipe, you will be able to answer the following questions or solve the following problems"

* What is structural pattern matching?
* How to use structural pattern matching
* Why would you use structural pattern matching over if/else

### Things you'll need to know before you start this

* if/else/else-if in python
* string manipulation in python
* lists in python

### Third party resources

## Topics

### Introduction

```python
def filter_some_stuff(that_last_number):
    out = f"{float(that_last_number):,.8f}".rstrip("0")
    return out

def filter_code_thing(code_to_filter):
    start_of_useless_data_size = len("IN-LBF-S")
    end_of_useless_data = 1
    if start_of_useless_data_size + end_of_useless_data >= len(code_to_filter): return ""
    return code_to_filter[start_of_useless_data_size:-1]
    

rows = [
    "1193 OFRGHTK IN-LBF-SSTUFF_THAT_IS_INTERESTING2 0.4899162E-06",
    "1194 TDCHFR 1966.269"
]

for row in rows:
    match row.split():
        case [number_thing, code_thing, other_code_thing, that_last_number]: 
            print("that second condition", end=" ")
            code_thing = filter_code_thing(other_code_thing)
            that_last_number = filter_some_stuff(that_last_number)
            print(code_thing, that_last_number)
        case [number_thing, code_thing, that_last_number]: 
            print("hey it's the first thing")
            that_last_number = filter_some_stuff(that_last_number)
            print(that_last_number)
```

## Practice Questions

## Challenge
