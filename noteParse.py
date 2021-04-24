import xml.etree.ElementTree as ET
import note

def parseNote(fileName):
    tree = ET.parse(fileName)
    enExport = tree.getroot()
    noteTree = enExport[0]
    title = noteTree.findall('title')[0].text
    author = noteTree.findall('note-attributes')[0].findall('author')[0].text
    created = noteTree.findall('created')[0].text
    updated = noteTree.findall('updated')[0].text
    
    contentStr = noteTree.findall('content')[0].text
    contentStr = contentStr.replace("""<?xml version="1.0" encoding="UTF-8" standalone="no"?>""", "")
    contentStr = contentStr.replace("""<!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">""","")
    contentTree = ET.fromstring(contentStr)
    
    resourceListTree = noteTree.findall('resource')

    noteObj = note.Note()
    noteObj.author = author
    noteObj.title = title
    noteObj.created = created
    noteObj.updated = updated
    noteObj.contentTree = contentTree
    noteObj.resources = resourceListTree

    return noteObj


def recursivePrintTree(prefix, node):
    print(prefix + "|-->" + node.tag)
    for child in node:
        recursivePrintTree(prefix+"    ", child)

def printTree(fileName):
    tree = ET.parse(fileName)
    root = tree.getroot()
    print(fileName)
    recursivePrintTree("", root)

printTree('./sample-notes/Just Text.enex')
printTree('./sample-notes/Text and Image.enex')

contentParse = ET.fromstring("""<en-note>
        <div>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the 
        industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and 
        scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into 
        electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of 
        Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like 
        Aldus PageMaker including versions of Lorem Ipsum.</div>
      </en-note>""")
recursivePrintTree("",contentParse)

parsedNote = parseNote('./sample-notes/Just Text.enex')
parsedNote.printBasicStats()