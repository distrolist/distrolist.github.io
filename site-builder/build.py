#!/usr/bin/python3
import os
os.chdir("..")
os.mkdir("site")
distros=os.listdir("build/sources")
print(distros)
