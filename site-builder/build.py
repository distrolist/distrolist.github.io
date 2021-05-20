#!/usr/bin/python3
import os
from template import page
os.chdir("..")
sources=os.listdir("build/sources")
for s in sources:
    p=page("site-builder/template.html")
    p.set_var("content","RST2HTML body")
    p.set_var("logo","https://raw.githubusercontent.com/distrolist/data/master/res/debian-logo.svg")
    p.save()
