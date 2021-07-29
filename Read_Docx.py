#! python3

# p. 365

import docx


def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

# p. 366

# To add a double space between paragraphs, change the join() call code from Read_Docx to this:

# return '\n\n'.join(fullText)
