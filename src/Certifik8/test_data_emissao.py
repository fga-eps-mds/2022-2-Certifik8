from data_emissao import DataEmissao
import re


def validar_data(data):
    regex = r"^(0[1-9]|[12]\d|3[01])\sde\s(Janeiro|Fevereiro|Março|Abril|Maio|Junho|Julho|Agosto|Setembro|Outubro|Novembro|Dezembro)\sde\s(20)\d{2}$"
    if re.match(regex, data):
        return True
    else:
        return False

def test_data_emissao():
    data = DataEmissao()
    assert validar_data(data.getDataPorExtenso())


if __name__ == "__main__":
    pass
