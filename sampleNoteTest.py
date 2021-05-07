from noteParse import printTree, parseNote, recursivePrintTree, parseNotebook
import xml.etree.ElementTree as ET
import note

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
parsedNote.exportToLatex()
parsedNote.printLatex()

parsedNote = parseNote('./sample-notes/Multi Section.enex')
parsedNote.printBasicStats()
parsedNote.exportToLatex()
parsedNote.printLatex()

parsedNote = parseNote('./sample-notes/Text and Image.enex')
parsedNote.printBasicStats()
parsedNote.exportToLatex()
parsedNote.printLatex()

parsedNote = parseNote('./sample-notes/Note With Link.enex')
parsedNote.printBasicStats()
parsedNote.exportToLatex()
parsedNote.printLatex()

parsedNote = parseNote('./sample-notes/Lists.enex')
parsedNote.printBasicStats()
parsedNote.exportToLatex()
parsedNote.printLatex()


parsedNote = parseNote('./sample-notes/Fun with Formating.enex')
parsedNote.printBasicStats()
parsedNote.exportToLatex()
parsedNote.printLatex()


parsedNote = parseNote('./sample-notes/Code blocks.enex')
parsedNote.printBasicStats()
parsedNote.exportToLatex()
parsedNote.printLatex()


parsedNote = parseNote('./sample-notes/Highlighting.enex')
parsedNote.printBasicStats()
parsedNote.exportToLatex()
parsedNote.printLatex()

parsedNote = parseNote('./sample-notes/Citations.enex')
parsedNote.printBasicStats()
parsedNote.exportToLatex()
parsedNote.printLatex()

parsedBook = parseNotebook('./sample-notes/Test Notes.enex')
parsedBook.exportToLatex()
parsedBook.printLatex()