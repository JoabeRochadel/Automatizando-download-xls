import requests
import os
import datetime

# current_time = datetime.datetime.now()
# print(current_time.month,current_time.day, sep = '-')

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
    # baixar_arquivo('http://www.fenabrave.org.br/ftp/abralib/Emplacamentos_Mensal_Segmentos_S_Fabricante.xls',
    #                'fenabrave_mensal.csv')
    OUTPUT_DIR = '//192.168.5.175/librelato/MKT_Estrategico/. 2020/Joabe/base de dados consolidada joabe DB/Python/Nova pasta'

    for i in range(1, 1):
        nome_arquivo = os.path.join(OUTPUT_DIR, 'Extraoficial{}.xls'.format(i))
        baixar_arquivo(BASE_URL.format(i), nome_arquivo)
