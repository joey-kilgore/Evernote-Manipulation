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

    def addTextToLatex(self, node):
        self.latex.addText(node.text)
        for child in node:
            self.addToLatex(child)

    def addToLatex(self, node):
        if(node.tag == "div"):
            if('style' in node.attrib):
                style = None
                if('text-align:center' in node.attrib['style']):
                    self.latex.startCentering()
                    style = 'center'

                if('text-align:right' in node.attrib['style']):
                    self.latex.startRightAlign()
                    style = 'right'

                if('--en-codeblock:true' in node.attrib['style']):
                    self.latex.startCodeBlock()
                    style = 'code'
                
                if(style != None):
                    self.addTextToLatex(node)
                    self.latex.addText(node.tail)

                if(style == 'center'):
                    self.latex.endCentering()

                if(style == 'right'):
                    self.latex.endRightAlign()

                if(style == 'code'):
                    self.latex.endCodeBlock()

                return
            else:
                self.addTextToLatex(node)
                self.latex.endText()
                return

        if(node.tag == 'span'):
            self.addTextToLatex(node)
            self.latex.endText()
            return

        if(node.tag == 'b'):
            self.latex.startBold()
            self.addTextToLatex(node)
            self.latex.endFormat()
            self.latex.addText(node.tail)
            return

        if(node.tag == 'i'):
            self.latex.startItalic()
            self.addTextToLatex(node)
            self.latex.endFormat()
            self.latex.addText(node.tail)
            return
        
        if(node.tag == 'u'):
            self.latex.startUnderline()
            self.addTextToLatex(node)
            self.latex.endFormat()
            self.latex.addText(node.tail)
            return

        if(node.tag == 'br'):
            self.latex.addBreak()

        if(node.tag == 'h1'):
            self.latex.addSection(node.text)
        
        if(node.tag == 'h2'):
            self.latex.addSubSection(node.text)
        
        if(node.tag == 'h3'):
            self.latex.addSubSubSection(node.text)

        if(node.tag == 'en-media'):
            self.latex.addFigure(node.attrib['hash']+".png")
        
        if(node.tag == 'a'):
            self.latex.addText(node.attrib['href'])

        if(node.tag == 'ul'):
            self.latex.startUnorderedList()
            for child in node:
                self.addToLatex(child)
            self.latex.endUnorderedList()
            return
        
        if(node.tag == 'ol'):
            self.latex.startOrderedList()
            for child in node:
                self.addToLatex(child)
            self.latex.endOrderedList()
            return

        if(node.tag == 'li'):
            self.latex.addItem()

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
