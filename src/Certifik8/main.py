from src.Certifik8.certificado import Certificados
from tkinter import filedialog
'''from certificado import Certificados'''
import os

def run():
    certificados = Certificados()
    print(
        "Bem-vindo ao Certifik8, gerador de certificados da Semana Universitária da UnB"
    )
    path_tabela = filedialog.askopenfilename()

    if os.path.exists(path_tabela) and os.path.splitext(path_tabela)[1] == ".xlsx":
        certificados.gerarCertificados(path_tabela)
    else:
        print("Tabela não encontrada")