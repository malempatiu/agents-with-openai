from agents import Agent, function_tool
from sendgrid.helpers.mail import Mail, Email, To, Content
import sendgrid
import certifi
import os
from .email_instructions import get_email_instructions
os.environ['SSL_CERT_FILE'] = certifi.where()

model = 'gpt-4o-mini'
agent_names = [
    'Email subject writer',
    'HTML email body converter'
]

tools_data = {
    'Email subject writer': {
        'tool_name': 'subject_writer',
        'tool_description': 'Write a subject for a cold sales email'
    },
    'HTML email body converter': {
        'tool_name': 'html_converter',
        'tool_description': 'Convert a text email body to an HTML email body'
    }
}


@function_tool
def send_html_email(subject: str, html_body: str) -> dict[str, str]:
    """ Send out an email with the given subject and HTML body to all sales prospects """
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email(os.environ.get('SENDGRID_EMAIL_SENDER'))
    to_email = To(os.environ.get('SENDGRID_EMAIL_RECEIVER'))
    content = Content("text/html", html_body)
    mail = Mail(from_email, to_email, subject, content).get()
    sg.client.mail.send.post(request_body=mail)
    return {"status": "success"}

def get_email_agents():
  instructions = get_email_instructions()
  email_agents = []
  [
      email_agents.append(
          Agent(
              name=agent_name,
              instructions=instructions[agent_name],
              model=model
          )
      ) for agent_name in agent_names
  ]

  return email_agents


def get_email_agents_as_tools():
  email_agents = get_email_agents()
  email_agents_as_tools = []
  [
      email_agents_as_tools.append(
          email_agent.as_tool(
              tool_name=tools_data[email_agent.name]['tool_name'],
              tool_description=tools_data[email_agent.name]['tool_description']
          )
      )
      for email_agent in email_agents
  ]
  return email_agents_as_tools + [send_html_email]


if __name__ == '__main__':
  print(get_email_agents_as_tools())
