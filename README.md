# tiny-shell-scripts
scripts, utilities, stuff too small to have its own repository

### ssh_proxycommand.php

allows you to ssh over multiple nodes in one take, like this:
```
ssh host1/host2 # ssh to host2, then to host1
ssh host1/host2/host3/host4 # ssh host4, then host3, then host2, then host1
ssh user1@host1/user2%host2/user3%host3 # obvious
ssh 'user1@host1/user2%host2#2222/user3%host3' # obvious, but port 2222 in the middle
```

Installation instructions included in the file.

### sanitize-ip.py

```
$ echo 'check out 1.2.3.4 or http://www.example.com/, yo!' | sanitize-ip.py 
check out 1[.]2[.]3[.]4 or http://www[.]example[.]com/, yo!
$
```

Installation is pretty obvious:
```
wget https://raw.githubusercontent.com/milankowww/tiny-shell-scripts/master/sanitize-ip.py
chmod a+x sanitize-ip.py
mv sanitize-ip.py /usr/local/bin/
```

### kvm-heartbeat-cluster/

A heartbeat resource script to run KVM virtual machines on a cluster, with live migration and bells and whistles.
