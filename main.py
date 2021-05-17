import urllib.request
import os
sources=[]
distros=[]
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
                distro=line.split("/")[-1].split(".")[0]
                if distro in distros:
                    print("Distro already exists:"+distro)
                    exit(1)
                else:
                    distros.append(distro)
    except:
        print("Failed to import url")

print("\x1b[33;1mGetting source list\x1b[;0m")
get_sources("https://raw.githubusercontent.com/distrolist/data/master/main.list")
get_sources("https://raw.githubusercontent.com/distrolist/data/master/imports.list")
os.mkdir("build/sources")
print("\x1b[33;1mDistributions:\x1b[;0m "+str(distros))
print("\x1b[33;1mGetting distro information\x1b[;0m")
for s in sources:
    try:
        f=urllib.request.urlopen(s).read().decode("UTF-8")
        print("Import: "+s)
        file="build/sources/"+s.split("/")[-1].split(".")[0]+".yaml"
        if not os.path.exists(file):
            open(file,"w").write(f)
    except:
        print("Fail:"+s)
