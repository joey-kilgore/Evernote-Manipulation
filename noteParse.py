import xml.etree.ElementTree as ET

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
print(contentParse)