from datetime import date


class DataEmissao:
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

    def getDataPorExtenso(self) -> str:
        dia = date.today().strftime("%d")
        mes = int(date.today().strftime("%m")) - 1
        ano = date.today().strftime("%Y")
        return f"{dia} de {self.meses[mes]} de {ano}"

    def printDataPorExtensoDebuger(self):
        print(self.getDataPorExtenso())


if __name__ == "__main__":
    pass
