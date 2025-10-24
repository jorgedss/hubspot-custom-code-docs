/*
    Objetivo: Obtém os anexos associados a um objeto específico no HubSpot.

    Parâmetros:
        - objectType: O tipo do objeto (ex: "deals", "contacts").
        - objectId: O ID do objeto ao qual os anexos estão associados.
        - toObjectType: O tipo do objeto ao qual os anexos estão associados (ex: "notes").
        - token: Token de autenticação para a API do HubSpot.

    Retorno:
       Uma Promise que resolve com os dados dos anexos associados ou rejeita com um erro.
*/

async function getAssociatedAttachments(
  objectType,
  objectId,
  toObjectType,
  token
) {
  try {
    const url = `https://api.hubapi.com/crm/v4/objects/${objectType}/${objectId}/associations/${toObjectType}`;
    const headers = {
      Authorization: `Bearer ${token}`,
    };

    const response = await axios({ url, method: "GET", headers });
    const results = response.data.results;
    console.log("Anexos associados encontrados:", results);

    return results;
  } catch (error) {
    console.error("Erro ao buscar anexos associados:", error);
    throw error;
  }
}
