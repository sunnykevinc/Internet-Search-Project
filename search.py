import os
from langchain import OpenAI, SerpAPIWrapper
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType

os.environ["OPENAI_API_KEY"] = "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"
os.environ["SERPAPI_API_KEY"] = "52ef0648b26613c31e68069c46eae702a436c37594541671911be42468abb87a"

llm = OpenAI(temperature=0)
search = SerpAPIWrapper()
tools = [
  Tool(
    name="Intermediate Answer",
    func=search.run,
    description="useful for when you need to answer questions",
  )
]

while True:
  query = input("What is your question:")
  self_ask_with_search = initialize_agent(tools,
                                          llm,
                                          agent=AgentType.SELF_ASK_WITH_SEARCH,
                                          verbose=True)
  self_ask_with_search.run(query)