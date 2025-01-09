from pydantic_ai import Agent
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from app.db import get_db_connection

# load env for agent
load_dotenv()

# define the output pydantic schema
class Balance(BaseModel):
    name: str = Field(description="name of customer")
    balance: str = Field(description="bank balance of customer")
    id: str = Field(description='id of customer')

# create agent instance
agent = Agent(
    model='openai:gpt-4o',
    system_prompt = 'You are customer service agent for a bank'
)

#define tools via decorator
@agent.tool
def return_account_balance(self):
    return '$12'

@agent.tool
def get_customer_name(self):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT name FROM customers")
        result = cursor.fetchall()
        return [dict(row) for row in result]
    finally:
        cursor.close()
        conn.close()

#Dynamic system prompts can be registered with the @agent.system_prompt decorator, 
# and can make use of dependency injection.
@agent.system_prompt
def customer_id(ctx):
    return 'Customer id is 11'
    
#create main function 
async def main(): 
    result = await agent.run('Find my account balance for me?', result_type=Balance)
    print(result.data)
    
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())