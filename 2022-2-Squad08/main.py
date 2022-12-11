from generator.certificado import Certificados
import os


if __name__ == "__main__":
    certificados = Certificados()
    print(
        "Bem-vindo ao Certifik8, gerador de certificados da Semana Universitária da UnB"
    )
    path_tabela = input("Digite o endereço da tabela:\n")
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

    if os.path.exists(path_tabela) and os.path.splitext(path_tabela)[1] == ".xlsx":
        certificados.gerarCertificados(
            path_tabela,
            nome_curso,
            carga_horaria,
            nome_professor,
            nome_departamento,
            data_inicial,
            data_final,
        )
    else:
        print("Tabela não encontrada")
