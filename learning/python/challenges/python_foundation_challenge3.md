# Challenge 3: Python Programming

## Required masteries/learning

It is expected that you have completed all elements before moving onto the warm up and the challenge.

* [Python Dictionaries](../micro_lessons/data_structures/dictionaries/dictionaries_cookbook.md)
* [Hashlib](../micro_lessons/hashing_and_encryption/hashlib/hashlib_cookbook.md)
* [datetime](../micro_lessons/python_modules/datetime/datetime_cookbook.md)
* [joining lists of characters into strings](../micro_lessons/python_modules/joining_strings/joining_strings_cookbook.md)
* [itertools](../micro_lessons/python_modules/itertools/itertools_cookbook.md)

## Challenges Questions

NOTE: At the bottom of this document is a list of common passwords that you should use. This list of words is uncensored to keep it's accuracy. 

### Brute force PIN numbers (warm up)

Using the following code as a template, crack 100 very large security numbers. 

* Numbers can be anything from 000000 to 999999
* You need to work in the brute force function
* DON'T DELETE STUFF! Just ignore the parts where I am being too clever

You will need itertools. I've handled the time measuring for you. 

```python

def delta_time(f):
    import time
    def aux(*args, **kwargs):
        start_time = time.process_time()
        out = f(*args, **kwargs)
        end_time = time.process_time()
        print(f"{f.__name__} took {end_time - start_time} seconds: ".ljust(35), end="")
        return out
    return aux

@delta_time
def brute_force(secret_pin):
    # EDIT THIS FUNCTION!!!!
    # If you make this function do something
    # you can delete the pass 
    pass

@delta_time      
def brute_force_100_pins():
    for i in range(100):
        secret_pin = f"{randint(0, 1000000)}".zfill(6)
        print(brute_force(secret_pin))

if __name__ == "__main__":
    brute_force_100_pins()
```

Your output should look and end a bit like this: 

```text
brute_force took 0.046875 seconds: 519947
brute_force took 0.0625 seconds:   558706
brute_force took 0.03125 seconds:  375091
brute_force took 0.078125 seconds: 642624
brute_force_100_pins took 6.328125 seconds:
```


### Brute force passwords (warm up)

* Loop through the list of passwords below. 
* Save all of the passwords that have the `len(word)` of 4 or less. 
* Pick one at random
* Create a solution that brute forces all possible combinations of passwords until you find the correct one
* measure how long it takes to find solutions this way. 
* create a loop to do this with 100 random words
 * measure the average time to crack each password

note: itertools is a great help

### Create a hashed dictionary attack

You've found a list of passwords but they've been hashed in md5. Create a solution that finds each of these hashed passwords. 

```python
password_table = ['fd820a2b4461bddd116c1518bc4b0f77', 'faf2ca38c02c5f2ba1c49d200a03f9fb', '823fec7a2632ea7b498c1d0d11c11377', '4badaee57fed5610012a296273158f5f', 'dc599a9972fde3045dab59dbd1ae170b', '5f0cbc3f99acb914d429cfdf23dd75e3', '63188b0436e754a4d9a1d89dfc978209', '5583413443164b56500def9a533c7c70', 'fe01d67a002dfa0f3ac084298142eccd', 'b1f4f9a523e36fd969f4573e25af4540']

```

### Top 1,000 passwords

This is a real list of the top 1,000 passwords. If your password is on here, you should change it! 

NOTE: DO NOT SCROLL RIGHT UNTIL YOU READ THIS!

This is a real, uncensored, list of passwords. There naughty words on here (some are very naughty). I present it in full for two reasons: 

1. This is an actual list of known, common, passwords that have been discovered by hackers (black hats) and sold on the darknet. These passwords have since been captured by people who work in digital security (white hats). 
2. I feel that editing or censoring this list creates a dishonest atmosphere of what the world looks like.

If this presents a major problem to you please speak up and we can see if we can find a different solution.

