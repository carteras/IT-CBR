
# Email




## lab

Set up the following network: 

![](imgs/2023-07-24-13-48-21.png)

DHCP: 

![](imgs/2023-07-24-13-51-15.png)

DNS

![](imgs/2023-07-24-13-52-55.png)


FTP

![](imgs/2023-07-24-13-53-34.png)


Checking out what's in our directory on PC0

![](imgs/2023-07-25-08-44-35.png)

Connecting to FTP

![](imgs/2023-07-25-08-46-57.png)

Getting a list of commands: 

![](imgs/2023-07-25-08-47-24.png)

Let's try dir for directory

![](imgs/2023-07-25-08-47-55.png)

File 29, ir800_yocto-1.7.2.tar looks like a good candidate to download because it's only 2.8 meg. 

Let's `get` it. 

![](imgs/2023-07-25-08-48-43.png)

It's going to take a while. I guess it thinks we're on dial up ;)

![](imgs/2023-07-25-08-49-12.png)

Let's disconnect from the server with `quit`. 

Let's check the local directory of PC0

![](imgs/2023-07-25-08-49-51.png)

Two things stand out to me: 

* The file we downloaded is there and it looks complete. 
* There is another file there! 

Let's upload it!

![](imgs/2023-07-25-08-50-49.png)

To upload it, we need to use the `put` command. 

So let's do that. Type 

`put sampleFile.txt` in there and see what happens....


Oh oh ... 

![](imgs/2023-07-25-08-51-56.png)

What went wrong? 

```bash
%Error ftp://ftp.cbrc.com/sampleFile.txt (No such file or directory Or Permission denied)
550-Requested action not taken. permission denied).
```

Why is that? It's because we didn't set up foo with permissions to upload/write. 

![](imgs/2023-07-25-08-53-00.png)

See how the `foo` user only has the `RL` permissions? That means all they can do is `READ` and `LIST`. We have two choices, we can use the cisco:cisco account or we can modify foo:foo to have more permissions. Let's do the latter

![](imgs/2023-07-25-08-54-40.png)

Now try again: 

![](imgs/2023-07-25-08-55-12.png)