import os 
from langchain.agents import create_agent
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.tools.tools import web_search,web_scrape
load_dotenv()

GROQ_API_KEY= os.getenv("GROQ_API_KEY")

llm = ChatGroq(model = "openai/gpt-oss-20b",verbose = True,temperature=0.3)

def build_search_agent():
    return create_agent(
        model = llm,
        tools = [web_search],
    )

def reader_agent():
    return create_agent(
        model = llm,
        tools = [web_scrape],
    )