from converter.html2pdf import Html2Pdf
import pandas as pd
import os
from utils.data_emissao import DataEmissao
from bs4 import BeautifulSoup


class Certificados:
    html_template = "template/template.html"
    DataEmissao = DataEmissao()

    def xlsx_content(self, path):
        data_frame = pd.read_excel(path)
        return data_frame

    def gerarCertificados(
        self,
        filename,
        nome_evento,
        carga_hor,
        nome_prof,
        nome_dep,
        data_inicial,
        data_final,
    ):
        try:
            df = self.xlsx_content(filename)
        except:
            pass

        data_emissao = self.DataEmissao.getDataPorExtenso()
        for i in df.index:
            html_doc = open(self.html_template).read()
            soup = BeautifulSoup(html_doc, "html.parser")
            soup.find("span", class_="nome_participante").replace_with(df["Nome"][i])
            soup.find("span", class_="cpf_participante").replace_with(df["cpf"][i])
            soup.find("span", class_="nome_evento").replace_with(nome_evento)
            soup.find("span", class_="carga_hor").replace_with(carga_hor)
            soup.find("span", class_="nome_prof").replace_with(nome_prof)
            soup.find("span", class_="nome_dep").replace_with(nome_dep)
            soup.find("span", class_="cargo_participante").replace_with(df["Função"][i])
            soup.find("span", class_="frequencia_participante").replace_with(
                str(df["Frequência"][i])
            )
            soup.find("span", class_="data_inicial").replace_with(data_inicial)
            soup.find("span", class_="data_final").replace_with(data_final)
            soup.find("span", class_="data_emissao").replace_with(data_emissao)
            with open(df["Nome"][i] + ".html", "w") as file:
                file.writelines(soup.prettify())
            Html2Pdfs = Html2Pdf(html=df["Nome"][i] + ".html")
            Html2Pdfs.convert(df["Nome"][i])
            os.remove(df["Nome"][i] + ".html")


if __name__ == "__main__":
    pass
