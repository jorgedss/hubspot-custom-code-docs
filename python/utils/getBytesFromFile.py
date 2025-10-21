import requests

"""
    Baixa um arquivo de uma URL e retorna seu conteúdo em bytes.
    Parâmetros:
        url (str): A URL do arquivo a ser baixado.
    Retorna:
        bytes: Conteúdo do arquivo em bytes ou None em caso de falha.
"""


def download_file_to_bytes(url):
    try:
        response = requests.get(url, timeout=20)
        response.raise_for_status()
        return response.content
    except Exception as e:
        print(f"Erro ao baixar o arquivo: {e}")
        return None
