from pypdf import PdfWriter
import os

folder = r"E:\REPOSITORY\Journey_of_Learning_Python_Programming\DAY 71"  

merger = PdfWriter()


files = [f for f in os.listdir(folder) if f.endswith(".pdf") and f != "merged-pdf.pdf"]


for pdf in files:
    merger.append(os.path.join(folder, pdf))


merger.write(os.path.join(folder, "merged-pdf.pdf"))
merger.close()

print(f"Done! Merged {len(files)} files.")