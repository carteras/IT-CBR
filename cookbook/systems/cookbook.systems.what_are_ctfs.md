# How does something work? 

## Learning Goals

*By the end of this recipe you should be able to answer the following:*

* What is a "CTF"?
* Where do CTFs come from?
* What do CTFs look like here?

## Concepts

Capture The Flag (CTF) competitions were first used by computer security experts who wanted to test each other's skills. They created challenges and solved them in fun contests. Later, CTFs became popular at a hacking conference called DefCon. Today, CTFs are used by people who want to learn about cybersecurity and compete with others in a challenging and enjoyable way. Companies and governments also use CTFs to find talented cybersecurity professionals. Many people think that CTFs are important for learning about cybersecurity.

## Examples

Capture The Flag (CTF) is a type of computer security game that teaches people about cybersecurity in a fun way. In CTFs, players try to find hidden "flags" or clues by solving puzzles and answering questions related to computer security. Here are some examples of simple CTF questions using Python code and operating system commands:

Python Code: Let's imagine we're playing a CTF where we've been told that the password is very common. We're given the following Python code and asked to find the correct password:

```python
common_passwords = ['123456', ... , 'freepass']

def find_secret_password(secret_file):
    with open(secret_file, 'w') as secret_passwords:
        for secret in secret_passwords:
            if secret in common_passwords:
                return secret
    return None

if (passphrase := find_secret_password("secrets")):
    print("cbrcCTF{"+passphrase+"}")
else:
    print("There were no common passwords")
```

Operating System Commands: Let's imagine we're playing a CTF where we need to find a hidden file on a computer. We're given the following command prompt and asked to find the hidden file:

```shell
$ ls -a
file1.txt file2.txt .hiddenfile
```

## Practice Question

From the linked file [words](files/words) the flag is the only word which meets the following conditions:

* Is an isogram
* Is in the list more than once