```python
passwords = ['123456', 'password', '12345678', 'qwerty', '123456789', '12345', '1234', '111111', '1234567', 'dragon', '123123', 'baseball', 'abc123', 'football', 'monkey', 'letmein', '696969', 'shadow', 'master', '666666', 'qwertyuiop', '123321', 'mustang', '1234567890', 'michael', '654321', 'pussy', 'superman', '1qaz2wsx', '7777777', 'fuckyou', '121212', '000000', 'qazwsx', '123qwe', 'killer', 'trustno1', 'jordan', 'jennifer', 'zxcvbnm', 'asdfgh', 'hunter', 'buster', 'soccer', 'harley', 'batman', 'andrew', 'tigger', 'sunshine', 'iloveyou', 'fuckme', '2000', 'charlie', 'robert', 'thomas', 'hockey', 'ranger', 'daniel', 'starwars', 'klaster', '112233', 'george', 'asshole', 'computer', 'michelle', 'jessica', 'pepper', '1111', 'zxcvbn', '555555', '11111111', '131313', 'freedom', '777777', 'pass', 'fuck', 'maggie', '159753', 'aaaaaa', 'ginger', 'princess', 'joshua', 'cheese', 'amanda', 'summer', 'love', 'ashley', '6969', 'nicole', 'chelsea', 'biteme', 'matthew', 'access', 'yankees', '987654321', 'dallas', 'austin', 'thunder', 'taylor', 'matrix', 'william', 'corvette', 'hello', 'martin', 'heather', 'secret', 'fucker', 'merlin', 'diamond', '1234qwer', 'gfhjkm', 'hammer', 'silver', '222222', '88888888', 'anthony', 'justin', 'test', 'bailey', 'q1w2e3r4t5', 'patrick', 'internet', 'scooter', 'orange', '11111', 'golfer', 'cookie', 'richard', 'samantha', 'bigdog', 'guitar', 'jackson', 'whatever', 'mickey', 'chicken', 'sparky', 'snoopy', 'maverick', 'phoenix', 'camaro', 'sexy', 'peanut', 'morgan', 'welcome', 'falcon', 'cowboy', 'ferrari', 'samsung', 'andrea', 'smokey', 'steelers', 'joseph', 'mercedes', 'dakota', 'arsenal', 'eagles', 'melissa', 'boomer', 'booboo', 'spider', 'nascar', 'monster', 'tigers', 'yellow', 'xxxxxx', '123123123', 'gateway', 'marina', 'diablo', 'bulldog', 'qwer1234', 'compaq', 'purple', 'hardcore', 'banana', 'junior', 'hannah', '123654', 'porsche', 'lakers', 'iceman', 'money', 'cowboys', '987654', 'london', 'tennis', '999999', 'ncc1701', 'coffee', 'scooby', '0000', 'miller', 'boston', 'q1w2e3r4', 'fuckoff', 'brandon', 'yamaha', 'chester', 'mother', 'forever', 'johnny', 'edward', '333333', 'oliver', 'redsox', 'player', 'nikita', 'knight', 'fender', 'barney', 'midnight', 'please', 'brandy', 'chicago', 'badboy', 'iwantu', 'slayer', 'rangers', 'charles', 'angel', 'flower', 'bigdaddy', 'rabbit', 'wizard', 'bigdick', 'jasper', 'enter', 'rachel', 'chris', 'steven', 'winner', 'adidas', 'victoria', 'natasha', '1q2w3e4r', 'jasmine', 'winter', 'prince', 'panties', 'marine', 'ghbdtn', 'fishing', 'cocacola', 'casper', 'james', '232323', 'raiders', '888888', 'marlboro', 'gandalf', 'asdfasdf', 'crystal', '87654321', '12344321', 'sexsex', 'golden', 'blowme', 'bigtits', '8675309', 'panther', 'lauren', 'angela', 'bitch', 'spanky', 'thx1138', 'angels', 'madison', 'winston', 'shannon', 'mike', 'toyota', 'blowjob', 'jordan23', 'canada', 'sophie', 'Password', 'apples', 'dick', 'tiger', 'razz', '123abc', 'pokemon', 'qazxsw', '55555', 'qwaszx', 'muffin', 'johnson', 'murphy', 'cooper', 'jonathan', 'liverpoo', 'david', 'danielle', '159357', 'jackie', '1990', '123456a', '789456', 'turtle', 'horny', 'abcd1234', 'scorpion', 'qazwsxedc', '101010', 'butter', 'carlos', 'password1', 'dennis', 'slipknot', 'qwerty123', 'booger', 'asdf', '1991', 'black', 'startrek', '12341234', 'cameron', 'newyork', 'rainbow', 'nathan', 'john', '1992', 'rocket', 'viking', 'redskins', 'butthead', 'asdfghjkl', '1212', 'sierra', 'peaches', 'gemini', 'doctor', 'wilson', 'sandra', 'helpme', 'qwertyui', 'victor', 'florida', 'dolphin', 'pookie', 'captain', 'tucker', 'blue', 'liverpool', 'theman', 'bandit', 'dolphins', 'maddog', 'packers', 'jaguar', 'lovers', 'nicholas', 'united', 'tiffany', 'maxwell', 'zzzzzz', 'nirvana', 'jeremy', 'suckit', 'stupid', 'porn', 'monica', 'elephant', 'giants', 'jackass', 'hotdog', 'rosebud', 'success', 'debbie', 'mountain', '444444', 'xxxxxxxx', 'warrior', '1q2w3e4r5t', 'q1w2e3', '123456q', 'albert', 'metallic', 'lucky', 'azerty', '7777', 'shithead', 'alex', 'bond007', 'alexis', '1111111', 'samson', '5150', 'willie', 'scorpio', 'bonnie', 'gators', 'benjamin', 'voodoo', 'driver', 'dexter', '2112', 'jason', 'calvin', 'freddy', '212121', 'creative', '12345a', 'sydney', 'rush2112', '1989', 'asdfghjk', 'red123', 'bubba', '4815162342', 'passw0rd', 'trouble', 'gunner', 'happy', 'fucking', 'gordon', 'legend', 'jessie', 'stella', 'qwert', 'eminem', 'arthur', 'apple', 'nissan', 'bullshit', 'bear', 'america', '1qazxsw2', 'nothing', 'parker', '4444', 'rebecca', 'qweqwe', 'garfield', '01012011', 'beavis', '69696969', 'jack', 'asdasd', 'december', '2222', '102030', '252525', '11223344', 'magic', 'apollo', 'skippy', '315475', 'girls', 'kitten', 'golf', 'copper', 'braves', 'shelby', 'godzilla', 'beaver', 'fred', 'tomcat', 'august', 'buddy', 'airborne', '1993', '1988', 'lifehack', 'qqqqqq', 'brooklyn', 'animal', 'platinum', 'phantom', 'online', 'xavier', 'darkness', 'blink182', 'power', 'fish', 'green', '789456123', 'voyager', 'police', 'travis', '12qwaszx', 'heaven', 'snowball', 'lover', 'abcdef', '00000', 'pakistan', '007007', 'walter', 'playboy', 'blazer', 'cricket', 'sniper', 'hooters', 'donkey', 'willow', 'loveme', 'saturn', 'therock', 'redwings', 'bigboy', 'pumpkin', 'trinity', 'williams', 'tits', 'nintendo', 'digital', 'destiny', 'topgun', 'runner', 'marvin', 'guinness', 'chance', 'bubbles', 'testing', 'fire', 'november', 'minecraft', 'asdf1234', 'lasvegas', 'sergey', 'broncos', 'cartman', 'private', 'celtic', 'birdie', 'little', 'cassie', 'babygirl', 'donald', 'beatles', '1313', 'dickhead', 'family', '12121212', 'school', 'louise', 'gabriel', 'eclipse', 'fluffy', '147258369', 'lol123', 'explorer', 'beer', 'nelson', 'flyers', 'spencer', 'scott', 'lovely', 'gibson', 'doggie', 'cherry', 'andrey', 'snickers', 'buffalo', 'pantera', 'metallica', 'member', 'carter', 'qwertyu', 'peter', 'alexande', 'steve', 'bronco', 'paradise', 'goober', '5555', 'samuel', 'montana', 'mexico', 'dreams', 'michigan', 'cock', 'carolina', 'yankee', 'friends', 'magnum', 'surfer', 'poopoo', 'maximus', 'genius', 'cool', 'vampire', 'lacrosse', 'asd123', 'aaaa', 'christin', 'kimberly', 'speedy', 'sharon', 'carmen', '111222', 'kristina', 'sammy', 'racing', 'ou812', 'sabrina', 'horses', '0987654321', 'qwerty1', 'pimpin', 'baby', 'stalker', 'enigma', '147147', 'star', 'poohbear', 'boobies', '147258', 'simple', 'bollocks', '12345q', 'marcus', 'brian', '1987', 'qweasdzxc', 'drowssap', 'hahaha', 'caroline', 'barbara', 'dave', 'viper', 'drummer', 'action', 'einstein', 'bitches', 'genesis', 'hello1', 'scotty', 'friend', 'forest', '010203', 'hotrod', 'google', 'vanessa', 'spitfire', 'badger', 'maryjane', 'friday', 'alaska', '1232323q', 'tester', 'jester', 'jake', 'champion', 'billy', '147852', 'rock', 'hawaii', 'badass', 'chevy', '420420', 'walker', 'stephen', 'eagle1', 'bill', '1986', 'october', 'gregory', 'svetlana', 'pamela', '1984', 'music', 'shorty', 'westside', 'stanley', 'diesel', 'courtney', '242424', 'kevin', 'porno', 'hitman', 'boobs', 'mark', '12345qwert', 'reddog', 'frank', 'qwe123', 'popcorn', 'patricia', 'aaaaaaaa', '1969', 'teresa', 'mozart', 'buddha', 'anderson', 'paul', 'melanie', 'abcdefg', 'security', 'lucky1', 'lizard', 'denise', '3333', 'a12345', '123789', 'ruslan', 'stargate', 'simpsons', 'scarface', 'eagle', '123456789a', 'thumper', 'olivia', 'naruto', '1234554321', 'general', 'cherokee', 'a123456', 'vincent', 'Usuckballz1', 'spooky', 'qweasd', 'cumshot', 'free', 'frankie', 'douglas', 'death', '1980', 'loveyou', 'kitty', 'kelly', 'veronica', 'suzuki', 'semperfi', 'penguin', 'mercury', 'liberty', 'spirit', 'scotland', 'natalie', 'marley', 'vikings', 'system', 'sucker', 'king', 'allison', 'marshall', '1979', '098765', 'qwerty12', 'hummer', 'adrian', '1985', 'vfhbyf', 'sandman', 'rocky', 'leslie', 'antonio', '98765432', '4321', 'softball', 'passion', 'mnbvcxz', 'bastard', 'passport', 'horney', 'rascal', 'howard', 'franklin', 'bigred', 'assman', 'alexander', 'homer', 'redrum', 'jupiter', 'claudia', '55555555', '141414', 'zaq12wsx', 'shit', 'patches', 'nigger', 'cunt', 'raider', 'infinity', 'andre', '54321', 'galore', 'college', 'russia', 'kawasaki', 'bishop', '77777777', 'vladimir', 'money1', 'freeuser', 'wildcats', 'francis', 'disney', 'budlight', 'brittany', '1994', '00000000', 'sweet', 'oksana', 'honda', 'domino', 'bulldogs', 'brutus', 'swordfis', 'norman', 'monday', 'jimmy', 'ironman', 'ford', 'fantasy', '9999', '7654321', 'PASSWORD', 'hentai', 'duncan', 'cougar', '1977', 'jeffrey', 'house', 'dancer', 'brooke', 'timothy', 'super', 'marines', 'justice', 'digger', 'connor', 'patriots', 'karina', '202020', 'molly', 'everton', 'tinker', 'alicia', 'rasdzv3', 'poop', 'pearljam', 'stinky', 'naughty', 'colorado', '123123a', 'water', 'test123', 'ncc1701d', 'motorola', 'ireland', 'asdfg', 'slut', 'matt', 'houston', 'boogie', 'zombie', 'accord', 'vision', 'bradley', 'reggie', 'kermit', 'froggy', 'ducati', 'avalon', '6666', '9379992', 'sarah', 'saints', 'logitech', 'chopper', '852456', 'simpson', 'madonna', 'juventus', 'claire', '159951', 'zachary', 'yfnfif', 'wolverin', 'warcraft', 'hello123', 'extreme', 'penis', 'peekaboo', 'fireman', 'eugene', 'brenda', '123654789', 'russell', 'panthers', 'georgia', 'smith', 'skyline', 'jesus', 'elizabet', 'spiderma', 'smooth', 'pirate', 'empire', 'bullet', '8888', 'virginia', 'valentin', 'psycho', 'predator', 'arizona', '134679', 'mitchell', 'alyssa', 'vegeta', 'titanic', 'christ', 'goblue', 'fylhtq', 'wolf', 'mmmmmm', 'kirill', 'indian', 'hiphop', 'baxter', 'awesome', 'people', 'danger', 'roland', 'mookie', '741852963', '1111111111', 'dreamer', 'bambam', 'arnold', '1981', 'skipper', 'serega', 'rolltide', 'elvis', 'changeme', 'simon', '1q2w3e', 'lovelove', 'fktrcfylh', 'denver', 'tommy', 'mine', 'loverboy', 'hobbes', 'happy1', 'alison', 'nemesis', 'chevelle', 'cardinal', 'burton', 'wanker', 'picard', '151515', 'tweety', 'michael1', '147852369', '12312', 'xxxx', 'windows', 'turkey', '456789', '1974', 'vfrcbv', 'sublime', '1975', 'galina', 'bobby', 'newport', 'manutd', 'daddy', 'american', 'alexandr', '1966', 'victory', 'rooster', 'qqq111', 'madmax', 'electric', 'bigcock', 'a1b2c3', 'wolfpack', 'spring', 'phpbb', 'lalala', 'suckme', 'spiderman', 'eric', 'darkside', 'classic', 'raptor', '123456789q', 'hendrix', '1982', 'wombat', 'avatar', 'alpha', 'zxc123', 'crazy', 'hard', 'england', 'brazil', '1978', '01011980', 'wildcat', 'polina', 'freepass']
```

