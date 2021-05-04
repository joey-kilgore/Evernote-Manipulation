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

    def getStateTypeNode(self, node):
        if(node.tag == "div"):
            if("style" in node.attrib):
                if('text-align:center' in node.attrib['style']):
                    return "CENTERED"
                if('text-align:right' in node.attrib['style']):
                    return "RIGHTALIGNED"
                if('--en-codeblock:true' in node.attrib['style']):
                    return "CODEBLOCK"
                return "TEXT"
            return "TEXT"

        if(node.tag == 'span'):
            if('style' in node.attrib):
                if('--en-highlight:yellow' in node.attrib['style']):
                    return "LITERAL"
                return "TEXT"
            return "TEXT"
        
        if(node.tag == 'b'):
            return "BOLD"

        if(node.tag == 'i'):
            return "ITALIC"

        if(node.tag == 'u'):
            return "UNDERLINE"

        if(node.tag == 'br'):
            return "BREAK"

        if(node.tag == 'h1'):
            return "SECTION"
        
        if(node.tag == 'h2'):
            return "SUBSECTION"
        
        if(node.tag == 'h3'):
            return "SUBSUBSECTION"

        if(node.tag == 'en-media'):
            return "FIGURE"
        
        if(node.tag == 'a'):
            #self.latex.addText(node.attrib['href'])
            return "TEXT"

        if(node.tag == 'ul'):
            return "UNORDEREDLIST"
        
        if(node.tag == 'ol'):
            return "ORDEREDLIST"

        if(node.tag == 'li'):
            return "ITEM"

    def getTextNode(self, node):
        if(node.tag == 'en-media'):
            return node.attrib['hash']+".png"
        if(node.tag == 'a'):
            return node.attrib['href']
        return node.text

    def addNodeToLatex(self, node):
        stateType = self.getStateTypeNode(node)
        innerText = self.getTextNode(node)
        tailText = node.tail

        self.latex.addState(stateType, innerText, tailText)

        for child in node:
            self.addNodeToLatex(child)
        
        self.latex.removeState()

    def exportToLatex(self):
        self.latex = LatexDoc(self.title, self.author, 'article')
        for node in self.contentTree:
            self.addNodeToLatex(node)
        self.saveResources()

    def printLatex(self):
        self.latex.writeToFile()

    def saveResources(self):
        for resource in self.resources:
            resourceFile = resource.findall('resource-attributes')[0].findall('source-url')[0].text
            resourceFile = "./output-doc/figs/" + resourceFile.split("+")[2] + ".png"
            img_data = resource.findall('data')[0].text.strip().encode('utf-8')
            with open(resourceFile, "wb") as fh:
                fh.write(base64.decodebytes(img_data))
