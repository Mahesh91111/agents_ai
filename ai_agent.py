import os ##  THIS CODE IS DEVELOP BY MAHESHssss and ai_data_engineer_developer and is umahesh varma
from dotenv import load_dotenv 

from langchain.tools import tool
from langchain.agents import create_agent
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv() ## dotenv files is loaded

# Create Groq LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile", ##model
    temperature=0 ##No changess
)

# -----------------------------
# Tool
# -----------------------------
@tool  ##Tool is created
def get_weather(city: str) -> str:
    """Get the weather for a city."""

    weather = {
        "hyderabad": "☀️ 34°C, Sunny",
        "bangalore": "🌤️ 27°C, Cloudy",
        "chennai": "🌧️ 31°C, Rainy",
        "mumbai": "🌦️ 29°C, Heavy Rain",
        "delhi": "🔥 39°C, Hot"
    }

    return weather.get(
        city.lower(),
        f"No weather data available for {city}"
    )

# -----------------------------
# Create Agent
# ----------------------------- ## Agent is created by mahesh this agent is helpful for weather information retirved
agent = create_agent(  ##This is line is used to create the agent
    model=llm,
    tools=[get_weather],
    system_prompt="You are a helpful weather assistant."
)

print("Weather Agent Started!")
print("Type 'exit' to quit.\n")

while True:
    query = input("You : ")

    if query.lower() == "exit":
        break

    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": query
                }
            ]
        }
    )

    print("\nAssistant:") ## This is print statement for printing the data
    print(result["messages"][-1].content)
    print("-" * 50)
    
## code is tell About the weather information for different cities using a Groq LLM and LangChain tools. The agent responds to user queries about the weather in specified cities.
## and thens it provides the user with the requested weather information.