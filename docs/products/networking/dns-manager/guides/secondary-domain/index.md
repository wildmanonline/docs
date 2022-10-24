---
author:
  name: Linode
  email: docs@linode.com
description: "How (and why) to use the Linode DNS Manager as a secondary name server."
license: '[CC BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0)'
modified: 2022-09-23
modified_by:
  name: Linode
published: 2022-09-23
title: "Secondary Name Server"
keywords: ["dns"]
tags: ["linode platform","cloud manager"]
---

When you add, edit, or delete DNS records, the changes are made directly to the primary name server. Secondary name servers then query the primary name server and obtain a copy of the updated DNS records. 

In modern usage, there's less of a distinction between primary and secondary name servers than their use to be. Most DNS providers offer 2 or more name servers that are anycasted to many geographically distributed locations. This effectively means that there could be tens or hundreds of name servers that are hosting your domain's DNS records. When defining the authoritative name servers at your registrar, you can use one or more of the name servers given to you by your DNS provider. It does not matter which ones you add to your domain registrar. All name servers added to your domain within your registrar or DNS provider are authoritative, regardless if they are technically a primary or secondary name server.

If your DNS provider does not offer secondary name servers, is not equipped to handle large amounts of DNS traffic, or does not implement any high availability features.

A common reason for using another DNS provider as a secondary name server is if your primary name server is self-hosted. It could be that you're running a dedicated DNS software (such as BIND) and manually creating and updating your DNS records within that software. It could also be that you are using a piece of software that automatically manages DNS records for you, such as cPanel, Plesk, and many other applications. In these cases, you may value the control or automation you get from self-hosting the 

Most major DNS providers include a primary name server and one or more secondary name servers by default. It does not matter which ones you add to your domain registrar. All name servers added to your domain within your registrar or DNS provider are authoritative, regardless if they are technically a primary or secondary name server.