import pdfkit
import os


class Html2Pdf:
    options = {
        "page-size": "A5",
        "orientation": "landscape",
        "encoding": "UTF-8",
    }

    def __init__(self, html="template/template.html"):
        self.html2pdf = html

    def convert(self, output_name) -> None:
        download_folder = self.get_download_path()
        pdfkit.from_file(
            self.html2pdf, download_folder + f"{output_name}.pdf", options=self.options
        )

    def get_download_path(self):
        return os.path.join(os.path.expanduser("~"), "Downloads/")


if __name__ == "__main__":
    pass
