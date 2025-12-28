from agents import Agent
from .workflow_instructions import get_workflow_instructions

model = 'gpt-4o-mini'
agent_names = [
  'Professional Sales Agent',
  'Engaging Sales Agent', 
  'Busy Sales Agent'
]

instructions = get_workflow_instructions()

def get_sales_agents():
  sales_agents = []
  [
    sales_agents.append(
      Agent(
        name=agent_name,
        instructions=instructions[agent_name],
        model=model
      )
    ) for agent_name in agent_names
  ]

  return sales_agents


def get_sales_agents_as_tools():
  sales_agents = get_sales_agents()
  sales_agents_as_tools = []
  [
      sales_agents_as_tools.append(
        sales_agent.as_tool(
          tool_name=f'sales_agent{i+1}', 
          tool_description='Write a cold sales email'
        )
      )
    for i, sales_agent in enumerate(sales_agents)
  ]
  return sales_agents_as_tools

if __name__=='__main__':
  print(get_sales_agents_as_tools())