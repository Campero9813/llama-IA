import json
from llamaapi import LlamaAPI

# Initialize the SDK
llama = LlamaAPI("LA-b5686052ccce4f1a9f782c508fda7f03fe581d041c1846a1b9341d25c0271964")

# Build the API request
def generate_response(prompt):
    api_request_json = {
        "model": "llama3.1-70b",
        "messages": [
            {"role": "user", "content": prompt},
        ],
        "stream": False,
    }

    response = llama.run(api_request_json)

    try:
        response_data = response.json()
        # Intentamos extraer solo el mensaje del asistente
        if "choices" in response_data and len(response_data["choices"]) > 0:
            return response_data["choices"][0]["message"]["content"]
        else:
            return "Lo siento, no pude generar una respuesta."
    except Exception as e:
        return f"Error al procesar la respuesta: {str(e)}"

def chat():
    print("Inicia el chatbot con Llama IA. Escribe 'salir' para terminar la conversación.")
    while True:
        user_input = input("Usuario: ")
        if user_input.lower() == "salir":
            break
        response = generate_response(user_input)
        print(f"LlamaIA: {response}")

if __name__ == "__main__":
    chat()
