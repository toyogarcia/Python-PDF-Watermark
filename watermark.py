import PyPDF2
import sys

watermark = PyPDF2.PdfFileReader(open (sys.argv[1],'rb'))
template =  PyPDF2.PdfFileReader(open (sys.argv[2],'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

with open (sys.argv[3],'wb') as file:
    output.write(file)
    



