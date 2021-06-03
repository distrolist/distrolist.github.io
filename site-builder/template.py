class page:
    def __init__(self, path="", name="example"):
        self.template = open(path, "r").read()
        self.path = "site"
        self.name = name
        self.css = ["../site-builder/main.css"]

    def save(self):
        """save template to file"""
        f = open("{}/{}.html".format(self.path, self.name), "w")
        f.write("<!DOCTYPE html>\n")
        f.write("<html>\n  <head>\n")
        f.write("  <meta charset=\"utf-8\">\n")
        for c in self.css:
            f.write("  <link rel=\"Stylesheet\" href=\"{}\" />\n".format(c))
        f.write("  </head>\n<body>\n")
        for line in self.template.split("\n"):
            f.write("    {}\n".format(line))
        f.write("  </body>\n</html>")
        f.close()

    def set_var(self, data):
        """set variable from template set_var("name","example")"""
        print(data)
        for key, value in data.items():
            self.template = self.template.replace("@{}@".format(str(key)), str(value))
