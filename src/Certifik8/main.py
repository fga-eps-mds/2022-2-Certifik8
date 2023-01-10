from src.Certifik8.certificado import Certificados
'''from certificado import Certificados'''
import os

def run():
    certificados = Certificados()

    paths = ['/home/pedro/2022-2-Certifik8/docs/exemplo/exemplo.xlsx',
             '/home/pedro/2022-2-Certifik8/docs/exemplo/exemplo2.xlsx'
    ]

    for path in paths:
        print(
            "Bem-vindo ao Certifik8, gerador de certificados da Semana Universitária da UnB"
        )
        nome_curso = input("Digite o nome do curso:\n")
        carga_horaria = input("Digite a carga horaria:\n")
        nome_professor = input("Digite o nome do professor:\n")
        nome_departamento = input("Digite o nome do departamento:\n")
        data_inicial = input(
            "Digite a data de início do curso(Ex: 08 de Novembro de 2022):\n"
        )
        data_final = input(
            "Digite a data de encerramento do curso(Ex: 17 de Novembro de 2022):\n"
        )

        if os.path.exists(path) and os.path.splitext(path)[1] == ".xlsx":
            certificados.gerarCertificados(
                path,
                nome_curso,
                carga_horaria,
                nome_professor,
                nome_departamento,
                data_inicial,
                data_final,
            )
        else:
            print("Tabela não encontrada")
