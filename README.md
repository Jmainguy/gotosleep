# gotosleep
A golang daemon to shut off the computer at a set time.
## Compile
Read instructions in Makefile for pre-reqs, once met run
```/bin/bash
make rpm
```
## Install
Find location of compiled rpm from output above
```/bin/bash
dnf install <gotsleep.rpm>
```

## Configure
Set the time you want computer to shut off at every night in 
```/bin/bash
/etc/gotosleep/config.yaml
```

## Run
It installs as a systemd daemon, stop / start it as such
```/bin/bash
systemctl start gotosleep
systemctl enable gotosleep
```
