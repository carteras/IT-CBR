# Hashlib

## Topics covered

"At the end of this learning brief, you will be able to answer the following questions"

* What are hashs?
* How do we roll our own hashing function?

## Learning Resources

* [Python docs: hashlib](https://docs.python.org/3/library/hashlib.html)

## Topics

### What is a hash?

Hashing is the transformation of a string of characters into a usually shorter fixed-length value or key that represents the original string. Hashing is used to index and retrieve items in a database because it is faster to find the item using the shorter hashed key than to find it using the original value.

### Creating a simple md5 digest.

We are going to be playing with the hash function md5. Md5 is not a secure hash anymore, but we are using it because it is small.

```python
from haslib import md5

def make_md5(phrase_to_hash):
  phrase_to_hash = phrase_to_hash.encode('utf-8')
  m = mdf(phrase_to_hash)
  return m.hexdigest()

passphrase = "password"
print(passphrase, make_md5(passphrase)
```
