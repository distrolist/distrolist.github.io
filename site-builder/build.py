#!/usr/bin/python3
import os
import yaml
import glob
from rst2html import rst2html
from template import page

os.chdir("..")
sources = os.listdir("build/sources")
index_page=open("site/index.html","w")
def l2str(l):
    if type(l) == type(""):
        print(l)
        return str(l)
    ret=""
    for i in l[:-2]:
        ret+=i+", "
    ret+=l[-1]
    return ret

for s in sources:
    for d in os.listdir("build/sources/{}/yaml".format(s)):
        contents = yaml.load(open(glob.glob("build/sources/" + s + "/yaml/" + d)[0]).read(),
                             Loader=yaml.FullLoader)

        with open("build/sources/" + s + "/rst/" + contents["description"], "r") as f:
            description, warning = rst2html(f.read())

        p = page("site-builder/template.html")
        p.name = contents["name"]
        p.set_var("description", description)
        for i in ["name","homepage","based-on","os-type","release","origin","founder",
                  "category","license","founder","desktop","package-manager",
                  "service-manager","architecture"]:
            try:
                p.set_var(str(i), str(l2str(contents[i])))
            except:
                p.set_var(str(i), "Unknown")
        ss=""
        try:
            for img in contents["screenshot"]:
                ss+="\t<img class=\"screenshot\" src=\""+"https://raw.githubusercontent.com/distrolist/data/master/res/"+str(img)+"\">\n"
            p.set_var("screenshot",ss)
        except:
            p.set_var("screenshot","Screenshot not available!")
        p.set_var("logo", "https://raw.githubusercontent.com/distrolist/data/master/logo/" + contents["logo"])
        p.save()

        index_page.write("<a href=\"{0}.html\">{0}</a><br>\n".format(contents["name"]))

