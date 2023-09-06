# Routers and VLANS

## Learning intentions and selection criterion

### Learning intentions

*What are we learning in this brief?*

Sometimes we want to subdivide parts of the network on a single router. Considering the limited number of ports available on routers (not to mention their cost), how can we manage that?

### Selection criterion

*I will know I have learned this when I can:"

* I will be able to configure multiple VLANs on a single switch
* I will know the difference between switchmode access and trunk
* I will be able to set up dot1q encapsulation on a given trunk port
* I will be able to use the different VLANs to allocate DHCP via the routers

## Topic | Commands | Code

*It is important to practice commands | code and challenge our brain in new ways. Do all of the problems below, including the example problems. They will make you a better programmer | operator.*


Consider the following network: 

![](img/20230815210648.png)

I've nominated four subnets that we can use for this network. We're going to use 3 of them for this task. 

| Network Address | Usable Host Range           | Broadcast Address: |     |
| --------------- | --------------------------- | ------------------ | --- |
| 10.13.37.0      | 10.13.37.1 - 10.13.37.62    | 10.13.37.63        |10.13.37.0/26|
| 10.13.37.64     | 10.13.37.65 - 10.13.37.126  | 10.13.37.127       |10.13.37.64/26|
| 10.13.37.128    | 10.13.37.129 - 10.13.37.190 | 10.13.37.191       |10.13.37.128/26|
| 10.13.37.192    | 10.13.37.193 - 10.13.37.254 | 10.13.37.255       |10.13.37.192/26|

VLAN 10 and 20 are going to use the 10.13.37.0/26 and 10.13.37.64/26 networks respectively. The server group is going to use 10.13.37.128/26 network. That leaves the 10.13.37.192/26 network spare. 

Let's configure the two VLANs. 

```cmd
Switch>enable
Switch#configure terminal
Switch(config)#vlan 10
Switch(config-vlan)# name TOP_NETWORK
Switch(config-vlan)# vlan 20
Switch(config-vlan)# name BOTTOM_NETWORK
Switch(config-vlan)#end
```

```cmd
Switch#config terminal

Switch(config)#int fa0/1
Switch(config-if)#switchport mode access
Switch(config-if)#switchport access vlan 10

Switch(config-if)#int fa0/2
Switch(config-if)#switchport mode access
Switch(config-if)#switchport access vlan 10

Switch(config-if)#int fa0/3
Switch(config-if)#switchport mode access
Switch(config-if)#switchport access vlan 20

Switch(config-if)#int fa0/4
Switch(config-if)#switchport mode access
Switch(config-if)#switchport access vlan 20
```

Note: we could have configured the above interfaces as access ports using `interface range`

```cmd
Switch(config-if)#int range fa0/1-4
Switch(config-if-range)#switchport mode access
```

Let's configure that outbound connection from the switch to the router so it handles multiple VLANs. We'll set it up for trunk access. 

```cmd
Switch> enable
Switch#Configure Terminal
Switch(config)# interface f0/5
Switch(config-if)#switchport mode trunk
```

Done!

Now, let's configure the router. 

```cmd
Router#enable
Router#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)#int g0/0/0
Router(config-if)#no shutdown
Router(config-if)#int g0/0/0.10
```

It looks all good until that g0/0/0.10, what's the deal with that? 

I'm basically telling the router that I am going to encapsulate multiple VLANs over the same ethernet port. 

```cmd
Router(config-subif)#encapsulation dot1q 10
Router(config-subif)#ip add 10.13.37.1 255.255.255.192
Router(config-subif)#int g0/0/0.20
Router(config-subif)#encapsulation dot1q 20
Router(config-subif)#ip add 10.13.37.65 255.255.255.192
Router(config-subif)#exit
```

Here I've arranged both vlans to come through. Encapsulation dot1Q on specifies the use of [IEEE 802.1Q VLAN tagging](https://en.wikipedia.org/wiki/IEEE_802.1Q) on an interface, allowing multiple VLANs on a single link. Essential for trunk connections.

