/*
    Objetivo: Cria um lote de notas associadas a um negócio no HubSpot.

    Parametros:
        - associationTypeId: ID do tipo de associação entre nota e negócio 
        (https://developers.hubspot.com/docs/api-reference/crm-associations-v4/guide#association-type-id-values).
        - dealId: ID do negócio ao qual as notas serão associadas.
        - notesData: Array de objetos contendo os dados das notas a serem criadas com as propriedades
         `hs_note_body`, `hs_timestamp` e `hs_attachment_ids` (adapte conforme necessário).
        - token: Token de autenticação para a API do HubSpot.

    Retorna:
    - Resposta da API do HubSpot com os detalhes das notas criadas.
*/

async function createBatchOfNotes(associationTypeId, dealId, notesData, token) {
  const url = "https://api.hubapi.com/crm/v3/objects/notes/batch/create";
  const payload = {
    inputs: notesData.map((note) => {
      return {
        associations: [
          {
            types: [
              {
                associationCategory: "HUBSPOT_DEFINED",
                associationTypeId: associationTypeId,
              },
            ],
            to: { id: dealId },
          },
        ],
        properties: {
          hs_note_body: note.hs_note_body ?? "Copia de nota sem corpo",
          hs_timestamp: Date.now(),
          hs_attachment_ids: note.hs_attachment_ids,
        },
      };
    }),
  };

  const headers = {
    Authorization: `Bearer ${token}`,
    "Content-Type": "application/json",
  };
  try {
    const response = await axios.post(url, payload, { headers });
    return response.data;
  } catch (error) {
    const errorMessage =
      error.response?.data?.message || "Erro desconhecido no Hubspot ";
    throw new Error(errorMessage);
  }
}
