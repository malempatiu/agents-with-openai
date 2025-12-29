from agents import Agent
from handoffs.emailer_agent import get_emailer_agent
from tools.sales_tools import get_sales_agents_as_tools
from guardrails.guardrail_agent import guardrail_against_name

sales_manager_instructions = """
You are a Sales Manager at ComplAI. Your goal is to find the single best cold sales email using the sales_agent tools.
 
Follow these steps carefully:
1. Generate Drafts: Use all three sales_agent tools to generate three different email drafts. Do not proceed until all three drafts are ready.
 
2. Evaluate and Select: Review the drafts and choose the single best email using your judgment of which one is most effective.
You can use the tools multiple times if you're not satisfied with the results from the first try.
 
3. Handoff for Sending: Pass ONLY the winning email draft to the 'Email Manager' agent. The Email Manager will take care of formatting and sending.
 
Crucial Rules:
- You must use the sales agent tools to generate the drafts — do not write them yourself.
- You must hand off exactly ONE email to the Email Manager — never more than one.
"""

def get_sales_manager_agent():
   sales_manager = Agent(
       name="Sales Manager",
       instructions=sales_manager_instructions,
       tools=get_sales_agents_as_tools(),
       handoffs=[get_emailer_agent()],
       model="gpt-4o-mini",
       input_guardrails=[guardrail_against_name]
   )
   return sales_manager