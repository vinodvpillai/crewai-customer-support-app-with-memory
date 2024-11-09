from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from customer_support_automation.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, WebsiteSearchTool
from crewai import LLM # type: ignore
import os
from os.path import join, dirname
from dotenv import load_dotenv


# Load environment variables
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

@CrewBase
class CustomerSupportAutomationCrew():
	"""CustomerSupportAutomation crew"""
	
	# LLM
	llm = LLM(model=os.getenv('GEMINI_MODEL'),api_key=os.getenv('GEMINI_API_KEY'))

	@agent
	def support_agent(self) -> Agent:
		return Agent(
			llm=self.llm,
			config=self.agents_config['support_agent'], # type: ignore
			verbose=True
		)

	@agent
	def support_quality_assurance_agent(self) -> Agent:
		return Agent(
			llm=self.llm,
			config=self.agents_config['support_quality_assurance_agent'], # type: ignore
			verbose=True
		)

	@task
	def inquiry_resolution(self) -> Task:
		return Task(
			tools=[ScrapeWebsiteTool(website_url="https://docs.crewai.com/introduction")],
			config=self.tasks_config['inquiry_resolution'], # type: ignore
		)

	@task
	def quality_assurance_review(self) -> Task:
		return Task(
			config=self.tasks_config['quality_assurance_review'], # type: ignore
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the CustomerSupportAutomation crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator # type: ignore
			tasks=self.tasks, # Automatically created by the @task decorator # type: ignore
			process=Process.sequential,
			embedder={
				"provider": "cohere",
				"config": {
					"api_key": os.getenv('COHERE_API_KEY'),
					"model_name": os.getenv('COHERE_MODEL')
				}
			},
			verbose=False,
			memory=True
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)