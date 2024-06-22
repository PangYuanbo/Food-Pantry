import getpass
import os
from langchain_core.messages import HumanMessage,SystemMessage
os.environ["OPENAI_API_KEY"] = getpass.getpass()

from langchain_openai import ChatOpenAI

model = ChatOpngenAI(model="gpt-4")
messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi!"),
]

model.invoke(messages)
print(messages[1].content)