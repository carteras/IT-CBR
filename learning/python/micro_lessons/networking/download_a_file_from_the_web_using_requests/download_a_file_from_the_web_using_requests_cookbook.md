# Requests

## Topics covered

"At the end of this learning brief, you will be able to answer the following questions"

* What is the requests library?
* Will I need to install requests?
* How do I make a simple request?
* Downloading a file with Requests

## Learning Resources

* [Reference Material](https://docs.python-requests.org/en/latest/user/quickstart/)
* [More material](https://www.w3schools.com/python/module_requests.asp)

## Topics

### What is the requests library?

Requests is an elegant and simple HTTP library for Python, built for human beings.

### Will I need to install requests?

Maybe. If the following code doesn't work go to the shell (on the right panel click shell) and type `pip install requests`

### How do I make a simple request?

Making a request with Requests is very simple.

Begin by importing the Requests module:

```python
import requests
```
Now, let’s try to get a webpage. For this example, let’s get GitHub’s public timeline:

```python
import requests
r = requests.get('https://api.github.com/events')
print(r)
print(r.headers['Server'])
```

Now, we have a Response object called r. We can get all the information we need from this object.



### Downloading a file with Requests

```python
url = f'https://raw.github.com/carteras/IT_CBR/master/{file_name}.{extension}'
r = requests.get(url, stream=True)

with open(f'{file_name}.{extension}', 'wb') as file_descriptor:
    for chunk in r.iter_content(128):
        fd.write(chunk)
```

## Practice Questions

### Practice Question 1

...

### Practice Question 2

...

## Mastery Questions

### Mastery Question 1

...

### Mastery Question 2

...

### Mastery Question 3

...
