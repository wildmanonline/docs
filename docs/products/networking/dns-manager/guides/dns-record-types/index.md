---
author:
  name: Linode
  email: docs@linode.com
description: ""
license: '[CC BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0)'
published: 2022-10-03
modified_by:
  name: Linode
title: "Supported DNS Record Types"
keywords: ["dns"]
tags: ["linode platform"]
---

## Common Fields

- **Hostname:** The hostname you wish to use. This is also referred to as the subdomain. Leave this field blank (or enter a `@` character) to use the base domain (`example.com`) or enter a value to use a specific subdomain. For instance, entering `www` creates a record for `www.example.com`.

- **TTL** - *Time To Live* (pronounced as `lɪv`): Sets the lifespan of the cache for the DNS record. Setting the TTL to **5 minutes** is recommended for many use cases. If **Default** is selected, the TTL is set to **24 hours**. To provide some context, most DNS queries are handled by a DNS resolver, which acts as the middle entity between the end user's computer and the authoritative name servers. When the DNS resolver receives a query for a new DNS record, it asks the authoritative name server and stores the result in its cache. If another request for that DNS record comes in and the TTL value *has not yet elapsed*, the DNS resolver uses the cached copy. If the TTL *has elapsed*, the DNS resolver re-queries the authoritative name server.

## Support DNS Record Types

### SOA

### NS

### MX

### A/AAAA

An **A** (*Address*) record matches a domain name to an IPv4 address. In most cases, this is the IPv4 address of the machine hosting the desired resource for the domain. **AAAA** (also called *quad A*) records are the same as *A* records, but store the IPv6 address of the machine instead of the IPv4 address. See [Overview of DNS and DNS Records > A and AAAA](/docs/guides/dns-overview/#a-and-aaaa).

- **Hostname:** The hostname you wish to use. This is also referred to as the subdomain. Leave this field blank (or enter a `@` character) to use the base domain (`example.com`) or enter a value to use a specific subdomain. For instance, entering `www` creates a record for `www.example.com`.
- **IP Address:** Enter the IPv4 address of the target server if you wish to create an A record. Enter the IPv6 address of the server to create a AAAA (pronounced *quad A*) record. See the [Find Your Linode's IP Address](/docs/guides/find-your-linodes-ip-address/) guide for help locating an IP address on your Linode Compute Instance.
- **TTL** - *Time To Live* (pronounced as `lɪv`): Sets the lifespan of the cache for the DNS record. Setting the TTL to **5 minutes** is recommended for many use cases. If **Default** is selected, the TTL is set to **24 hours**. To provide some context, most DNS queries are handled by a DNS resolver, which acts as the middle entity between the end user's computer and the authoritative name servers. When the DNS resolver receives a query for a new DNS record, it asks the authoritative name server and stores the result in its cache. If another request for that DNS record comes in and the TTL value *has not yet elapsed*, the DNS resolver uses the cached copy. If the TTL *has elapsed*, the DNS resolver re-queries the authoritative name server.

### CNAME

### TXT

### SRV

### CAA