import ollama
 
def chat():
    print("Inicia el chatbot con Llama IA. Escribe 'salir' para terminar la conversación.")
    while True:
        user_input = input("Usuario: ")
        if user_input.lower() == "salir":
            break
        """response = ollama.chat(model="llama3:8b", messages=[{"role": "user", "content": user_input}])"""
        response = ollama.chat(model="mistral", messages=[{"role": "user", "content": user_input}])
        """response = ollama.chat(model="gemma", messages=[{"role": "user", "content": user_input}])"""
        
        ai_response = response.get("message", {}).get("content", "no entendi la pregunta")
        print(f"LlamaIA: {ai_response}")
 
if __name__ == "__main__":
    chat()