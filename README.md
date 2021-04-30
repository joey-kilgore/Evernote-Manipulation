# Evernote-Manipulation
Manipulate Evernotes into other formats. Particularly for use in turning .enex files into .tex files.  

## Convert from .enex to .tex  
For an individual note
```
python enToLatex.py -n "path/to/file.enex"
```

Or you can convert an entire notebook into a LaTeX book
```
python enToLatex.py -b "path/to/file.enex"
```

A .tex file should be generated into an output-docs folder (which you may need to create) and a subsequent figs folder within it for all the figures.

## What is supported
Currently there is support for the following:
- Standard text (with automatic character replacement for .tex)
- Headings (all three sizes) are converted to sections, subsections, subsubsections
- italics, bold, underline
- images
- bulleted and numbered lists
- code blocks
- links (gets the web address and puts that in the .tex)
- LaTeX syntax (highlight text that should be taken literally to the .tex file with no character replacement)
- Notebooks converted to books (each note is a chapter in order created)
