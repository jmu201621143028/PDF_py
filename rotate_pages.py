import PyPDF2  #pip install PyPDF2
import argparse
import os
import random


parser = argparse.ArgumentParser()
parser.add_argument('name')
parser.add_argument('rotation')
parser.add_argument("progress")
args = parser.parse_args()
name = args.name
rotation = int(args.rotation)
if rotation % 90 != 0:
	exit(-1)

def writeprogress(progress):
	fpg = open(args.progress, 'w')
	fpg.write('progress={}\n'.format(progress))
	fpg.close()

newFileName = ''.join(args.name.split('.')[:-1]) + "_rotate.pdf"
if os.path.exists(newFileName):
	newFileName = ''.join(args.name.split('.')[:-1]) + '_rotate_' + ''.join(random.sample('1234567890', 5)) + ".pdf"

def PDFrotate(origFileName, newFileName, rotation):
	pdfFile = open(origFileName, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFile)
	pdfWriter = PyPDF2.PdfFileWriter()
	for page in range(pdfReader.numPages):
		pageObj = pdfReader.getPage(page)
		pageObj.rotateClockwise(rotation)
		pdfWriter.addPage(pageObj)
		writeprogress(page/pdfReader.numPages * 100)
	newFile = open(newFileName, 'wb')
	pdfWriter.write(newFile)
	pdfFile.close()
	newFile.close()
	writeprogress(100)
PDFrotate(args.name, newFileName, rotation)

