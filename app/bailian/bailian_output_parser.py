from langchain_core.output_parsers import StrOutputParser, CommaSeparatedListOutputParser
from langchain.output_parsers import DatetimeOutputParser
from langchain_core.prompts import ChatPromptTemplate
from app.bailian.common import chat_prompt_template, llm

# parser = StrOutputParser()
# parser = CommaSeparatedListOutputParser()
parser = DatetimeOutputParser()

instructions = parser.get_format_instructions()
#
# chain = chat_prompt_template | llm | parser

# resp = chain.invoke(input={"role": "计算", "domain": "数学计算", "question": "100*100=?"})

prompt = ChatPromptTemplate.from_messages([
    ('system', f"必须按照以下格式返回日期时间：{instructions}"),
    ('human', '请将以下自然语言转换为标准日期时间格式：{text}')
])

print(prompt)

chain = prompt | llm | parser

resp = chain.invoke({"text": "二零二五年二月一日上午十点十分"})

print(type(resp))

print(resp)