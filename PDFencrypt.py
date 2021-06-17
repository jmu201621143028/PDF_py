from PyPDF2 import PdfFileWriter, PdfFileReader
import argparse
import os
import random

parser = argparse.ArgumentParser()
parser.add_argument("name")
parser.add_argument("password")
parser.add_argument("progress")
args = parser.parse_args()

def writeprogress(progress):
	fpg = open(args.progress, 'w')
	fpg.write('progress={}\n'.format(progress))
	fpg.close()

out = PdfFileWriter()
file = PdfFileReader(args.name)
num = file.numPages
for idx in range(num):
	page = file.getPage(idx)
	out.addPage(page)
	writeprogress(idx / num * 100)
password = args.password
out.encrypt(password)

encrypt_name = ''.join(args.name.split('.')[:-1]) + "_encrypted.pdf"
if os.path.exists(encrypt_name):
	encrypt_name = ''.join(args.name.split('.')[:-1]) + '_encrypted_' + ''.join(random.sample('123', 5)) + ".pdf"

with open(encrypt_name, "wb") as f:
	out.write(f)
writeprogress(100)

