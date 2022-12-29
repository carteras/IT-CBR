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

To download a file we need to know it's full address where the file is saved. In our case, it is stored on github but it's stored in a special place. If you go to github and look at the file `https://github.com/carteras/IT-CBR/blob/main/learning/python/micro_lessons/exceptions/alice.txt` you'll see that the file is framed with webpage content. We don't want that extra content, just the real content. 

So, we click the `raw` button. Tada!

```python
url = f'https://raw.githubusercontent.com/carteras/IT-CBR/main/learning/python/micro_lessons/exceptions/alice.txt'
```

Because files can be long, we don't want to download all of it in one chunk. So, we'll use a technology that you are all aware off, streaming. To do this we simply turn it on: 

```python
r = requests.get(url, stream=True)
```

Next we want to treat the download much like a file but with some special qualifiers: 

```python
with open(f'alice.txt', 'wb') as file_descriptor
```

`wb` means write bytes. Because we are downloading a file, we'll keep it as a file and if we need to do something with it (like turn it into text) we can do that later.

Next, because we are streaming the file, we need to tell python how many bytes we are going to stream in each loop. We do this with the rather long keyword `iter_content(128)`. iter_content means iterate through content and the 128 is the number of bytes it consumes per loop. 

```python
for chunk in r.iter_content(128):
    fd.write(chunk)
```

All together!

```python
url = f'https://raw.githubusercontent.com/carteras/IT-CBR/main/learning/python/micro_lessons/exceptions/alice.txt'
r = requests.get(url, stream=True)

with open(f'alice.txt', 'wb') as file_descriptor:
    for chunk in r.iter_content(128):
        fd.write(chunk)
```

## Practice Questions

### Practice Question 1: 

Create a program that downloads the alice.txt file and count how many words are in the entire text.

### Practice Question 2:

Create a program that downloads the thegreenknight.txt and count how many words are in in the entire text.

## Mastery Questions

### Mastery Question 1

Create a program that downloads 51tales.txt and counts the following: 

* How many lines are in the file
* How many words are in each line
* How many words are in the whole document