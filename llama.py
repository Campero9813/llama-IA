import json
from llamaapi import LlamaAPI

# Initialize the SDK
llama = LlamaAPI("LA-b5686052ccce4f1a9f782c508fda7f03fe581d041c1846a1b9341d25c0271964")

# Build the API request
def genereate_response(prompt):
    api_request_json = {
        "model": "llama3.1-70b",
        "messages": [
            {"role": "user", "content": prompt},
        ],
        "functions": [
            {
                "name": "obtener_eventos",
                "description": "Obtener eventos en la ubicación especificada",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "La ciudad y el estado por ejemplo, Ciudad de México, CDMX",
                        },
                        "categoria": {
                            "type": "string",
                            "description": "La categoría del evento, por ejemplo, música, deportes",
                        },
                        "fecha": {
                            "type": "string",
                            "description": "La fecha del evento en formato 2025-03-12",
                        },
                    },
                },
                "required": ["location", "categoria"],
            }
        ],
        "stream": False,
        "function_call": "obtener_eventos",
    }

    # Execute the Request
    response = llama.run(api_request_json)
    # Verificar si la respuesta es válida antes de intentar convertirla a JSON
    try:
        return response.json()
    except Exception as e:
        return {"error": f"Error al procesar la respuesta: {str(e)}"}


#Funcion para chatbot
def chat():
    print("Inicia el chat bot con llama IA. Escribe 'salir' para terminar la conversación")
    while True:
        user_input = input("Usuario: ")
        if user_input.lower() == "salir":
            break
        response = genereate_response(user_input)
        print(f"LlamaIA: , {json.dumps(response, indent=2, ensure_ascii=False)}")
if __name__ == "__main__":
    chat()