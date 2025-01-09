from pydantic_ai import Agent
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model='openai:gpt-4o',
    system_prompt = 'You are customer service agent for a bank'
)

result = agent.run_sync('What is my account balance?')
print(result.data)