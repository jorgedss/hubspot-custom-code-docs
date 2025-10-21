import requests


def set_recipient_in_envelope(
    access_token_intellisign, envelope_id, recipient_email, recipient_name
):

    try:
        url = f"https://api.intellisign.com/v1/envelopes/{envelope_id}/recipients"
        payload = {
            "type": "signer",
            "signature_type": "simple",
            "addressees": [
                {
                    "via": "email",
                    "value": recipient_email,
                    "name": recipient_name,
                }
            ],
        }
        headers = {
            "Authorization": f"Bearer {access_token_intellisign}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code in (200, 201):
            data = response.json()
            print("Destinatário adicionado com sucesso:", data)
            return {
                "outputFields": {
                    "recipient_name": recipient_name,
                    "recipient_email": recipient_email,
                }
            }
        elif response.status_code == 422:
            raise Exception("Destinatário já existe no envelope.")
        else:
            raise Exception(
                f"Resposta inesperada do Intellisign: {response.status_code} - {response.text}"
            )
    except Exception as e:
        print(f"Erro ao adicionar destinatário no envelope: {e}")
        raise
