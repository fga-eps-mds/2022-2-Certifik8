from src.Certifik8.html2pdf import Html2Pdf
import pandas as pd
import os
from src.Certifik8.data_emissao import DataEmissao
from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <title>Template</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
        main{
            position: relative;
            width: 1096px;
            height: 748px;
            font-family: 'Roboto', sans-serif;
            background-image: url(https://cdn.discordapp.com/attachments/1034883038586351647/1049011662566465546/template.png);
        }
        #texto_principal{
            position: absolute;
            top: 250px;
            left: 148px;
            width: 800px;
            text-align: justify;
            font-size: 18px;
            font-weight: 700;
        
        }
        .nome_participante, .cpf_participante, .nome_evento, .nome_prof, .nome_dep, .cargo_participante, .frequencia_participante{
            text-transform: uppercase;
        }
        #local_data{
            position: absolute;
            top: 400px;
            right: 148px;
            font-size: 22px;
            font-weight: 700;
        }
        #informacoes_adicionais{
            position: absolute;
            top: 470px;
            width: 1096px;
        }
        .texto_adicional{
            margin: 0;
            font-size: 22px;
            text-align: center;
            font-weight: 700;
        }
        p.nao_negrito{
            font-size: 20px;
            font-weight: 400;
        }
    </style>
</head>
<body>
    <main>
        <p id="texto_principal">Certificamos que, <span class="nome_participante"></span>, CPF <span class="cpf_participante"></span>, participou do
            evento de extensão <span class="nome_evento"></span>, com carga horária de <span class="carga_hor"></span>
            hora(s), coordenado pelo(a) Professor(a) <span class="nome_prof"></span>, promovido
            pelo(a) <span class="nome_dep"></span>, na função de <span class="cargo_participante"></span>,
            com frequência <span class="frequencia_participante"></span>%. A atividade foi realizada no período de <span class="data_inicial"></span> a
            <span class="data_final">***</span>.
        </p>
        <p id="local_data">Brasília, <span class="data_emissao"></span></p>
        <div id="informacoes_adicionais">
            <p class="texto_adicional">OLGAMIR AMANCIA FERREIRA</p>
            <p class="texto_adicional nao_negrito">Decana de Extensão</p>
        </div>
    </main>
</body>
</html>
"""

class Certificados:
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
