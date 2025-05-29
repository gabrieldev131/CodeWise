import os
import traceback
from dotenv import load_dotenv
from cw_runner import CodewiseRunner  # <- nova importação

# Carrega variáveis do .env
load_dotenv(dotenv_path=".env")

print("Modelo em uso:", os.getenv("MODEL_NAME"))

def run():
    input_path = "entrada.txt"   # <- entrada que está simulando o commit por enquanto
    output_path = "resposta.txt" # <- saída unificada dos .md

    try:
        runner = CodewiseRunner(input_path=input_path, output_path=output_path)
        runner.rodar()
    except Exception as e:
        print("Erro ao executar:")
        traceback.print_exc()

if __name__ == "__main__":
    run()
