from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch

# The agent
llm = ChatOllama(
# hte gpt-oss model gives an error!
    # model="gemma4:26b",
#    model="hf.co/unsloth/gpt-oss-20b-GGUF:Q5_K_M",
    model="gemma4:e4b",
    # temperature=0
)
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)
 

def main():
    print("Hello from react-search-agent!")
    # weather in tokyo
    # result = agent.invoke({"messages":HumanMessage(content="What is the weather in Tokyo?")})

    # 3 job postings
    result = agent.invoke({"messages":HumanMessage(
        content="""Search for 3 job postings for junior position in a field related to ai in Sweden.
          List the details of each posting including links to the listings.""")})
    print(result)

if __name__ == "__main__":
    main()
