import os
from dotenv import load_dotenv

from langchain.tools import tool
from langchain.agents import create_agent
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# Create Groq LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile", ##model
    temperature=0 ##No changes
)

# -----------------------------
# Tool
# -----------------------------
@tool
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
# -----------------------------
agent = create_agent(
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

    print("\nAssistant:")
    print(result["messages"][-1].content)
    print("-" * 50)