What is a VPC?
A Virtual Private Cloud (VPC) is a private, isolated network that a customer can manage that has been securely carved out of a cloud provider’s public network. With a VPC, customers can deploy applications whose data communications are hidden and fully isolated from the view of the public internet and the other tenants deployed within the same cloud provider infrastructure.

A core principle with any VPC technology is that it provides network-level isolation guarantees on behalf of the customer that the cloud provider enforces.
Can I use a VLAN as a VPC?
Yes. Linode’s VLAN service provides customers with a pure layer-2 or ethernet layer isolation technology. When attaching virtual machine instances onto a Virtual Local Area Network (VLAN), the customer is effectively plugged into their own isolated and virtual network switch.

Since the service operates at layer-2, any application that was designed to work connected to a network switch will work with Linode’s VLAN service. So, for example, applications like keepalived or any other application that uses local broadcast or multicast traffic will work as expected without modification. The application can also use any network protocol, not just IP. You could even host a virtual LAN party and play multiplayer Doom like in 1993, which used IPX, not IP, in its networking stack.

The same security challenges of operating a network at layer-2 apply here. Since Linode provides isolation at the layer-2 boundary, securing the upper protocol layers is the customer's responsibility. Therefore, layer-3 and above firewall protections must be implemented using a solution like iptables or nftables. The customer may also need to provide address resolution protocol (ARP) and neighbor discovery (ND) protections to secure the binding between the layer-2 and associated layer-3 address for communication. These protection requirements are the side-effect of having a purely layer-2 implementation. The risks and security considerations are no different than having a set of physical machines plugged into a shared network switch.

A VLAN can only be deployed within a region and cannot span regions or accounts. Therefore, any bridging of VLANs is something that the customer would also need to provide. Bridging of VLANs may also become limited by the bandwidth limitations of the compute plan selected.

Linode maintains a guide detailing the common-use cases for its VLAN service and tutorials on creating and configuring it. Linode also allows customers to configure compute instances with multiple interfaces. The linked tutorials demonstrate how to use multiple VLAN interfaces in addition to the default public interface.
How Does VLAN Compare with other VPC Implementations?
Other cloud providers typically use a purely layer-3 (aka network layer or IP layer) approach with their VPC implementations, in contrast to the pure layer-2 implementation offered by Linode.

As a result, broadcast and multicast capabilities are typically not supported. Also, the network traffic within a VPC must be IP-based, and some provider implementations further restrict the transport protocols that may be utilized.

The cloud provider ensures proper binding between layer-2 and layer-3 addresses used on the VPC. The customer can often configure firewall policy (aka network security groups) for any layer-3 or above traffic flowing through the VPC and the host itself. Doing so allows the cloud provider to be configured with firewall rules it can enforce without the customer resources needing to provide their own firewall and network protection capabilities.

Most other cloud provider VPC implementations are routed. This approach allows multiple subnets to be stitched together and VPC implementations to peer across regions, on-premises data centers, and different accounts or subscriptions.

Managed service offerings and software-as-a-service (SaaS) products sold by the cloud provider can also be placed onto the VPC directly thereby allowing nodes without public internet access the ability to consume these services using private addresses.
When Should I use a VLAN as a VPC?
The answer here depends on the trust model for your deployment and how many additional layers of protection are required to achieve your particular isolation and security goals. The answer also depends on the type of network flows your application aims to support and if the traffic stays largely within the VLAN or needs to communicate with many external services.

The VLAN approach is likely sufficient for any deployment where basic network-level segmentation is required. The VLAN can then be used as a private network segment where any resource deployed within the VLAN can freely communicate with any other resource using the VLAN-dedicated interface. Any additional protections within the VPC would need to be provided or implemented by each resource on the network beyond the layer-2 isolation the Linode VLAN service offers.

The use of a VLAN also fits use-cases where the bulk of the traffic flows stay within the VLAN itself. If the resources deployed within the VLAN need to talk to other resources outside the VLAN, for example, the public internet or other external managed services, then it is possible that performance can become bottlenecked via aggregation points like NAT exit points or service gateways.
Why Not Use a Cloud Firewall to Create a VPC?
Linode offers a cloud firewall product that can apply to any Linode interface configured with public or data center-scoped private IP addresses. However, the cloud firewall cannot be used with VLAN interfaces.

A firewall by itself does not strictly offer data segmentation. It simply protects the host from sending or receiving particular traffic classes as configured by the firewall rules. The firewall does not protect the data once it leaves its enforcement boundary.

