from pathlib import Path
import pdfkit
import os
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date


class DataEmissao:
    
    def __init__(self):
        self.meses = (
            'Janeiro',
            'Fevereiro',
            'Março',
            'Abril',
            'Mail',
            'Junho',
            'Julho',
            'Agosto',
            'Setembro',
            'Outubro',
            'Novembro',
            'Dezembro',
        )

    def getDataPorExtenso(self) -> str:
        dia = date.today().strftime('%d')
        mes = int(date.today().strftime('%m'))-1
        ano = date.today().strftime('%Y')
        return f'{dia} de {self.meses[mes]} de {ano}'

    def printDataPorExtensoDebuger(self):
        print(self.getDataPorExtenso())

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
    
    def __init__(self, html="template.html"):
        self.html2pdf = html

    def convert(self, output_name) -> None: 
        download_folder = self.get_download_path()
        pdfkit.from_file(self.html2pdf, download_folder + f"{output_name}.pdf", options=self.options)

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

class Certificados:
    html_template = 'template.html'
    DataEmissao = DataEmissao()

    def get_full_path(self, filename):
        pre = os.path.dirname(os.path.realpath(__file__))
        return pre + "/" + filename

    def xlsx_content(self, path):
        data_frame = pd.read_excel(path)
        return data_frame

    def gerarCertificados(self, 
                filename, 
                nome_evento, 
                carga_hor,
                nome_prof,
                nome_dep,
                data_inicial,
                data_final
                ):
        try:
            df = self.xlsx_content(filename)
        except:
            df = self.xlsx_content(self.get_full_path(filename))

        data_emissao = self.DataEmissao.getDataPorExtenso()
        for i in df.index:
            html_doc = open(self.html_template).read()
            soup = BeautifulSoup(html_doc, 'html.parser')
            soup.find("span", class_="nome_participante").replace_with(df['Nome'][i])
            soup.find("span", class_="cpf_participante").replace_with(df['cpf'][i])
            soup.find("span", class_="nome_evento").replace_with(nome_evento)
            soup.find("span", class_="carga_hor").replace_with(carga_hor)
            soup.find("span", class_="nome_prof").replace_with(nome_prof)
            soup.find("span", class_="nome_dep").replace_with(nome_dep)
            soup.find("span", class_="cargo_participante").replace_with(df['Função'][i])
            soup.find("span", class_="frequencia_participante").replace_with(str(df['Frequência'][i]))
            soup.find("span", class_="data_inicial").replace_with(data_inicial) 
            soup.find("span", class_="data_final").replace_with(data_final) 
            soup.find("span", class_="data_emissao").replace_with(data_emissao) 
            with open(df['Nome'][i] + '.html', 'w') as file:
                file.writelines(soup.prettify())
            Html2Pdfs = Html2Pdf(html=df['Nome'][i]+'.html')
            Html2Pdfs.convert(df['Nome'][i])
            os.remove(df['Nome'][i]+'.html')

'''
filename, 
                nome_evento, 
                carga_hor,
                nome_prof,
                data_inicial,
                data_final
'''
if __name__ == "__main__":
    certificados = Certificados()
    certificados.gerarCertificados("teste.xlsx", "Curso Básico Python", "10", "Bernardini Glauco", "Departamento de Computação", "08 de Novembro de 2022", "17 de Novembro de 2022")