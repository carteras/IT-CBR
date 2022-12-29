# Challenge 3

You have been hired to create an authentication system for a gate. users must enter their username and password. 

Using the following code blocks as a starting point create a program that does the following

* checks to see if the the user has entered the correct password
* using a dictionary, create a lookup list that checks known hashed passwords to common passwords
* If a user's password belongs to the top [1000 common passwords](https://github.com/DavidWittman/wpxmlrpcbrute/blob/master/wordlists/1000-most-common-passwords.txt) push a messaging asking the user to change their password
* Create a user interaction that allows them to change their password


```python
users = {
    'ada_lovelace': "e10adc3949ba59abbe56e057f20f883e",
    'bob_kahn': "25f9e794323b453885f5181f1b624d0b",
    'charles_babbage': "827ccb0eea8a706c4c34a16891f84e7b",
    'elizabeth_feinler': 'd8578edf8458ce06fbc5bb76a58c5ca4',
    'frances_allen': '5f4dcc3b5aa765d61d8327deb882cf99'
}
```

```python
from hashlib import md5

passwords = ['123456', '123456789', '12345', 'qwerty', 'password', '12345678', 'correct_horse_battery_staple']


for word in passwords:
    print(md5(word.encode()).hexdigest())
```

## Spicyness! 

* Create a program that can download the common password lists dynamically
* Create a greater range of options that allows users to do things:
  * auth:username:password -> authenticates them to the system
  * check:password -> returns "Good" if the password is not on the most common list and "Weak" if the password is known
  * crack:hashedpassword -> returns cleartext password if a user enters a known hashed password e.g., e10adc3949ba59abbe56e057f20f883e would return 123456