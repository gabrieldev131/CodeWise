import os
import traceback
from dotenv import load_dotenv
from cw_runner import CodewiseRunner

def main():
    load_dotenv()
    print("Modelo em uso:", os.getenv("MODEL_NAME"))

    try:
        runner = CodewiseRunner()
        runner.executar()
    except Exception:
        print("Erro ao executar:")
        traceback.print_exc()

if __name__ == "__main__":
    main()
