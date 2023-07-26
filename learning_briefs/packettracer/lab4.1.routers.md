# Configuring SSH

## Topics

### Terminology 

General Terms: 

* CLI - Command line interface
* SSH - Secure Shell : A network protocol that gives uses a secure way to communicate over a network
* The VTY lines are the Virtual Terminal lines of the router, used solely to control inbound Telnet connections. They are virtual, in the sense that they are a function of software - there is no hardware associated with them. 

Device Modes:

* User EXEC Device>
* Privileged EXEC Device#
* Global Config Device­(co­nfig)#
* Interface Config Device­(co­nfi­g-if)#
* Line Config Device­(co­nfi­g-line)

Handy Keyboard Shortcuts

* Up Arrow Automatically re-types last command
* Ctrl+Shift+6 Oh crap, stop! (Cancels whatever it's currently doing)
* Ctrl+C Exits config mode
* Ctrl+Z Applies current command & returns to priv. EXEC mode 
* Ctrl+U Erases anything on current prompt line
* Tab Completes abbreviated command

Show Commands

* show ip interface brief name, IP, status, etc. (all interf­aces)


General Commands 

* en enable user EXEC > priv. EXEC
* conf t config terminal priv. EXEC > global config
* int inter­face global config > interface config

Router Configuration 

* hostname xyz sets hostname to xyz
* line vty 0 15 - enters line config mode for 16 virtual terminal lines 
* ip address [ip] [subnet] - sets an IP address
* no shut - turns on interface

### Lab1 - SSH between two routers

Put two routers onto the deck. It shouldn't matter which kind of routers you pick but I chose 1941

![](imgs/2021-08-01-11-33-30.png)

Open both views so they are side by side. 

![](imgs/2021-08-01-11-33-58.png)

Open the CLI mode for Router 1. We will be using CLI to configure everything. 

When you open the CLI mode you will see the router booting. It will end with the following statement. 

`Would you like to enter the initial configuration dialog? [yes/no]:`

Say no

By default we start in User EXEC mode. We want to move our permissions to Privileged EXEC mode. We can do this by typing `enable`


![](imgs/2021-08-01-11-35-19.png)

Then, we want enter into configuration mode we can type `config terminal` to enter Global Config mode. We will know that we are in config mode because the interface will start with a `#` instead of a `>`

![](imgs/2021-08-01-11-37-51.png)

We want to change the hostname from Router 0 to R0. To change the hostname we can do it by typing `hostname R0`

end configuration by typing `end`

### Configuring the link

The next thing we want to do is get our router ready to to work on the network. Let's see if our connections are up or down. 

`show ip interface brief`

Shows all the internet protocol interfaces in a brief format. 

![](imgs/2021-08-01-11-40-04.png)

Here we can see that all of our interfaces are down. 

We want to turn the interface that we have plugged in on. 

Go back into config mode with `config terminal`

Now, let's choose an interface. I am going to choose the gigabyte connection 0/0. To do this, I type `interface g0/0`

![](imgs/2021-08-01-11-41-57.png)

Notice how our terminal window is now headed with `R0(config-if)#`? That's how you know you are configuring an interface. 

Let's pick an IP address. 

I am going to type   
`ip address 192.168.1.1 255.255.255.0`

Now, I will bring the link up

`no shutdown`

Cisco should tell you that the Interface for g0/0 has changed stated to up. 

![](imgs/2021-08-01-11-43-35.png)

### The second router! 

Do the same as above, but for Router 1. Change it's name to R1. R1 will have an IP number of 192.168.1.2 and a subnet of 255.255.255.0


### Testing the connection

Once both machines are configured. Pick one and end out of `config-if` and `config`. To This will leave you in enable mode. You should be left with `R0#` (or `R1#`)

Let's see if we have configured the machines appropriately. We can do this by pinging the other machine. Because I am on R0, I will need to ping the address of R1 

`ping 192.168.1.2` 

If it works you should see something like this: 

`Sending 5, 100-byte ICMP Echos to 192.168.1.2, timeout is 2 seconds: .!!!!`

`Success rate is 80 percent (4/5), round-trip min/avg/max = 0/0/0 ms`

The first packet was dropped as the new address was unknown to it. Try it again.

## Challenge

Remake the same network but using the following details: 

```
Router0 

* name change to Lab1
* g0/0 ip 10.13.37.1 255.255.255.0

Router1

* name change to Lab2
* g0/0 ip 10.13.37.2 255.255.255.0
```

