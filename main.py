import urllib
sources=[]
def get_sources(link=""):
    print("Import: "+str(link))
    list=urllib.urlopen(link).read()
    for line in list.split("\n"):
        if len(line)<5:
            pass
        elif "import " in line:
            get_sources(line.split(" ")[1])
        elif line[0] != "#":
            if "gh://" in line:
                line.replace("gh://","https://raw.githubusercontent.com/")
            sources.append(line)

get_sources("https://raw.githubusercontent.com/paledega/distrolist.github.io/master/main.list")
get_sources("import https://raw.githubusercontent.com/paledega/distrolist.github.io/master/imports.list")
print(sources)
