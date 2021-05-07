import defs

class State:
    def __init__(self, stateType, innerText, tailText):
        self.stateType = stateType
        self.innerText = innerText
        self.tailText = tailText

class LatexDoc:
    documentClass = ""
    title = ""
    author = ""
    date = ""
    documentText = ""
    filePath = ""
    stateStack = []
    addons = []

    endedText = True
    replacement = True
    hasAddedText = False

    def __init__(self, title, author, documentClass):
        self.documentClass = documentClass
        self.title = title
        self.author = author
        self.filePath = "./output-doc/"+title+".tex"
        self.documentText = ""
        self.replacement = True
        self.inCodeBlock = False

    def addState(self, stateType, innerText, tailText):
        newState = State(stateType, innerText,tailText)
        self.stateStack.append(newState)

        if(stateType == "SECTION"):
            self.startSection()
        elif(stateType == "SUBSECTION"):
            self.startSubSection()
        elif(stateType == "SUBSUBSECTION"):
            self.startSubSubSection()
        elif(stateType == "LITERAL"):
            self.turnOffReplacement()
        elif(stateType == "BOLD"):
            self.startBold()
        elif(stateType == "ITALIC"):
            self.startItalic()
        elif(stateType == "UNDERLINE"):
            self.startUnderline()
        elif(stateType == "UNORDEREDLIST"):
            self.startUnorderedList()
        elif(stateType == "ORDEREDLIST"):
            self.startOrderedList()
        elif(stateType == "ITEM"):
            self.startItem()
        elif(stateType == "CODEBLOCK"):
            self.startCodeBlock()
        elif(stateType == "CENTERED"):
            self.startCentering()
        elif(stateType == "RIGHTALIGNED"):
            self.startRightAlign()
        elif(stateType == "BREAK"):
            self.addBreak()
        elif(stateType == "FIGURE"):
            self.addFigure()
            return

        self.addText(innerText)

    def removeState(self):
        tailText = self.stateStack[-1].tailText
        stateType = self.stateStack[-1].stateType

        if(stateType == "SECTION"):
            self.endSect()
        elif(stateType == "SUBSECTION"):
            self.endSect()
        elif(stateType == "SUBSUBSECTION"):
            self.endSect()
        elif(stateType == "LITERAL"):
            self.turnOnReplacement()
        elif(stateType == "BOLD"):
            self.endFormat()
        elif(stateType == "ITALIC"):
            self.endFormat()
        elif(stateType == "UNDERLINE"):
            self.endFormat()
        elif(stateType == "UNORDEREDLIST"):
            self.endUnorderedList()
        elif(stateType == "ORDEREDLIST"):
            self.endOrderedList()
        elif(stateType == "CODEBLOCK"):
            self.endCodeBlock()
        elif(stateType == "CENTERED"):
            self.endCentering()
        elif(stateType == "RIGHTALIGNED"):
            self.endRightAlign()
        elif(stateType == "TEXT"):
            self.endText()

        self.stateStack.pop()
        self.addText(tailText)

    def addText(self, text):
        if(text!=None):
            if(self.replacement == True and not self.inCodeBlock):
                    text = text.replace('\\', r'\textbackslash ')
                    text = text.replace('$', r'\$ ')
                    text = text.replace('%', r'\% ')
                    text = text.replace('_', r'\_ ')
                    text = text.replace('}', r'\} ')
                    text = text.replace('{', r'\{ ')
                    text = text.replace('&', r'\& ')
                    text = text.replace('#', r'\# ')
                    text = text.replace('~', r'\textasciitilde ')

            text = text.replace(u'\xa0', ' ')
            text = text.encode('ascii', 'ignore')
            text = text.decode()
            self.documentText += text
            self.hasAddedText = True

    def startSection(self):
        self.documentText += r"\section{"

    def startSubSection(self):
        self.documentText += r"\subsection{"
    
    def startSubSubSection(self):
        self.documentText += r"\subsubsection{"

    def endSect(self):
        self.documentText += "}\n"

    def turnOnReplacement(self):
        self.replacement = True

    def turnOffReplacement(self):
        self.replacement = False

    def endText(self):
        if(not self.hasAddedText):
            # if we haven't added text we don't want to add extra new lines
            return

        # we are about to add some number of new line characters so we can
        #   reset our text flag
        self.hasAddedText = False
        if(self.inCodeBlock):
            self.documentText += "\n"
            return
        if(len(self.stateStack) < 1 or self.stateStack[-1].stateType == "TEXT"):
            # to leave a text state, we need to add 2 new lines so that we create
            #  a new paragraph in LaTeX
            self.documentText += "\n\n"
            return
        
        self.documentText += "\n"

    def startBold(self):
        self.documentText += r"\textbf{"
    
    def startItalic(self):
        self.documentText += r"\textit{"
    
    def startUnderline(self):
        self.documentText += r"\underline{"

    def endFormat(self):
        self.documentText += "}"

    def startCodeBlock(self):
        self.documentText += r"\begin{verbatim}" + "\n"
        self.inCodeBlock = True

    def endCodeBlock(self):
        self.documentText += r"\end{verbatim}" + "\n"
        self.inCodeBlock = False

    def startCentering(self):
        self.documentText += r"\begin{center}"+"\n"
    
    def endCentering(self):
        self.documentText += r"\end{center}" + "\n"

    def startRightAlign(self):
        self.documentText += r"\begin{flushright}"+"\n"
    
    def endRightAlign(self):
        self.documentText += r"\end{flushright}" + "\n"

    def addBreak(self):
        self.documentText += "\n"

    def startUnorderedList(self):
        self.documentText += r"\begin{itemize}" + "\n"

    def endUnorderedList(self):
        self.documentText += r"\end{itemize}" + "\n"

    def startOrderedList(self):
        self.documentText += r"\begin{enumerate}" + "\n"

    def endOrderedList(self):
        self.documentText += r"\end{enumerate}" + "\n"
    
    def startItem(self):
        self.documentText += r"\item "

    def addFigure(self):
        fileName = self.stateStack[-1].innerText
        self.documentText += r"\begin{figure}[h!]" + "\n"
        self.documentText += r"\centering" + "\n"
        self.documentText += r"\includegraphics[width=0.8\linewidth]{./figs/" + fileName +"}\n"
        self.documentText += r"\end{figure}" + "\n"

    def addChapter(self, chapter):
        self.documentText += r"\chapter{" + chapter + "}\n"

    def writeToFile(self):
        with open(self.filePath, 'w') as f:
            if(self.documentClass != 'book'):
                f.write(r"\documentclass{"+self.documentClass+"}\n\n")
            else:
                f.write(r"\documentclass[12pt,a4paper]{book}" + "\n\n")
            f.write(r"\usepackage{graphicx}" + "\n\n")
            f.write(r"\title{"+self.title+"}\n")
            f.write(r"\author{"+self.author+"}\n\n")
            f.write(r"\begin{document}"+"\n")
            f.write(r"\maketitle"+"\n")
            if(self.documentClass == 'book'):
                f.write(r"\tableofcontents")
            f.write(self.documentText + "\n")

            if('bib' in self.addons):
                f.write(r"\bibliographystyle{plain}" + "\n")
                f.write(r"\bibliography{" + defs.BIB_FILE_PATH + "}\n")

            f.write(r"\end{document}")

