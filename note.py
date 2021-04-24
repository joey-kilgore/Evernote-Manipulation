# the Note class contains relevant information for storing
#  data related to evernotes
from latexDoc import LatexDoc
import base64

class Note:
    title = ""
    created = ""
    updated = ""
    author = ""
    contentTree = ""
    resources = ""
    latex = ""

    def __init__(self):
        self.title = "new note"

    def printBasicStats(self):
        print("TITLE: "+self.title)
        print("CREATED: "+self.created)
        print("AUTHOR: "+self.author)
        print("DIVS: "+str(len(self.contentTree.findall('div'))))
        print("RESOURCES: "+str(len(self.resources)))

    def addToLatex(self, node):
        if(node.tag == "div"):
            self.latex.addText(node.text)
        
        if(node.tag == 'br'):
            self.latex.addBreak()

        if(node.tag == 'h1'):
            self.latex.addSection(node.text)
        
        if(node.tag == 'h2'):
            self.latex.addSubSection(node.text)
        
        if(node.tag == 'h3'):
            self.latex.addSubSubSection(node.text)

        for child in node:
            self.addToLatex(child)

    def exportToLatex(self):
        self.latex = LatexDoc(self.title, self.author)
        for node in self.contentTree:
            self.addToLatex(node)
        self.latex.writeToFile()

    def saveResources(self):
        for resource in self.resources:
            resourceFile = resource.findall('resource-attributes')[0].findall('source-url')[0].text
            resourceFile = "./output-doc/figs/" + resourceFile.split("+")[2] + ".png"
            img_data = resource.findall('data')[0].text.strip().encode('utf-8')
            with open(resourceFile, "wb") as fh:
                fh.write(base64.decodebytes(img_data))
