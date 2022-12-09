from pathlib import Path
import pdfkit
import os


class Html2Pdf:
    """
    Classe para fazer a conversao de html para pdf

    Returns:
        _type_: _description_
    """
    
    options = {
        "page-size": "A5",
        "orientation": "landscape",
        "encoding": "UTF-8",
    }
    """
    Options para configuração do pdf
    
    :param page-size: define o tamanho da pagina
    :param orientation: define a orientacao da pagina
    :param encoding: (opcional) define a formatação do teclado
    
    Returns: None
    """
    
    def __init__(self, html="2022-2-Squad08/template.html"):
        self.html2pdf = html

    def convert(self) -> None: 
        download_folder = self.get_download_path()
        pdfkit.from_file(self.html2pdf, download_folder + "certificado.pdf", options=self.options)

    # Funcao que pega o caminho para pasta download do sistema.
    def get_download_path(self):
        if os.name == "nt":
            import winreg

            sub_key = (
                r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"
            )
            downloads_guid = "{374DE290-123F-4565-9164-39C4925E467B}"
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
                location = winreg.QueryValueEx(key, downloads_guid)[0]
            return location
        else:
            return os.path.join(os.path.expanduser("~"), "Downloads/")


if __name__ == "__main__":
    Html2Pdfs = Html2Pdf()
    Html2Pdfs.convert()
