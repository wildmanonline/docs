---
slug: mysql-authsocket-authentication-note-shortguide
title: About MySQL auth_socket Authentication
description: 'Shortguide that describes how MySQL auth_socket authentication works.'
authors: ["Linode"]
contributors: ["Linode"]
published: 2018-08-03
license: '[CC BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0)'
keywords: []
tags: ["web server","php","mysql","apache","security","lamp"]
headless: true
show_on_rss_feed: false
aliases: ['/web-servers/lamp/mysql-authsocket-authentication-note-shortguide/']
---

{{< note type="secondary" title="About MySQL authentication" isCollapsible=true >}}
By default, MySQL is configured to use the `auth_socket` authorization plugin. This authorization scheme allows you to log in to the database's root user as long as you are connecting from the Linux root user on localhost, or as a user with sudo privileges (i.e. with `sudo mysql -u root`). In this scheme, no password is assigned to MySQL's root user:

{{< highlight sql >}}
mysql> SELECT user,host,authentication_string,plugin FROM mysql.user WHERE user='root';
+------+-----------+-----------------------+-------------+
| user | host      | authentication_string | plugin      |
+------+-----------+-----------------------+-------------+
| root | localhost |                       | auth_socket |
+------+-----------+-----------------------+-------------+
1 row in set (0.02 sec)
{{< /highlight >}}

You can keep using the `auth_socket` plugin, and this is considered a secure option for production systems. If you'd rather switch to password authentication and assign a password, enter the following commands. Replace `password` with a new root password:

{{< highlight sql >}}
mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH 'mysql_native_password' BY 'password';
mysql> FLUSH PRIVILEGES;
{{< /highlight >}}

After making this change, you should pass the `-p` option when invoking the MySQL shell:

    mysql -u root -p

{{< /note >}}