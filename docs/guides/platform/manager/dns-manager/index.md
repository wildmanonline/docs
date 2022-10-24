---
slug: dns-manager
author:
  name: Linode
  email: docs@linode.com
description: "Learn how to use Linode's Domain service, a comprehensive DNS management service for controlling DNS records on your domain names."
keywords: ["dns manager", "linode dns", "Linode Cloud Manager dns", "dns configuration", "ttl", "domain zones", "domain name"]
tags: ["linode platform","networking","cloud manager","dns"]
license: '[CC BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0)'
aliases: ['/dns-manager/','/platform/manager/dns-manager/','/networking/dns/dns-manager/','/platform/manager/dns-manager-new-manager/','/networking/dns/dns-manager-overview/','/platform/manager/dns-manager-classic-manager/']
modified: 2021-11-30
modified_by:
  name: Linode
published: 2009-07-16
title: "DNS Manager"
image: dns-manager.png
---

### Subdomains

Add a subdomain by adding an entry under the *A/AAAA Record* heading, with just the subdomain. For example, for `subdomain.example.com`

1. Add `subdomain` under *Host*.

1. Set the IP address.

1. Adjust the TTL if necessary.

1. Click **Save**.


### Wildcards

A wildcard DNS record will match requests for domains that do not exist. Wildcards are often used to point all non-existing subdomains to an existing top level domain. For example, if a queried first-level subdomain does not exist, the IP address specified in the wildcard DNS record will respond.

To create a [wildcard DNS record](https://en.wikipedia.org/wiki/Wildcard_DNS_record):

1. Navigate to the **Domains** section of the Cloud Manager and click on the Domain that you'd like to add a wildcard DNS record to.

1. Find the **A/AAAA Record** section and select **Add an A/AAAA Record**.

1. When the **Create A/AAAA Record** panel appears, enter an asterisk (`*`) in the **Hostname** field and provide a valid IP address in the **IP Address** field.

1. Click **Save**.

{{< note >}}
A wildcard must always be the furthest subdomain from the TLD (top level domain), i.e. `*.example.com`. If you would like to add a wildcard as a subdomain for a subdomain, you will need to add a new domain zone for that subdomain and then add the wildcard record to it. For example, to create `*.subdomain.example.com`, you must add a separate domain zone for `subdomain.example.com` first, then add an A/AAAA DNS record to that zone as indicated above.
{{</ note >}}

### Sub-Subdomains

The Linode Cloud Manager does not support the addition of a subdomain on top of an existing subdomain in the same domain zone. For example, if you have `example.com` as a domain with an A record for `subdomain.example.com`, you cannot create `another.subdomain.example.com` within that same domain zone.

Instead, [add the subdomain](#add-a-domain) to the Cloud Manager as a separate domain with its own domain zone and DNS records. Then add an A/AAAA record for the second-level subdomain. In the previous example, you would create a domain zone named `subdomain.example.com`, the create an A/AAAA record with hostname `another` inside of it.

### Import Domains with AXFR

If you're migrating domains to Linode from another hosting provider and that provider allows zone transfers from its DNS server, it may be possible to import your existing domain and its DNS records into the Linode Cloud Manager. If the import is successful, the domain along with all of its existing DNS records will be available in the **Domains** section of the Cloud Manager.

Here's how to import a zone file:

1.  From the **Domains** section, click on **Import a Zone**.

    ![This page lets you import a domain zone.](import-zone-axfr.png "Import a domain zone with AXFR")

1.  Enter the domain name in the **Domain** field, as shown in the example above.

1.  Enter the name server in the **Remote Nameserver** field.

    {{< note >}}
The name server must allow zone transfers (AXFR) from the following IP addresses:

    96.126.114.97
    96.126.114.98
    2600:3c00::5e
    2600:3c00::5f
{{< /note >}}

1.  Click **Save**. The Linode Cloud Manager will connect to the remote name server and import your existing DNS records.

### Clone DNS records

The *Clone* feature allows you to copy DNS records from an existing domain in your Linode account to a new domain. If you've already set up DNS records for one of the services you host on your Linode account, this is a good way to quickly assign another domain to that same service.

Here's how to clone DNS records for an existing domain:

1.  Click on the **more options ellipsis** corresponding to the domain whose DNS records you would like to clone and select **Clone** from the menu.

1.  Enter the name of the new domain in the **New Domain** field.

    ![Clone an existing domain zone](domain-clone-a-zone.png "Clone an existing domain zone.")

1.  Click **Create**. The DNS records will then be copied from the existing domain to the domain.

## DNSSEC Limitations

The Linode DNS Manager does not support DNSSEC at this time. If you have DNSSEC enabled at your domains registrar it will cause name resolution failures such as `NXDOMAIN` when an attempt is made to access the DNS.

## Next Steps

Now that you are familiar with Linode's DNS Manager, you should set up your [reverse DNS configuration](/docs/guides/configure-your-linode-for-reverse-dns/), and consider reading through at our [Common DNS Configurations](/docs/guides/common-dns-configurations/) guide. For help with DNS records, see our [Troubleshooting DNS](/docs/platform/manager/troubleshooting-dns) guide.
