import requests

"""
    Cria um envelope na Intellisign.
    Parâmetros:
        access_token_intellisign (str): Token de acesso para autenticação.
        title (str): Título do envelope.
        subject (str): Assunto do envelope.
        message (str): Mensagem do envelope.
    Retorna:
        str: ID do envelope criado ou None em caso de falha.
"""


def create_envelope(access_token_intellisign, title, subject, message):
    try:
        url = "https://api.intellisign.com/v1/envelopes"
        payload = {
            "title": title,
            "subject": subject,
            "message": message,
        }
        headers = {
            "Authorization": f"Bearer {access_token_intellisign}",
            "Content-Type": "application/json",
        }
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code in (200, 201):
            return response.json().get("id")
        return None
    except Exception as e:
        print(f"Erro ao criar envelope: {e}")
        return None
