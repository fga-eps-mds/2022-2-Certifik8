from pathlib import Path
import pdfkit
import os
#Funcao para converter html para pdf
def convert_html_to_pdf(html_page, save_name):
    pdfkit.from_file(html_page, save_name)

#Funcao que pega o caminho para pasta download do sistema, podendo ser tanto Windows quanto Unix.
def get_download_path():
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'Downloads/')

download_folder = get_download_path()
convert_html_to_pdf('2022-2-Squad08/certificado.html', download_folder + 'file.pdf')

