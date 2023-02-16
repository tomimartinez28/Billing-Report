import pdfquery
import pandas as pd

pdf = pdfquery.PDFQuery('27206517382_211_00007_00000012.pdf')
pdf.load()
pdf.tree.write('pdfXML.txt', pretty_print = True)
