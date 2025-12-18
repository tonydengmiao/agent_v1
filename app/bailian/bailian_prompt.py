from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate

from app.bailian.common import llm

# resp = llm.invoke("100+100=?")
# print(resp.content)
#
# resp = llm.stream("100+100=?")
# for chunk in resp:
#     print(chunk.content, end="")

# prompt_template = PromptTemplate.from_template("今天{something}真不错")
# prompt = prompt_template.format(something="天气")
# print(prompt)

# system_message_template = ChatMessagePromptTemplate.from_template(
#     template="你是一位{role}专家，擅长回答{domain}领域的问题",
#     role="system"
# )
#
# human_message_template = ChatMessagePromptTemplate.from_template(
#     template="用户问题：{question}",
#     role="user"
# )
#
# chat_prompt_template = ChatPromptTemplate.from_messages([
#     system_message_template,
#     human_message_template
# ])
# prompt = chat_prompt_template.format_messages(role="编程", domain="Web开发", question="如何构建一个基于Vue的前端应用?")
# print(prompt)
# resp = llm.stream(prompt)
# for chunk in resp:
#     print(chunk.content, end="")

example_prompt = "输入：{input}\n输出：{output}"
examples = [
    {"input": "将'Hello'翻译成中文", "output": "你好"},
    {"input": "将'Goodbye'翻译成中文", "output": "再见"}
]

few_shot_prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=PromptTemplate.from_template(example_prompt),
    prefix="请将以下英文翻译成中文：",
    suffix="输入：{text}\n输出：",
    input_variables=["text"]
)

# print(few_shot_prompt_template)
#
# prompt = few_shot_prompt_template.format(text="Thank you!")
# print(prompt)
# resp = llm.stream(prompt)

chain = few_shot_prompt_template | llm
resp = chain.stream(input={"text": "Thank you!"})

for chunk in resp:
    print(chunk.content, end="")