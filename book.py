# the Note class contains relevant information for storing
#  data related to evernotes
from latexDoc import LatexDoc
import base64
import note

class Book:
    title = ""
    created = ""
    updated = ""
    author = ""
    notes = []
    latex = ""

    def __init__(self):
        self.title = "book"
        self.notes = []

    def printBasicStats(self):
        print("TITLE: "+self.title)
        print("CREATED: "+self.created)
        print("AUTHOR: "+self.author)
        print("DIVS: "+str(len(self.contentTree.findall('div'))))
        print("RESOURCES: "+str(len(self.resources)))

    def exportToLatex(self):
        self.latex = LatexDoc(self.title, self.author, 'book')
        for note in self.notes:
            self.latex.addChapter(note.title)
            note.exportToLatex()
            self.latex.documentText += note.latex.documentText
        self.latex.writeToFile()
        self.saveResources()

    def saveResources(self):
        for note in self.notes:
            for resource in note.resources:
                resourceFile = resource.findall('resource-attributes')[0].findall('source-url')[0].text
                resourceFile = "./output-doc/figs/" + resourceFile.split("+")[2] + ".png"
                img_data = resource.findall('data')[0].text.strip().encode('utf-8')
                with open(resourceFile, "wb") as fh:
                    fh.write(base64.decodebytes(img_data))
