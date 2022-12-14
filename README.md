# 2022-2-Certifik8

<a name="readme-top"></a>

<div align="center">

[![Contributors](https://img.shields.io/github/contributors/fga-eps-mds/2022-2-Squad08.svg?style=for-the-badge&color=e703f7)](https://github.com/fga-eps-mds/2022-2-Squad08/graphs/contributors)
[![Issues](https://img.shields.io/github/issues/fga-eps-mds/2022-2-Squad08.svg?style=for-the-badge&color=e703f7)](https://github.com/fga-eps-mds/2022-2-Squad08/issues)
[![MIT License](https://img.shields.io/github/license/fga-eps-mds/2022-2-Squad08.svg?style=for-the-badge&color=e703f7)](https://github.com/fga-eps-mds/2022-2-Squad08/blob/main/LICENSE)

</div>

<br />
<div align="center">
  <a href="https://github.com/fga-eps-mds/2022-2-Squad08">
    <img src="https://github.com/fga-eps-mds/2022-2-Certifik8/blob/main/docs/imagens/logo.png" width="300" height="300">
  </a>
  
  <h3 align="center">Certifik8</h3>

  <p align="center">
   Gerador Automatico de Certificados 
    <br />
    <a href="docs">Documentos</a>
    -
    <a href="https://github.com/fga-eps-mds/2022-2-Squad08/blob/main/SECURITY.md">Reportar Bug</a>
    -
    <a href="https://github.com/fga-eps-mds/2022-2-Squad08/issues">Recomendar Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Conteúdo</summary>
  <ol>
    <li>
      <a href="#Sobre-o-projeto">📝 Sobre o projeto</a>
      <ul>
        <li><a href="#Tecnologias">💻 Tecnologias</a></li>
      </ul>
    </li>
    <li><a href="#Funcionalidade">🤖 Funcionalidade</a></li>
    <li><a href="#Requisitos">❗ Requisitos</a></li>
    <li><a href="#Como-rodar">🛞 Como rodar</a></li>
    <li><a href="#Devenvolvedores">👨‍💻 Desenvolvedores</a></li>
  </ol>
</details>

## 📝 Sobre o projeto

Certifik8 é um gerador de certificados automático criado em Python. O projeto busca facilitar a geração massiva de documentos a serem emitidos após algum evento. 

## 💻 Tecnologias

#### Tecnologias utilizadas neste projeto:

<p align="center">
	<a href="https://skillicons.dev">
		<img src="https://skillicons.dev/icons?i=python,html,css"/>
	</a>
</p>

## 🤖 Funcionalidade
O Certifik8 necessita de duas entradas de dados, uma tabela (Excel), no formato XLSX, e dados gerais sobre o evento. Para cada conjunto de informações um documento com um modelo já preestabelecido é gerado. Os certificados em formato PDF são salvos diretamente na pasta Downloads.

<div align="center">
  <a href="https://github.com/fga-eps-mds/2022-2-Certifik8/blob/main/docs/exemplo/Melissa%20Ribeiro%20Araujo.png">
    <img src="https://github.com/fga-eps-mds/2022-2-Certifik8/blob/main/docs/exemplo/Melissa%20Ribeiro%20Araujo.png" width="413" height="291">
  </a>
</div>

## ❗ Requisitos
O Certifik8 só funciona em sistemas operacionais Linux. 

Testado no:
- Linux Mint 21
- Ubuntu 22.04.01

<div align="center">

![LinuxMint](https://img.shields.io/badge/Linux_Mint-87CF3E?style=for-the-badge&logo=linux-mint&logoColor=black)

![Ubuntu](https://img.shields.io/static/v1?style=for-the-badge&message=Ubuntu&color=E95420&logo=Ubuntu&logoColor=FFFFFF&label=)

</div>



**Para conseguir executá-lo, o usuário precisa instalar:**
  - **Python3 e Pip**
    ```
    sudo apt install python3 && sudo apt install python3-pip
    ```
 
  - **As bibliotecas pdfkit, BeautifulSoup e Pandas**
    ```
    pip install pdfkit
    ```
    ```
    pip install beautifulsoup4
    ```
    ```
    pip install pandas
    ```

  - **Instalar a ferramenta wkhtmltopdf**
    ```
    sudo apt install wkhtmltopdf
    ```

## 🛞 Como rodar
### **- 👩‍🦰 Usuário**
1. **Instalando o Certifik8:**
```
pip install -i https://test.pypi.org/simple/ Certifik8==0.0.2
```

2. **Digite o comando para obter o endereço da biblioteca:**
 ```
 pip show Certifik8 
 ```
<div align="center">
<img src="https://github.com/fga-eps-mds/2022-2-Certifik8/blob/main/docs/imagens/pip-show.png" width="500" height="300">

Copie o endereço após a "Location", marcado de vermelho na imagem.
</div>

3. **Rodando a aplicação:**
 ```
 python3 {endereço_biblioteca}/Certifik8/main.py
 ```
<div align="center">
<img src="https://github.com/fga-eps-mds/2022-2-Certifik8/blob/main/docs/imagens/path-image.png" width="762" height="95">

Substitua a chave {endereço_biblioteca} pelo endereço copiado no passo 2.
</div>

4. **Insira os dados conforme pedido:**

* O endereço da tabela deve ser absoluto.

* Estrutura da tabela Excel ([Exemplo](docs/exemplo/exemplo.xlsx)): 
  - Obs: a tabela deve seguir essa estrutura obrigatoriamente.
    | 1  | Nome | cpf | Função | Frequência |
    |---|------|-----|--------|------------|
    | 2 | Samuel Barbosa Alves | 729.334.326-41 | PARTICIPANTE | 100 |
    | 3 | Melissa Ribeiro Araujo | 201.544.482-30 | MONITOR | 97 |
    | 4 | Gabrielly Rodrigues Castro | 451.016.912-40 | PARTICIPANTE | 80 |
    | ... | ... | ... | ... | ... |
  

<div align="center">

*Demonstração de funcionalidade.*

<img src="https://github.com/fga-eps-mds/2022-2-Certifik8/blob/main/docs/imagens/demonstracao.png" width="500" height="300">

</div>

### **- 🧙🏼‍♀️ Desenvolvimento local**
1. **Clone o repositório**
```
git clone https://github.com/fga-eps-mds/2022-2-Certifik8.git
```

2. **Rode os comando:**

```
sudo docker build -t squad08
```

```
docker run --name cont_squad08 -it squad08
```


## 👨‍💻 Desenvolvedores

<center>
<table style="margin-left: auto; margin-right: auto;">
    <tr>
        <td align="center">
            <a href="https://github.com/PedroSampaioDias">
                <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/90795603?v=4" width="150px;"/>
                <h5 class="text-center">Pedro Sampaio</h5>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/phmelosilva">
                <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/88786258?v=4" width="150px;"/>
                <h5 class="text-center">Pedro Henrique</h5>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/Victor-oss">
                <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/55855365?v=4" width="150px;"/>
                <h5 class="text-center">Victório Lazaro</h5>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/daniel-de-sousa">
                <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/95941136?v=4" width="150px;"/>
                <h5 class="text-center">Daniel Sousa</h5>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/Leanddro13">
                <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/86811628?v=4" width="150px;"/>
                <h5 class="text-center">Leandro Silva</h5>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/BlimblimCFT">
                <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/12275797?v=4" width="150px;"/>
                <h5 class="text-center">Geovane Freitas</h5>
            </a>
        </td>
</table>
</center>