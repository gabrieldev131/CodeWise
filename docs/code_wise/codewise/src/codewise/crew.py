import sys, os, re
import yaml
from dotenv import load_dotenv
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task

# Garante que diretórios internos sejam reconhecidos
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Carrega variáveis do .env
load_dotenv()

# Carrega configurações dos agentes (global)
with open('config/agents.yaml', 'r', encoding='utf-8') as f:
    agents_config_data = yaml.safe_load(f)

# Instancia o modelo Gemini
llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.7
)

@CrewBase
class Codewise():
    """Codewise crew"""

    def __init__(self, commit_message: str):
        self.commit_message = commit_message

        # Carrega tasks.yaml com substituição segura de {{ topic }}
        with open('config/tasks.yaml', 'r', encoding='utf-8') as f:
            raw_tasks = f.read()

            # Escapa corretamente a mensagem para evitar quebra no YAML
            escaped_message = self.commit_message.replace('"', '\\"').replace('\n', ' ').strip()

            # Substitui todas as ocorrências de {{ topic }} de forma segura
            raw_tasks = re.sub(r"\{\{\s*topic\s*\}\}", escaped_message, raw_tasks)
            self.tasks_config_data = yaml.safe_load(raw_tasks)

    @agent
    def senior_architect(self) -> Agent:
        config = agents_config_data['senior_architect']
        return Agent(config=config, llm=llm, verbose=True)

    @agent
    def senior_analytics(self) -> Agent:
        config = agents_config_data['senior_analytics']
        return Agent(config=config, llm=llm, verbose=True)

    @agent
    def quality_consultant(self) -> Agent:
        config = agents_config_data['quality_consultant']
        return Agent(config=config, llm=llm, verbose=True)

    @agent
    def quality_control_manager(self) -> Agent:
        config = agents_config_data['quality_control_manager']
        return Agent(config=config, llm=llm, verbose=True)

    @task
    def analise_estrutura(self) -> Task:
        cfg = self.tasks_config_data['analise_estrutura']
        return Task(
            description=cfg['description'],
            expected_output=cfg['expected_output'],
            agent=self.senior_architect(),
            output_file='arquitetura_atual.md'
        )

    @task
    def analise_heuristicas(self) -> Task:
        cfg = self.tasks_config_data['analise_heuristicas']
        return Task(
            description=cfg['description'],
            expected_output=cfg['expected_output'],
            agent=self.senior_analytics(),
            output_file='analise_heuristicas_integracoes.md'
        )

    @task
    def analise_solid(self) -> Task:
        cfg = self.tasks_config_data['analise_solid']
        return Task(
            description=cfg['description'],
            expected_output=cfg['expected_output'],
            agent=self.quality_consultant(),
            output_file='analise_solid.md'
        )

    @task
    def padroes_projeto(self) -> Task:
        cfg = self.tasks_config_data['padroes_projeto']
        return Task(
            description=cfg['description'],
            expected_output=cfg['expected_output'],
            agent=self.quality_control_manager(),
            output_file='padroes_de_projeto.md'
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[
                self.senior_architect(),
                self.senior_analytics(),
                self.quality_consultant(),
                self.quality_control_manager()
            ],
            tasks=[
                self.analise_estrutura(),
                self.analise_heuristicas(),
                self.analise_solid(),
                self.padroes_projeto()
            ],
            process=Process.sequential
        )
