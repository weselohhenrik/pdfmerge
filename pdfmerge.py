from PyPDF2 import PdfMerger
import argparse
from util import check_pdf, check_txt

parser = argparse.ArgumentParser(description= 'merge pdf files')
parser.add_argument('-o',metavar='Output', type=str, help='set the name of output file', default='output.pdf')
parser.add_argument('-c', metavar='Config file', type=str, help='set the name of config file', default='config.txt')

args = parser.parse_args()
configname = check_txt(args.c)
output = check_pdf(args.o)

#print(output)
#print(configname)

merger = PdfMerger()

file = open(configname, 'r')
lines = file.readlines()

for line in lines:
    #print(line.rstrip())
    merger.append(line.rstrip())

merger.write(output)
merger.close()
file.close()
