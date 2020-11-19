import requests
import os
import datetime

current_time = datetime.datetime.now()
month = (current_time.month)
day=(current_time.day)
a = (f'{month}-{day}')


def baixar_arquivo(url, endereco):
    resposta = requests.get(url)
    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
            novo_arquivo.write(resposta.content)
        print('Donwload finalizado. Salvo em: {}'.format(endereco))
    else:
        resposta.raise_for_status()

if __name__ == "__main__":
    BASE_URL = ('http://www.fenabrave.org.br/ftp/abralib/Emplacamentos_Diario_Segmentos_S_Fabricante.xls')
    BASE_URL2 = ('http://www.fenabrave.org.br/ftp/abralib/Emplacamentos_Mensal_Segmentos_S_Fabricante.xls')

    OUTPUT_DIR = '//192.168.5.175/librelato/MKT_Estrategico/. 2020/Joabe/base de dados consolidada joabe DB/Python/Nova pasta'

    for i in range(1, 2):
        month = (current_time.month)
        day = (current_time.day-1)
        month_day = (f'{month}-{day}')
        nome_arquivo_extraoficial = os.path.join(OUTPUT_DIR, 'Extraoficial{}.xls'.format(month_day))
        nome_arquivo_oficial = os.path.join(OUTPUT_DIR, 'Oficial{}.xls'.format(month_day))
        baixar_arquivo(BASE_URL.format(i), nome_arquivo_extraoficial)
        baixar_arquivo(BASE_URL2.format(i), nome_arquivo_oficial)
