class LatexDoc:
    documentClass = ""
    title = ""
    author = ""
    date = ""
    documentText = ""
    filePath = ""

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

    def addBreak(self):
        self.documentText += "\n\n"

    def writeToFile(self):
        with open(self.filePath, 'w') as f:
            f.write(r"\documentclass{"+self.documentClass+"}\n\n")
            f.write(r"\title{"+self.title+"}\n")
            f.write(r"\author{"+self.author+"}\n\n")
            f.write(r"\begin{document}"+"\n")
            f.write(r"\maketitle"+"\n")
            f.write(self.documentText + "\n")
            f.write(r"\end{document}")

