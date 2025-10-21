import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_associated_object_ids(from_object, object_id, to_object, access_token):
    try:
        url = f"https://api.hubapi.com/crm/v3/objects/{from_object}/{object_id}/associations/{to_object}"
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data.get("results"):
                return [result["id"] for result in data["results"]]
    except Exception as e:
        print(f"Erro ao obter o ID do orçamento associado: {e}")
        raise e


# [TESTE]
if __name__ == "__main__":
    # Exemplo de uso
    deal_id = "45759034953"
    access_token = os.getenv("HOUSI_ACCESS_TOKEN")
    result = get_associated_object_ids("deals", deal_id, "quotes", access_token)
    print("ID do objeto associado à citação:", result)
