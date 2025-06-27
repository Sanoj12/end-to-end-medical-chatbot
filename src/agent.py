from langchain.agents import create_react_agent,AgentExecutor
from langchain.prompts import PromptTemplate ##custom prompt
#from langgraph.checkpoint.memory import MemorySaver



from langchain_groq import ChatGroq

from dotenv import load_dotenv
import os


from src.translator_tool import translate_to_english,translate_back,detect_language

from src.pinecone_tool import search_doc

from src.web_search_tools import web_search




##memory init

#memory = MemorySaver()

load_dotenv()





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


agent = create_react_agent(llm=groq_llm ,tools=tools, prompt=prompt)
agent_executor = AgentExecutor(agent=agent,tools=tools, verbose=True,handle_parsing_errors=True)

##memory
#config={"configurable":{"thread_id":"1"}}




##
def run_agent(user_input):
    return agent_executor.invoke({"input":user_input})