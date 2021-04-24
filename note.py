# the Note class contains relevant information for storing
#  data related to evernotes
class Note:
    title = ""
    created = ""
    updated = ""
    author = ""
    contentTree = ""
    resources = ""

    def __init__(self):
        self.title = "new note"

    def printBasicStats(self):
        print("TITLE: "+self.title)
        print("CREATED: "+self.created)
        print("AUTHOR: "+self.author)
        print("DIVS: "+str(len(self.contentTree.findall('div'))))
        print("RESOURCES: "+str(len(self.resources)))