from agents import Agent
from tools.email_tools import get_email_agents_as_tools

def get_emailer_agent():
  instructions = """
    You are an email formatter and sender. You receive the body of an email to be sent. 
    You first use the subject_writer tool to write a subject for the email, then use the html_converter tool to convert the body to HTML. 
    Finally, you use the send_html_email tool to send the email with the subject and HTML body.
  """
  emailer_agent = Agent(
      name="Email Manager",
      instructions=instructions,
      tools=get_email_agents_as_tools(),
      model="gpt-4o-mini",
      handoff_description="Convert an email to HTML and send it"
    )
  return emailer_agent
