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

### withings-analyze.py

Dissects the top level file container of Withings firmware update, displays basic information.
```
./withings-analyze.py firmware1.bin
= File header =
Header checksum: 2211132523

Entry type: 1 (16 bytes)
 58 00 00 00 44 98 04 00 B3 17 E2 A9 B5 14 00 00
 Type: main firmware
 301124 bytes @ 88 (ends at 301211)
 dd if=firmware1.bin of=firmware1.bin.1 bs=1 count=301124 skip=88
 CRC: 0xA9E217B3
 Version: 5301

Entry type: 4 (16 bytes)
 9C 98 04 00 00 40 00 00 03 4D 96 49 12 00 00 00
 Type: boot loader
 16384 bytes @ 301212 (ends at 317595)
 dd if=firmware1.bin of=firmware1.bin.4 bs=1 count=16384 skip=301212
 CRC: 0x49964D03
 Version: 18

Entry type: 7 (16 bytes)
 9C D8 04 00 2D A7 00 00 2B 78 C2 F3 02 50 00 00
 Type: unknown
 42797 bytes @ 317596 (ends at 360392)
 dd if=firmware1.bin of=firmware1.bin.7 bs=1 count=42797 skip=317596
 CRC: 0xF3C2782B
 Version: 20482

Entry type: 8 (16 bytes)
 CC 7F 05 00 C8 B6 01 00 A9 E2 36 60 88 00 00 00
 Type: unknown
 112328 bytes @ 360396 (ends at 472723)
 dd if=firmware1.bin of=firmware1.bin.8 bs=1 count=112328 skip=360396
 CRC: 0x6036E2A9
 Version: 136
```
