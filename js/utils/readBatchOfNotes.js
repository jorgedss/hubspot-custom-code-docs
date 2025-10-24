/*
    Objetivo: Lê um lote de notas do Hubspot com base em seus IDs.

    Parametros:
        - notesIds: Array de IDs das notas a serem lidas.
        - token: Token de autenticação para a API do Hubspot.
        
    Retorno:
       Uma Promise que resolve com os dados das notas lidas ou rejeita com um erro.
*/

async function readBatchOfNotes(notesIds, token) {
  const url = "https://api.hubapi.com/crm/v3/objects/notes/batch/read";
  const headers = {
    Authorization: `Bearer ${token}`,
    "Content-Type": "application/json",
  };

  const payload = {
    inputs: notesIds.map((id) => {
      return { id: id };
    }),
    properties: ["hs_attachment_ids", "hs_note_body"],
  };

  try {
    const response = await axios.post(url, payload, { headers });
    return response.data.results;
  } catch (error) {
    console.error("Erro ao ler notas em lote:", error);
    const errorMessage =
      error.response?.data?.message || "Erro desconhecido no Hubspot ";

    throw new Error(errorMessage);
  }
}
