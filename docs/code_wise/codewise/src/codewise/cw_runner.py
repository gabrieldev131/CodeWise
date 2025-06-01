import os
from crew import Codewise

class CodewiseRunner:
    def __init__(self, caminho_entrada: str = "entrada.txt", caminho_saida: str = "resposta.txt"):
        self.caminho_entrada = caminho_entrada
        self.caminho_saida = caminho_saida
        self.arquivos_md_saida = [
            "arquitetura_atual.md",
            "analise_heuristicas_integracoes.md",
            "analise_solid.md",
            "padroes_de_projeto.md"
        ]

    def _ler_entrada(self) -> str:
        with open(self.caminho_entrada, "r", encoding="utf-8") as arquivo:
            return arquivo.read()

    def _mesclar_resultados_markdown(self):
        with open(self.caminho_saida, "w", encoding="utf-8") as arquivo_saida:
            for caminho_md in self.arquivos_md_saida:
                if os.path.exists(caminho_md):
                    with open(caminho_md, "r", encoding="utf-8") as arquivo_md:
                        arquivo_saida.write(arquivo_md.read())
                        arquivo_saida.write("\n" + "="*80 + "\n\n")
                else:
                    arquivo_saida.write(f"[ARQUIVO NÃO ENCONTRADO]: {caminho_md}\n")

    def executar(self):
        mensagem_commit = self._ler_entrada()
        codewise = Codewise(commit_message=mensagem_commit)
        crew = codewise.crew()
        crew.kickoff(inputs={"input": mensagem_commit})
        self._mesclar_resultados_markdown()
        print(f"\nArquivo final gerado: {self.caminho_saida}")
