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
    
    def printLatex(self):
        self.latex.writeToFile()
