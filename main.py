import urllib
sources=[]
def get_sources(link=""):
    list=urllib.urlopen(link).read()
    for line in list.split("\n"):
        if "import " in line:
            get_sources(line.split(" ")[1])
        else:
            sources.append(line)

get_sources("https://raw.githubusercontent.com/paledega/distrolist.github.io/master/main.list")
print(sources)