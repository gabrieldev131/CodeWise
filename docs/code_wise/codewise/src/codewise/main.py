import os
import traceback
from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")


print("Modelo em uso:", os.getenv("MODEL_NAME"))

from crew import Codewise
from datetime import datetime

def run():
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year),
        "project_path": "./"
    }
    codewise = Codewise()
    crew_instance = codewise.crew()

    try:
        crew_instance.kickoff(inputs=inputs)
    except Exception as e:
        print(f"Erro ao executar: {e}")

if __name__ == "__main__":
    run()
