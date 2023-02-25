#_______________________________________________________________________________

import openai
# Instalar la biblioteca en el terminal: pip install openai

# BOT CHATGPT

def chatGPT(prompt=str()):
    # Configurar la clave de API de OpenAI
    openai.api_key = "INTRODUCE AQUI TU API KEY"
    # Definir el prompt o estímulo para la generación de texto
    prompt = prompt
    # Generar texto utilizando la API de OpenAI
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)
    # Imprimir la respuesta generada
    respuesta =str(response.choices[0].text) 
    return respuesta

pregunta = print(chatGPT("INCLUYE LO QUE QUIERAS CONSULTAR"))









