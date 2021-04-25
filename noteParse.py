# noteParse contains methods that are used in breaking
#  apart evernote .enex files and giving them a parsed
#  and more accessible format

import xml.etree.ElementTree as ET
import note
import book
import os

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

def parseNotebook(fileName):
    tree = ET.parse(fileName)
    enExport = tree.getroot()
    noteTree = enExport[0]

    bookObj = book.Book()
    bookObj.title = os.path.splitext(os.path.basename(fileName))[0]

    for noteTree in enExport.findall('note'):
        title = noteTree.findall('title')[0].text
        try:
            author = noteTree.findall('note-attributes')[0].findall('author')[0].text
        except:
            author = "Joey Kilgore"
        created = noteTree.findall('created')[0].text
        updated = noteTree.findall('updated')[0].text
        
        contentStr = noteTree.findall('content')[0].text
        contentStr = contentStr.replace("""<?xml version="1.0" encoding="UTF-8" standalone="no"?>""", "")
        contentStr = contentStr.replace("""<!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">""","")
        contentStr = contentStr.replace("&nbsp;", "")
        contentTree = ET.fromstring(contentStr.strip())
        
        resourceListTree = noteTree.findall('resource')

        noteObj = note.Note()
        noteObj.author = author
        noteObj.title = title
        noteObj.created = created
        noteObj.updated = updated
        noteObj.contentTree = contentTree
        noteObj.resources = resourceListTree

        bookObj.notes.append(noteObj)
        bookObj.author = noteObj.author
    
    return bookObj

def recursivePrintTree(prefix, node):
    print(prefix + "|-->" + node.tag)
    for child in node:
        recursivePrintTree(prefix+"    ", child)

def printTree(fileName):
    tree = ET.parse(fileName)
    root = tree.getroot()
    print(fileName)
    recursivePrintTree("", root)