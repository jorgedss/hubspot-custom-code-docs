import requests

"""
    Obtém uma propriedade específica de um objeto no HubSpot.
    Parâmetros:
        from_object (str): O tipo do objeto de origem (ex: "deals").
        object_id (str): O ID do objeto de origem.
        access_token_hubspot (str): Token de acesso para autenticação na API HubSpot.
        properties_name (str): Nome das propriedades a serem obtidas separadas por vírgula.
        Ex: "name,lastname,email".
    Retorna:
        str: Valor da propriedade solicitada ou None se não encontrada.
"""


def get_object_properties(
    from_object, object_id, access_token_hubspot, properties_name
):
    try:
        url = f"https://api.hubapi.com/crm/v3/objects/{from_object}/{object_id}?properties={properties_name}"
        headers = {"Authorization": f"Bearer {access_token_hubspot}"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json().get("properties", {}).get(properties_name)
        return None
    except Exception as e:
        print(f"Erro ao obter propriedade do objeto: {e}")
        return None
