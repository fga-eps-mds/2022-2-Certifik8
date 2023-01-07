from data_emissao import DataEmissao
import requests
import json


def get_data_api():
    meses = (
        "Janeiro",
        "Fevereiro",
        "Março",
        "Abril",
        "Mail",
        "Junho",
        "Julho",
        "Agosto",
        "Setembro",
        "Outubro",
        "Novembro",
        "Dezembro",
    )

    response = json.loads(requests.get("http://worldtimeapi.org/api/timezone/America/Sao_Paulo").content)

    data = response['datetime'][0:10]
    data = data.split('-')
    dia = data[2]
    mes = int(data[1])
    mes = meses[mes-1]
    ano = int(data[0])

    return f"{dia} de {mes} de {ano}"


def test_data_emissao():
    data = DataEmissao()
    assert data.getDataPorExtenso() == get_data_api()
