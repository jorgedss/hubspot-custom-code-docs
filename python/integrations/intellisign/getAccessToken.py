import requests

"""
    Obtém um token de acesso da Intellisign usando as credenciais do cliente.
    Parâmetros:
        intellisign_client_id (str): ID do cliente Intellisign.
        intellisign_client_secret (str): Segredo do cliente Intellisign.
    Retorna:
        str: Token de acesso obtido ou None em caso de falha.
"""


def get_access_token(intellisign_client_id, intellisign_client_secret):

    try:
        url = "https://api.intellisign.com/oauth/token"
        payload = {
            "grant_type": "client_credentials",
            "client_id": intellisign_client_id,
            "client_secret": intellisign_client_secret,
            "scope": "*",
        }
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            return response.json().get("access_token")
        return None

    except Exception as e:
        print(f"Erro ao obter access token: {e}")
        return None
