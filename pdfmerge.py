from PyPDF2 import PdfMerger

merger = PdfMerger()

file = open('config.txt', 'r')
lines = file.readlines()

for line in lines:
    print(line.rstrip())
    merger.append(line.rstrip())

merger.write("mergedPdf.pdf")
merger.close()
file.close()