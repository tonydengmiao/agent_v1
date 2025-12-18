from langchain_openai import ChatOpenAI
from pydantic import SecretStr, BaseModel, Field
from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate, ChatMessagePromptTemplate
from langchain_community.agent_toolkits import FileManagementToolkit

llm = ChatOpenAI(
    model='qwen3-max',
    api_key=SecretStr("sk-d69bfd656643404688126c5e0658935e"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    streaming=True
)

system_message_template = ChatMessagePromptTemplate.from_template(
    template="你是一位{role}专家，擅长回答{domain}领域的问题",
    role="system"
)

human_message_template = ChatMessagePromptTemplate.from_template(
    template="用户问题：{question}",
    role="user"
)

chat_prompt_template = ChatPromptTemplate.from_messages([
    system_message_template,
    human_message_template
])

class AddInputArgs(BaseModel):
    a: int = Field(description="first number")
    b: int = Field(description="second number")

@tool(
    description="add two numbers",
    args_schema=AddInputArgs,
    return_direct=False
)
def add(a, b):
    """add two numbers"""
    return a + b

def create_calc_tools():
    return [add]

calc_tools = create_calc_tools()

file_toolkit = FileManagementToolkit(root_dir="/Users/tonyflame/aiProject/langchain_study/.temp")

file_tools = file_toolkit.get_tools()
