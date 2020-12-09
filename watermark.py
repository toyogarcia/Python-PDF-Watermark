import PyPDF2
import sys

try:
    if len(sys.argv) < 4:
        print('Wrong number of parameters')
        sys.exit()
        
    watermark = PyPDF2.PdfFileReader(open (sys.argv[1],'rb'))
    template =  PyPDF2.PdfFileReader(open (sys.argv[2],'rb'))
    output = PyPDF2.PdfFileWriter()

    for i in range(template.getNumPages()):
        page = template.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)

    with open (sys.argv[3],'wb') as file:
        output.write(file)

except FileNotFoundError:
    print('Error in parameters')

    



