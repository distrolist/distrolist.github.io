import urllib.request
sources=[]
def get_sources(link=""):
    print("Import: "+str(link))
    list=urllib.request.urlopen(link).read().decode("UTF-8")
    for line in list.split("\n"):
        if len(line)<5:
            pass
        elif "import " in line:
            get_sources(line.split(" ")[1])
        elif line[0] != "#":
            sources.append(line)

get_sources("https://raw.githubusercontent.com/paledega/distrolist.github.io/master/main.list")
get_sources("https://raw.githubusercontent.com/paledega/distrolist.github.io/master/imports.list")
print(sources)
