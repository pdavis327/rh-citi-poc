from util import docling
import glob

input_path = "./assets/inputs"
out_path = "./assets/outputs"

input_pdfs = glob.glob(f"{input_path}/*.pdf")

if __name__ == "__main__":
    converter = docling.PDFConverter()
    converter.convert_pdf(input_pdfs, out_path)
