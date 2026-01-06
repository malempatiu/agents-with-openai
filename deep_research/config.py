from dotenv import load_dotenv
import os


def check_openai_api_key():
  load_dotenv(override=True)
  api_key = os.getenv('OPENAI_API_KEY')
  if api_key and api_key[:8] == 'sk-proj-':
    print('OpenAI API Key found')
  else:
    raise ValueError('OpenAI API Key found')
