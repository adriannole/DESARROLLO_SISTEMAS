from dotenv import load_dotenv
import os

from ec.llm.service.InferenceService import InferenceService

if __name__ == '__main__':
    load_dotenv('secrets/.env')
    print(os.getenv('OPENAI_API_KEY'))

    try:
        number = int(input("Ingrese un número entero para convertir a binario: "))
        result = InferenceService().invoke(number)
        print(result)
    except ValueError:
        print("Por favor, ingrese un número entero válido.")