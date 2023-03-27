import os
from PyPDF2 import PdfReader, PdfMerger

# Get a list of all PDF files in the current directory
pdfs = [filename for filename in os.listdir() if filename.endswith('.pdf')]

# Create a PdfMerger object
merger = PdfMerger()

# Append each PDF to the merger object
for pdf in pdfs:
    with open(pdf, 'rb') as infile:
        merger.append(PdfReader(infile))

# Write the merged PDF to a file named "merged.pdf"
with open('merged.pdf', 'wb') as outfile:
    merger.write(outfile)
