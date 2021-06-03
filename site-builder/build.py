#!/usr/bin/python3
import os
import yaml
import glob
from rst2html import rst2html
from template import page

os.chdir("..")
sources = os.listdir("build/sources")

for s in sources:
    yaml_list = glob.glob("build/sources/" + s + "/yaml/*.yaml")
    for file in yaml_list:
        contents = open(file, 'r').read()
        contents = yaml.load(contents, Loader=yaml.FullLoader)

        with open("build/sources/main/rst/" + contents["description"], "r") as f:
            description, warning = rst2html(f.read())

        p = page("site-builder/template.html", os.path.splitext(os.path.basename(file))[0])

        data = {
            "name": contents["name"],
            "os-type": contents["os-type"],
            "homepage": contents["homepage"],
            "release": contents["release"],
            "logo": "https://raw.githubusercontent.com/distrolist/data/master/res/" + contents["logo"],
            "description": description,
            "licenses": ', '.join(contents["license"]),
            "based-on": ', '.join(contents["based-on"]),
            "origin": ', '.join(contents["origin"]),
            "founder": ', '.join(contents["founder"]),
            "desktop": ', '.join(contents["desktop"]),
            "architecture": ', '.join(contents["architecture"]),
            "category": ', '.join(contents["category"]),
            "package-manager": ', '.join(contents["package-manager"]),
            "service-manager": ', '.join(contents["service-manager"]),
        }
        p.set_var(data)
        p.save()
