# How do I enable Traceroute in Azure VM?

[Harry Davis](https://quick-adviser.com/author/gxtraiurigl987utifffuf8t/)[22.09.2021](https://quick-adviser.com/how-do-i-enable-traceroute-in-azure-vm/)

Table of Contents

* [How do I enable Traceroute in Azure VM?](https://quick-adviser.com/how-do-i-enable-traceroute-in-azure-vm/#How_do_I_enable_Traceroute_in_Azure_VM "How do I enable Traceroute in Azure VM?")
* [Does Traceroute work in Azure?](https://quick-adviser.com/how-do-i-enable-traceroute-in-azure-vm/#Does_Traceroute_work_in_Azure "Does Traceroute work in Azure?")
* [How do I do a traceroute on Linux?](https://quick-adviser.com/how-do-i-enable-traceroute-in-azure-vm/#How_do_I_do_a_traceroute_on_Linux "How do I do a traceroute on Linux?")
* [Can you ping an Azure VM?](https://quick-adviser.com/how-do-i-enable-traceroute-in-azure-vm/#Can_you_ping_an_Azure_VM "Can you ping an Azure VM?")
* [Can we ping Azure load balancer?](https://quick-adviser.com/how-do-i-enable-traceroute-in-azure-vm/#Can_we_ping_Azure_load_balancer "Can we ping Azure load balancer?")
* [What is TCP ping?](https://quick-adviser.com/how-do-i-enable-traceroute-in-azure-vm/#What_is_TCP_ping "What is TCP ping?")
* [Can I ping load balancer IP?](https://quick-adviser.com/how-do-i-enable-traceroute-in-azure-vm/#Can_I_ping_load_balancer_IP "Can I ping load balancer IP?")
* [How does the Azure load balancer know which back end VMs are unresponsive?](https://quick-adviser.com/how-do-i-enable-traceroute-in-azure-vm/#How_does_the_Azure_load_balancer_know_which_back_end_VMs_are_unresponsive "How does the Azure load balancer know which back end VMs are unresponsive?")
* [What is azure standard load balancer?](https://quick-adviser.com/how-do-i-enable-traceroute-in-azure-vm/#What_is_azure_standard_load_balancer "What is azure standard load balancer?")
* [How does load balancer work in Azure?](https://quick-adviser.com/how-do-i-enable-traceroute-in-azure-vm/#How_does_load_balancer_work_in_Azure "How does load balancer work in Azure?")
* [What is SKU IP address?](https://quick-adviser.com/how-do-i-enable-traceroute-in-azure-vm/#What_is_SKU_IP_address "What is SKU IP address?")
* [What is my private IP?](https://quick-adviser.com/how-do-i-enable-traceroute-in-azure-vm/#What_is_my_private_IP "What is my private IP?")

## How do I enable Traceroute in Azure VM?

So here is how you enable or allow ping (ICMP) to an Azure VM. Click on add a new inbound port rule for the Azure network security group (NSG). Change the protocol to ICMP. As you can see, you can also limit the sources which can make use of that rule, as well as change the name and description.

## Does Traceroute work in Azure?

Ping and Traceroute are not supported on Azure Cloud. To troubleshoot firewall connectivity in Azure cloud, ping and traceroute cannot be used as it is not supported on Azure. Refer to Microsoft FAQ.

## How do I do a traceroute on Linux?

To perform a trace route in Linux open Terminal and type in “traceroute domain.com” replacing domain.com with your domain name or IP address. If you do not have trace route installed you may need to install it. For example in Ubuntu the command to install trace route is “sudo apt-get install traceroute”.

## Can you ping an Azure VM?

When you have created your Virtual Machine in Microsoft Azure the easiest way to test connectivity is to ping your Virtual Machine. By default, ping is disabled for Azure Virtual Machines. To enable pinging, you need to open your Windows Firewall and your Azure Network Security Group.

## Can we ping Azure load balancer?

Can I ping a cloud service? No, not by using the normal “ping”/ICMP protocol. The ICMP protocol is not permitted through the Azure load balancer. To test connectivity, we recommend that you do a port ping.

## What is TCP ping?

TCP Ping is a TCP oriented ping alternative. It is used to test the reachability of a service on a host using TCP/IP and measure the time it takes to connect to the specifed port.

## Can I ping load balancer IP?

2 Answers. Regular icmp traffic is not allowed on Azure load balancers, you should either try a port ping (psping), telnet, nmap, nc, or other utilities to check E2E connectivity. Not only ICMP, any traffic from backend VM to frontend IP of internal load balancer will not work.

## How does the Azure load balancer know which back end VMs are unresponsive?

Use ps ping from one of the backend VMs within the VNet to test the probe port response (example: ps ping 10.0. 0.4:3389) and record results. If no response is received in these ping tests, run a simultaneous Netsh trace on the backend VM and the VNet test VM while you run PsPing then stop the Netsh trace.

## What is azure standard load balancer?

Load balancing refers to evenly distributing load (incoming network traffic) across a group of backend resources or servers. Azure Load Balancer operates at layer 4 of the Open Systems Interconnection (OSI) model. The backend pool instances can be Azure Virtual Machines or instances in a virtual machine scale set.

## How does load balancer work in Azure?

An Azure load balancer is a Layer-4 (TCP, UDP) load balancer that provides high availability by distributing incoming traffic among healthy VMs. A load balancer health probe monitors a given port on each VM and only distributes traffic to an operational VM.

## What is SKU IP address?

All public IP addresses created before the introduction of SKUs are Basic SKU public IP addresses. With the introduction of SKUs, specify which SKU you would like the public IP address to be. Basic SKU addresses: Assigned with the static or dynamic allocation method.

## What is my private IP?

Type: ipconfig and press ENTER. Look at the result and look for the line that says IPv4 address and IPv6 address . What is marked in red are your private IPv4 and IPv6 addresses . You’ve got it!

## psping或paping
