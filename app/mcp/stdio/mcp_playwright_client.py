import asyncio

from langchain_mcp_adapters.client import MultiServerMCPClient

# "playwright": {
#   "command": "npx",
#   "args": ["-y", "@executeautomation/playwright-mcp-server"]
# }

async def create_mcp_tools():
    client = MultiServerMCPClient({
        "playwright": {
            "command": "npx",
            "args": ["-y", "@executeautomation/playwright-mcp-server"],
            "transport": "stdio"
        }
    })

    tools = await client.get_tools()
    print(tools)
    return client, tools


asyncio.run(create_mcp_tools())