import sys
import os
import re
import yaml
from dotenv import load_dotenv
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class Codewise:
    """Classe principal da crew Codewise"""

    def __init__(self, commit_message: str):
        load_dotenv()

        print(f"DEBUG: commit_message recebido -> {repr(commit_message)}") 
        self.commit_message = commit_message

        self.llm = LLM(
            model="gemini/gemini-2.0-flash",
            temperature=0.7
        )

        with open('config/agents.yaml', 'r', encoding='utf-8') as f:
            self.agents_config = yaml.safe_load(f)

        with open('config/tasks.yaml', 'r', encoding='utf-8') as f:
            self.tasks_config = yaml.safe_load(f)


    @agent
    def senior_architect(self) -> Agent:
        return Agent(config=self.agents_config['senior_architect'], llm=self.llm, verbose=True)

    @agent
    def senior_analytics(self) -> Agent:
        return Agent(config=self.agents_config['senior_analytics'], llm=self.llm, verbose=True)

    @agent
    def quality_consultant(self) -> Agent:
        return Agent(config=self.agents_config['quality_consultant'], llm=self.llm, verbose=True)

    @agent
    def quality_control_manager(self) -> Agent:
        return Agent(config=self.agents_config['quality_control_manager'], llm=self.llm, verbose=True)

    @task
    def task_estrutura(self) -> Task:
        cfg = self.tasks_config['analise_estrutura']
        return Task(description=cfg['description'], expected_output=cfg['expected_output'],
                    agent=self.senior_architect(), output_file='arquitetura_atual.md')

    @task
    def task_heuristicas(self) -> Task:
        cfg = self.tasks_config['analise_heuristicas']
        return Task(description=cfg['description'], expected_output=cfg['expected_output'],
                    agent=self.senior_analytics(), output_file='analise_heuristicas_integracoes.md')

    @task
    def task_solid(self) -> Task:
        cfg = self.tasks_config['analise_solid']
        return Task(description=cfg['description'], expected_output=cfg['expected_output'],
                    agent=self.quality_consultant(), output_file='analise_solid.md')

    @task
    def task_padroes(self) -> Task:
        cfg = self.tasks_config['padroes_projeto']
        return Task(description=cfg['description'], expected_output=cfg['expected_output'],
                    agent=self.quality_control_manager(), output_file='padroes_de_projeto.md')

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
                self.task_estrutura(),
                self.task_heuristicas(),
                self.task_solid(),
                self.task_padroes()
            ],
            process=Process.sequential
        )
