import asyncio

from mcp import StdioServerParameters, ClientSession
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain.agents import initialize_agent, AgentType

from app.bailian.common import llm


async def create_mcp_stdio_client():
    server_parameters = StdioServerParameters(command="python", args=[
        "/Users/tonyflame/aiProject/langchain_study/app/mcp/stdio/mcp_stdio_server.py"])


    # read, write = await stdio_client(server_parameters)
    async with stdio_client(server_parameters) as (read, write):
        # session = ClientSession(read, write)
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)
            print(tools)

            agent = initialize_agent(
                llm=llm,
                tools=tools,
                agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
                verbose=True
            )

            resp = await agent.ainvoke("1 + 2 * 5 = ?")
            print(resp)

asyncio.run(create_mcp_stdio_client())