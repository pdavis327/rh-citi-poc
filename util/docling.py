from docling.document_converter import DocumentConverter


class PDFConverter:
    def __init__(self):
        self.doc_converter = DocumentConverter()

    def convert_pdf(self, in_path: str, output_path: str) -> None:
        """
        Convert PDFs to Markdown format and save to specified directory.

        Args:
            input_path (str): Directory with PDF files.
            output_path (str): Directory for converted Markdown files.

        Return:
            None
        """
        for i in in_path:
            conv_result = self.doc_converter.convert(i)
            with open(f"{output_path}/{conv_result.input.file.stem}.md", "w") as f:
                f.write(conv_result.document.export_to_markdown())
