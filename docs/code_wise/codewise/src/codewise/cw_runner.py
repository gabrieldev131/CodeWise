import os
from crew import Codewise

class CodewiseRunner:
    def __init__(self, input_path: str, output_path: str = "resposta.txt"):
        self.input_path = input_path
        self.output_path = output_path

    def _ler_input(self) -> str:
        with open(self.input_path, "r", encoding="utf-8") as f:
            return f.read()

    def _juntar_outputs(self, arquivos_md: list):
        with open(self.output_path, "w", encoding="utf-8") as f_out:
            for path in arquivos_md:
                if os.path.exists(path):
                    with open(path, "r", encoding="utf-8") as f_in:
                        f_out.write(f_in.read())
                        f_out.write("\n\n" + "="*80 + "\n\n")
                else:
                    f_out.write(f"[ARQUIVO NÃO ENCONTRADO]: {path}\n")

    def rodar(self):
        # Lê input do commit
        entrada_txt = self._ler_input()

        #  Corrigido: passa o commit_message para a instância
        codewise = Codewise(commit_message=entrada_txt)
        crew = codewise.crew()

        #  Agora não precisa mais de "inputs", pois o conteúdo foi injetado no YAML
        crew.kickoff()

        # Une os arquivos de output
        arquivos_md = [
            "arquitetura_atual.md",
            "analise_heuristicas_integracoes.md",
            "analise_solid.md",
            "padroes_de_projeto.md"
        ]
        self._juntar_outputs(arquivos_md)
        print(f"\n Output gerado em: {self.output_path}")
