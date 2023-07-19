# DHCP 

## Objective: 
Learn how DHCP servers allocate IP information. 

The vast majority of IP networks use DHCP to allocate IP information to hosts. Here we’ll configure a scope of addresses and other IP information to be allocated. 


## Topics

### DHCP 

Dynamic Host Configuration Protocol (DHCP) is a network management protocol used to automate the process of configuring devices on IP networks, thus allowing them to use network services such as DNS, NTP, and any communication protocol based on UDP or TCP. A DHCP server dynamically assigns an IP address and other network configuration parameters to each device on a network so they can communicate with other IP networks.

## Lab Topology: 

Please use the following topology to complete this lab exercise:

![](imgs/2021-08-06-08-24-03.png)

Switch: 2960x1
PCx2
Serverx1

## Tutorial

### Step 1
Connect a generic server to a Cisco switch using straight-through cables. You will add an IP address to the server but not to the host PCs, which will be using DHCP.

Server
IP: 192.168.1.1.
Subnet: 255.255.255.0


### Step 2
Configure the DHCP information on the server. Allocate the following: Address start—192.168.1.2 Subnet mask—255.255.255.0 Pool name—101Pool

Pool Name: cbrPool (or anything)
Start IP Address: 192.168.1.2
Subnet Mask: 255.255.255.0

Add (and check it is turned on ;p)
![](imgs/2021-08-06-08-27-13.png)



### Step 4

Configure the hosts to obtain information via DHCP. 

Click on the PC client and open the desktop
![](imgs/2021-08-06-08-29-03.png)


Switch DHCP on
![](imgs/2021-08-06-08-29-30.png)



### Step 4

Check the configuration has been applied by issuing the ‘ipconfig’ command on the hosts. 

Go do desktop and cmd window

![](imgs/2021-08-06-08-35-22.png)

type ipconfig

![](imgs/2021-08-06-08-35-43.png)

You can also ping the server from here

![](imgs/2021-08-06-08-36-34.png)

 If you hover your mouse over the image of any device in Packet Tracer, you will also see the IP configuration settings.

 ![](imgs/2021-08-06-08-36-55.png)

## Practice:

Finalise the configuration of PC 2



