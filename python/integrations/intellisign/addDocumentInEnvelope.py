import requests

"""
    Adiciona um documento em um envelope na Intellisign.
    Parâmetros:
        access_token_intellisign (str): Token de acesso para autenticação.
        envelope_id (str): ID do envelope onde o documento será adicionado.
        file_bytes (bytes): Conteúdo do arquivo em bytes.
        document_name (str): Nome do documento a ser adicionado.
    Retorna:
        dict: Informações do documento adicionado ou None em caso de falha.
        O dicionário contém links de exibição e download do documento.
"""


def add_document_in_envelope(
    access_token_intellisign, envelope_id, file_bytes, document_name
):
    try:
        if not file_bytes:
            print("Não foi possível baixar o documento do document_url")
            return None

        url = f"https://api.intellisign.com/v1/envelopes/{envelope_id}/documents"
        files = {
            "file": (
                f"{document_name}.pdf",
                file_bytes,
                "application/pdf",
            )
        }
        headers = {
            "Authorization": f"Bearer {access_token_intellisign}",
            "Accept": "application/json",
        }

        response = requests.post(url, files=files, headers=headers, timeout=60)

        if response.status_code in (200, 201):
            data = response.json()
            print("Documento adicionado com sucesso:", data)
            return {"document_link": data}

        print(
            f"Resposta inesperada do Intellisign: {response.status_code} - {response.text}"
        )
        return None

    except Exception as e:
        print(f"Erro ao adicionar documento no envelope: {e}")
        return None
