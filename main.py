from openclaw import Agent

controller_prompt = """
You are the Executive Producer of a Viral Horror YouTube Channel.
Your job is to coordinate the Idea Agent, Script Agent, and Video Agent.
Ensure the stories are 'Creepypasta' style: psychological, dark, and eerie.
"""

boss = Agent(
    name="Controller",
    instructions=controller_prompt,
    model="gpt-4-turbo"
)
