#!/usr/bin/python3
import os
import yaml
import glob
from rst2html import rst2html
from template import page

os.chdir("..")
sources = os.listdir("build/sources")

for s in sources:
    contents = yaml.load(open(glob.glob("build/sources/" + s + "/yaml/*.yaml")[0]).read(),
                         Loader=yaml.FullLoader)

    with open("build/sources/main/rst/" + contents["description"], "r") as f:
        description, warning = rst2html(f.read())

    p = page("site-builder/template.html")
    p.set_var("content", description)
    p.set_var("logo", "https://raw.githubusercontent.com/distrolist/data/master/res/" + contents["logo"])
    p.save()