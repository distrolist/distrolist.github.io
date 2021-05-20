class page:
    def __init__(self,path=""):
        self.template=open(path,"r").read()
        self.path="site"
        self.name="example"
        self.css=["../site-builder/main.css"]
    def save(self):
        """save template to file"""
        f=open("{}/{}.html".format(self.path,self.name),"w")
        f.write("<html>\n  <head>\n")
        for c in self.css:
            f.write("  <link rel=\"Stylesheet\" href=\"{}\" />\n".format(c))
        f.write("  </head>\n</body>\n")
        for line in self.template.split("\n"):
            f.write("    {}\n".format(line))
        f.write("  </body>\n</html>")
        f.close()
    def set_var(self,variable,value):
        """set variable from template set_var("name","example")"""
        self.template=self.template.replace("@{}@".format(variable),value)
