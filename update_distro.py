#!/usr/bin/python3
import os
f=open("main.list","w")
link="https://raw.githubusercontent.com/distrolist/distrolist.github.io/master/distro/"
for distro in os.listdir("distro"):
    print(distro)
    f.write(link+distro)
