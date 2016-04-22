A simple two-node cluster to run virtual machines on top of Ubuntu Linux. Ingredients:

* two computers (obvious) connected via dedicated link
* drbd + ocfs (to share the virtual server data), filesystem mounted at /shared
* heartbeat

Name your nodes something1 and something2 so that automatic scripts could
guess the name of the other node.

Create ssh key trust between the both nodes, _PermitRootLogin without-password_
in _/etc/ssh/sshd.config_.

Create a partition on both machines, configure it as a physical storage for
DRBD. Configure DRBD with _become-primary-on both;_

On top of the resource create the OCFS filesystem and add it to _/etc/fstab_
with _/dev/drbd/by-res/shared/0 /shared ofcs2 __netdev 0 0_

Don't forget `mkdir -p /shared/xml/something1 /shared/xml/something2`

Put _ipsec-virsh_ into /etc/heartbeat/resource.d and add a cluster resource
into _/etc/heartbeat/haresources_ for both nodes:
```
something1 \
        ipsec_virsh::something1::/shared

something2 \
        ipsec_virsh::something2::/shared
```

Put _live-migrate_ into /usr/local/bin.

Now put XML definitions for your virtual machines in /shared/xml/something1/
or something2.

Start heartbeat: `/etc/init.d/heartbeat start`
