# tools/web_search_tool.py

from langchain.tools import tool

from langchain_community.tools import TavilySearchResults


# Create instance of Tavily tool
tavily_tool = TavilySearchResults(max_results=2)

@tool
def web_search(query: str) -> str:
    """
    Perform a web search using Tavily for any medical or general query.
    """
    return tavily_tool.run(query)
