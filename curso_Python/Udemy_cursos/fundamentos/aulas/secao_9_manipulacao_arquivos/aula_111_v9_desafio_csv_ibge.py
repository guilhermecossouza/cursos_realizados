import csv
# urllib vai abrir qualquer coisa da web ex: site arquivos e etc....
import urllib.request


def abrindo_lendo_arquivo(url=""):
    if url != "":
        with urllib.request.urlopen(url) as entrada:  # abrindo o arquivo
            print("baixando o arquivo.....")
            # lendo o arquivo e decodificando a escrita do mesmo
            dados = entrada.read().decode("latin1")
            print("download completo....")
            # csv.reader -> vai ler cada ula linha | dados.splitlines() vai tratar as virgulas do arquivo
            for cidade in csv.reader(dados.splitlines()):
                print(f"{cidade[8]}: {cidade[3]}")
    else:
        pass


if __name__ == "__main__":
    url_download = r"http://files.cod3r.com.br/curso-python/desafio-ibge.csv"
    abrindo_lendo_arquivo(url=url_download)
