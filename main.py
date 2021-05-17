import urllib.request
import os
sources=[]
os.mkdir("build")
def get_sources(link=""):
    print("Import: "+str(link))
    try:
        list=urllib.request.urlopen(link).read().decode("UTF-8")
        for line in list.split("\n"):
            if len(line)<5 or line[0] == "#":
                pass
            elif "import " in line:
                get_sources(line.split(" ")[1])
            elif "://" in line:
                sources.append(line)
    except:
        print("Failed to import url")

get_sources("https://raw.githubusercontent.com/distrolist/data/master/main.list")
get_sources("https://raw.githubusercontent.com/distrolist/data/master/imports.list")
os.mkdir("build/sources")
for s in sources:
    print(s)
    try:
        f=urllib.request.urlopen(s).read().decode("UTF-8")
        file="build/sources/"+s.split("/")[-1].split(".")[0]+".yaml"
        print(file)
        open(file,"w").write(f)
    except:
        pass
