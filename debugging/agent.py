from langchain.agents import create_react_agent,AgentExecutor
from langchain.prompts import PromptTemplate ##custom prompt
#from langgraph.checkpoint.memory import MemorySaver



from langchain_groq import ChatGroq

from dotenv import load_dotenv
import os

load_dotenv()

from langchain_core.tracers import LangChainTracer

os.environ["LANGSMITH_PROJECT"]="my-medical-agent"

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
os.environ["TAVILY_API_KEY"]=os.getenv("TAVILY_API_KEY")
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_aPI_KEY")
os.environ["LANGSMITH_TRACING"] = "true"

from src.translator_tool import translate_to_english,translate_back,detect_language

from src.pinecone_tool import search_doc

from src.web_search_tools import web_search

groq_llm = ChatGroq(
    model_name="llama3-70b-8192",
    temperature=0
)



custom_templates = """
You are a helpful medical assistant...

Only return the final answer. show your thought process or reasoning steps.

User's question:
{input}



Available tools:
{tools}

Choose from: [{tool_names}]


{agent_scratchpad}
"""




prompt = PromptTemplate(
    input_variables=["input","tools","tool_names","agent_scratchpad"],
    template=custom_templates
)



tools=[
    detect_language,
    translate_to_english,
    translate_back,
    search_doc,
    web_search
]


tracer = LangChainTracer(project_name="my-medical-agent")




agent = create_react_agent(llm=groq_llm ,tools=tools, prompt=prompt)
agent_executor = AgentExecutor(agent=agent,tools=tools, verbose=True,  callbacks=[tracer] , handle_parsing_errors=True )