```cmd
Router(config)#ip dhcp pool TOP_NETWORK
Router(dhcp-config)#network 10.13.37.0 255.255.255.192
Router(dhcp-config)#default-router 10.13.37.1
Router(dhcp-config)#dns-server 10.13.37.130
Router(dhcp-config)#ip dhcp pool BOTTOM_NETWORK
Router(dhcp-config)#network 10.13.37.65 255.255.255.192
Router(dhcp-config)#default-router 10.13.37.65
Router(dhcp-config)#dns-server 10.13.37.130
Router(dhcp-config)#end
```

I've configured both dhcp pool to for this router. How does the router know which pool to use? Because the network knows which VLAN the packets are coming from and we've told the router than VLAN 10 is from 10.13.37.0/26 and VLAN 20 is from 10.13.37.64/26 the router can allocate the correct information to the computers coming from those VLANs

```cmd
Router#
Router(config)#interface g0/0/1
Router(config-if)#ip address 10.13.37.129 255.255.255.192
Router(config-if)#no shutdown
Router(config-if)#end
Router#show ip int
Router#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol 
GigabitEthernet0/0/0   unassigned      YES unset  up                    up 
GigabitEthernet0/0/0.1010.13.37.1      YES manual up                    up 
GigabitEthernet0/0/0.2010.13.37.65     YES manual up                    up 
GigabitEthernet0/0/1   10.13.37.129    YES manual up                    up 
GigabitEthernet0/0/1.10unassigned      YES unset  up                    up 
GigabitEthernet0/0/2   unassigned      YES unset  administratively down down 
Vlan1                  unassigned      YES unset  administratively down down
```


Hey, that's looking pretty good. Let's go do some testing: Let's start with PC0

```cmd
C:\>ipconfig

FastEthernet0 Connection:(default port)

   Connection-specific DNS Suffix..: 
   Link-local IPv6 Address.........: FE80::20C:85FF:FEA1:66A3
   IPv6 Address....................: ::
   IPv4 Address....................: 10.13.37.2
   Subnet Mask.....................: 255.255.255.192
   Default Gateway.................: ::
                                     10.13.37.1
```

10.13.37.2 that's a viable IP address for this subnet. 

255.255.255.192 that's a /26 range 

10.13.37.1 is in fact the gateway address.

All good! Let's do a reality check and ping ourselves. 

```cmd
C:\>ping 10.13.37.2

Pinging 10.13.37.2 with 32 bytes of data:

Reply from 10.13.37.2: bytes=32 time=4ms TTL=128
Reply from 10.13.37.2: bytes=32 time=2ms TTL=128
Reply from 10.13.37.2: bytes=32 time=2ms TTL=128
Reply from 10.13.37.2: bytes=32 time=4ms TTL=128
```

Looks good. 

Let's ping the gateway. 

```cmd
C:\>ping 10.13.37.1

Pinging 10.13.37.1 with 32 bytes of data:

Reply from 10.13.37.1: bytes=32 time<1ms TTL=255
Reply from 10.13.37.1: bytes=32 time<1ms TTL=255
Reply from 10.13.37.1: bytes=32 time<1ms TTL=255
Reply from 10.13.37.1: bytes=32 time<1ms TTL=255

Ping statistics for 10.13.37.1:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms
```

Looks good. 

I'm going to make an assumption that the first DHCP address has been allocated on VLAN 20, let's ping it. 

```cmd
C:\>ping 10.13.37.65

Pinging 10.13.37.65 with 32 bytes of data:

Reply from 10.13.37.65: bytes=32 time<1ms TTL=255
Reply from 10.13.37.65: bytes=32 time<1ms TTL=255
Reply from 10.13.37.65: bytes=32 time<1ms TTL=255
Reply from 10.13.37.65: bytes=32 time<1ms TTL=255
```

Looking good.

Let's ping our "server"

```cmd

C:\>ping 10.13.37.130

Pinging 10.13.37.130 with 32 bytes of data:

Reply from 10.13.37.130: bytes=32 time=8ms TTL=127
Reply from 10.13.37.130: bytes=32 time<1ms TTL=127
Reply from 10.13.37.130: bytes=32 time<1ms TTL=127
Reply from 10.13.37.130: bytes=32 time<1ms TTL=127
```

Amazing!

## Fluff about find out

So, you've learnt lots of things so far today. I challenge you to use your imagination and try and find some things that you feel you might be able to do, but weren't necessarily taught.

For our ad hoc challenge, create a third VLAN (VLAN 30) using the remaining IP range. 