That said, private IP addresses can be used to scope data to a given region and, when combined with cloud firewall rules, can further restrict information sharing between Linodes. Private IP addresses can also transfer data with other customers deployed within the same data center. This configuration is fragile and requires tight coordination to prevent accidental data exposure. However, pending the application, it can create a lightweight VPC where the data isolation is scoped to a data center (aka region) and further restricted using a cloud firewall.
What About Spanning Across Multiple Regions?
Linode does not offer a managed solution that can route across VLAN segments deployed in multiple regions. One way to implement such a solution is to stitch VLAN segments together using a Virtual Private Network (VPN).

Multiple VLANs deployed in a single region can be stitched together using a Linode that can act as a common router. Each VLAN segment is its own isolated layer-2 domain and is expected to operate within its layer-3 subnet. A Linode can then be deployed with multiple VLAN interfaces assigned to each VLAN and configured to act as a router. All traffic between the various VLAN segments will flow through the router, and firewall rules can be placed within the router to govern what traffic is allowed to traverse between the multiple segments.

This router instance can then be configured to bridge traffic between other network segments using the public internet and a VPN software like WireGuard or a protocol like IPSec.


In the above picture, each region is responsible for managing connectivity between several isolated VLANs. The router instances can then bridge the multiple regions locally using compute instances with multiple interfaces. These router nodes can then span multiple regions using WireGuard tunnels over the public internet to each region.

Traffic can now flow between any VLAN regardless of region. In addition, the router nodes can also be used as Network Address Translation (NAT) exit points providing internet connectivity for their local VLAN instances if they are deployed without local internet connectivity. In this configuration, the local router instance would be designated as the default gateway (i.e., typically configured as 10.0.0.1 on a 10.0.0.0/24 network). The router nodes can also be used as Secure Socket Shell (SSH) management bastions.

A common way to implement this kind of NAT configuration is by using a firewall rule to mark WireGuard traffic and to use IP masquerading for any traffic detected without this mark. For example, the router would be configured to use an iptables rule like
iptables -t nat -A POSTROUTING -o eth0 -m mark ! --mark 42 -j MASQUERADE
where WireGuard is configured to use a FirewallMark (i.e., 42) within its configuration. This ensures that the WireGuard traffic is not NATed while all VLAN traffic is NATed.

The cloud firewall rules would then get configured to allow the WireGuard communication between routing nodes (typically, udp/51820).

The router instances can then be configured with firewall rules to control or record traffic flow across the local and global segments as necessary.

This kind of geometry allows sharing of data globally across multiple regions and empowers the router instances to control the traffic flow between the customer’s various VLAN segments.
When funneling traffic from multiple VLAN segments into a single aggregation point, it is critical to understand the performance and bandwidth considerations when doing so. The performance will likely be limited by the upload bandwidth restrictions imposed by the virtual compute instance of the router itself. The VPN technology selected will also further impose point-to-point bandwidth limitations. 
What About Spanning Across Multiple Clouds?
The same kind of technology used to span across multiple regions could be used across various cloud providers. For example, a compute instance can be placed within another cloud service provider’s network boundary and tied into its local, cloud provider-specific VPC configuration. A WireGuard tunnel between the router instance could be used to bridge into the cloud provider network.

Another approach that is more commonly supported natively by many cloud providers is to peer across VPC implementations via a site-to-site IPSec VPN tunnel. StrongSwan, for example, could be used to set up the VPN tunnel between the router and a given cloud provider VPC network. It is best to configure the router to ignore marked IPSec traffic using the same firewall marking trick discussed above when the router is also acting as a NAT exit point.
What Else Exists?
Managing multiple WireGuard or IPSec tunnels to create a VPN overlay network can become quickly unwieldy. 

Slack’s Nebula project and products like Tailscale can be used to create and secure a mutually authenticated private overlay network. Tailscale is a more polished subscription-based service that simplifies but essentially mimics the fundamental capabilities of the open-source Nebula project. 

Nebula provides a user-controlled certificate authority that issues cryptographic assertions via a custom certificate format that defines what IP(s) a node can claim ownership over within the overlay, what network it is part of, any downstream networks it can connect to, and the group of machines it is associated with for general purpose access control when drafting firewall rules.

Nebula hosts must have network connectivity to lighthouses. The lighthouse nodes help the Nebula hosts discover other hosts on the overlay network. They can communicate directly and form to create a private network overlay. The routing path is optimized for performance and basic connectivity requirements.

For use cases where nodes need to communicate across multiple network segments more freely, a private overlay network may result in better aggregate performance than funneling traffic through common aggregation points.
The result is a comprehensive VPC-like overlay with cloud agnostic firewalling policy configuration.

It’s also worth noting, that the lighthouse instances may also be cost-effectively hosted on Linode compute infrastructure.
