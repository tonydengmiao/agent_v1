
from langchain_core.tools import tool
from app.bailian.common import chat_prompt_template, llm
from pydantic import BaseModel, Field
class AddInputArgs(BaseModel):
    a: int = Field(description="first number")
    b: int = Field(description="second number")

@tool(
    description="add two numbers",
    args_schema=AddInputArgs
)
def add(a, b):
    """add two numbers"""
    return a + b

# add_tools = Tool.from_function(
#     func=add,
#     name="add",
#     description="add two numbers"
# )

add_dict = {"add": add}

llm_with_tools = llm.bind_tools([add])

chain = chat_prompt_template | llm_with_tools

resp = chain.invoke(input={"role":"计算", "domain":"数学计算", "question": "100+100=?"})
# for chunk in resp:
#     print(chunk.content, end="")
print(resp)

for tool_calls in resp.tool_calls:
    print(tool_calls)

    args = tool_calls["args"]
    print(args)

    func = tool_calls["name"]
    print(func)

    tool_func = add_dict[func]

    # tool_content = tool_func(int(args['__arg1']), int(args['example_parameter_2']))
    tool_content = tool_func.invoke(args)
    print(tool_content)