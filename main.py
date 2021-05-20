#!/usr/bin/python3
import os
sources=[]
distros=[]
os.mkdir("build")
os.mkdir("build/sources")
os.chdir("build/sources")

def get_sources(link="",name=""):
    print("Import: "+str(link))
    os.system("git clone \"{}\" \"{}\"".format(link,name))

print("\x1b[33;1mGetting source list\x1b[;0m")
f=open("../../repos","r").read().split("\n")
for line in f:
    if "::" in line:
        name=line.split("::")[0]
        link=line.split("::")[1]
        get_sources(link,name)
