from PyPDF2 import PdfMerger

merger = PdfMerger()

for pdf in ["enter file path", "enter file path"]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
