import sys
from noteParse import printTree, parseNote, recursivePrintTree, parseNotebook
import xml.etree.ElementTree as ET
import note

def main():
    if('-h' in sys.argv[1]):
        print('convert evernote note (-n) or notebook (-b)')
        print('-n <pathToEvernote.enex>')
        print('-b <pathToEvernote.enex>')
        return

    if(len(sys.argv) == 3):
        if('-n' == sys.argv[1]):
            parsedNote = parseNote(sys.argv[2])
            parsedNote.printBasicStats()
            parsedNote.exportToLatex()
            parsedNote.printLatex()
        if('-b' == sys.argv[1]):
            print('making a notebook')
            parsedBook = parseNotebook(sys.argv[2])
            parsedBook.exportToLatex()
            parsedBook.printLatex()

if __name__ == '__main__':
    main()