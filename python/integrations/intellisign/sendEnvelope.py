import requests


def send_envelope(
    access_token_intellisign, envelope_id, recipient_email, recipient_name
):

    try:
        url = f"https://api.intellisign.com/v1/envelopes/{envelope_id}/send"
        headers = {
            "Authorization": f"Bearer {access_token_intellisign}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        payload = {"name": recipient_name, "value": recipient_email}
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code in (200, 201):
            data = response.json()
            print("Envelope enviado com sucesso:", data)
        print(
            f"Resposta inesperada do Intellisign: {response.status_code} - {response.text}"
        )
    except Exception as e:
        print(f"Erro ao enviar o envelope: {e}")
