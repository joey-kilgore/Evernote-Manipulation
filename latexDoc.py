class LatexDoc:
    documentClass = ""
    title = ""
    author = ""
    date = ""
    documentText = ""
    filePath = ""

    endedText = True

    def __init__(self, title, author):
        self.documentClass = "article"
        self.title = title
        self.author = author
        self.filePath = "./output-doc/"+title+".tex"
        self.documentText = ""

    def addSection(self, sectionTitle):
        self.documentText += r"\section{"+sectionTitle+"}\n"

    def addSubSection(self, subSectionTitle):
        self.documentText += r"\subsection{"+subSectionTitle+"}\n"
    
    def addSubSubSection(self, subSubSectionTitle):
        self.documentText += r"\subsubsection{"+subSubSectionTitle+"}\n"

    def addText(self, text):
        if(text!=None):
            self.documentText += text
            self.endedText = False

    def endText(self):
        if(self.endedText == False):
            self.documentText += "\n\n"
            self.endedText == True

    def startBold(self):
        self.documentText += r"\textbf{"
    
    def startItalic(self):
        self.documentText += r"\textit{"
    
    def startUnderline(self):
        self.documentText += r"\underline{"

    def startStrikethrough(self):
        self.documentText += r"\st{"

    def endFormat(self):
        self.documentText += "}"

    def startCentering(self):
        self.documentText += r"\begin{center}"+"\n"
    
    def endCentering(self):
        self.documentText += r"\end{center}" + "\n"

    def startRightAlign(self):
        self.documentText += r"\begin{flushright}"+"\n"
    
    def endRightAlign(self):
        self.documentText += r"\end{flushright}" + "\n"

    def addBreak(self):
        self.documentText += "\n\n"

    def startUnorderedList(self):
        self.documentText += r"\begin{itemize}" + "\n"

    def endUnorderedList(self):
        self.documentText += r"\end{itemize}" + "\n"

    def startOrderedList(self):
        self.documentText += r"\begin{enumerate}" + "\n"

    def endOrderedList(self):
        self.documentText += r"\end{enumerate}" + "\n"
    
    def addItem(self):
        self.documentText += r"\item "

    def addFigure(self, fileName):
        self.documentText += r"\begin{figure}[h!]" + "\n"
        self.documentText += r"\centering" + "\n"
        self.documentText += r"\includegraphics[width=0.8\linewidth]{./figs/" + fileName +"}\n"
        self.documentText += r"\end{figure}" + "\n"


    def writeToFile(self):
        with open(self.filePath, 'w') as f:
            f.write(r"\documentclass{"+self.documentClass+"}\n\n")
            f.write(r"\usepackage{graphicx}" + "\n\n")
            f.write(r"\title{"+self.title+"}\n")
            f.write(r"\author{"+self.author+"}\n\n")
            f.write(r"\begin{document}"+"\n")
            f.write(r"\maketitle"+"\n")
            f.write(self.documentText + "\n")
            f.write(r"\end{document}")

