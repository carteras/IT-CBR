# What is a challenge and what do you need to do

## Think about your problem

If it is a bushranger-type problem log into Bushranger (or if you are at home, bandit at overthewire) log into the directory and type `ls -la` 

Go through the process of solving that Bushranger a few times and write down each step that you have to do. For example, in bushranger4 the process is basically this: 

ssh bushranger4@10.13.37.152 -p 22
enter password
type ls -la to see what is in the directory
cd inhere to change directory into the inhere directory
ls -la 
file ./-* | file ./-file* | file ./-file0? to scan through all of the file types 
cat ./-file07
capture flag

`ls -la` will list the contents of the directory and show all of the hidden files and the permissions of each file.

Identify the username and group name for all of the files. Evalute if that's correct. For example, in bushranger4 the group for all of the files is users. Is that right? Should it be bushranger4? 

Check the permissions of the files. Actually, how do permissions work in linux? Here's the cheatsheet: https://chmodcommand.com/  

But in essence, it looks like this:

\- | --- | --- | ---

* The first column designates it as a directory
* The second column says if the user can read, write, or execute 
* The third column says if people in the group can read, write, or execute
* The fourth column says if any user can read, write, or execute 

So, for example: 

dr-xr-xr-x 2 bushranger4 bushranger4 4096 Apr 22 12:48 .

d | r-x | r-x | r-x 

It's a directory (the self/this directory actually)
User Bushranger4 can read and execute 
Users in Bushragner4 can read and execute 
Any user can read and execute 
-r--r----- 1 bushranger4 users        34 Apr 22 12:48 -file07

\- | r-- | r-- | --- 

* -file07 is not a directory
* user bushranger4 c and read the file 
* all users in the user group can read the file (do we want this feature?)
* Users who aren't bushranger4 or in the user group can not read this file. 

## Think about your challenge: 

* In 50 words, what does your challenge do that Bushranger doesn't?
* Write down all of the steps that you feel the user needs to complete
* Write down any additional files that you think you might need. For example, in bushranger4, I needed to generate a bunch of other files. 
* Think about red herrings (which I didn't do for my examples). If you need people to do 4 qualifiers, there should be red herrings to make it a requirement. 
* Where do you think you need to write stuff? How do you make it tricky but not impossible?
* Write down all of the permissions that you think you will need  

