import xml.etree.ElementTree as ET

def recursivePrintTree(prefix, node):
    print(prefix + node.tag)
    for child in node:
        recursivePrintTree(prefix+"  ", child)

def printTree(fileName):
    tree = ET.parse(fileName)
    root = tree.getroot()
    print(fileName)
    recursivePrintTree("", root)

printTree('./sample-notes/Just Text.enex')
printTree('./sample-notes/Text and Image.enex')