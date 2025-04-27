from langchain_openai import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)
from langchain.memory import ConversationSummaryBufferMemory
from langchain.schema import HumanMessage, AIMessage
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Read final master system prompt
with open("prompt.txt", "r") as f:
    NINA_SYSTEM_PROMPT = f.read()

# MODEL TOGGLE (choose 'gpt-4-turbo' or 'gpt-3.5-turbo-0125')
MODEL_NAME = os.getenv("NINA_MODEL", "gpt-4-turbo")

# Setup ChatOpenAI
llm = ChatOpenAI(
    model=MODEL_NAME,
    temperature=0.2,
    streaming=True
)

# Setup conversation memory
memory = ConversationSummaryBufferMemory(
    memory_key="messages",
    return_messages=True,
    llm=llm
)

# Setup prompt template
system_prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(NINA_SYSTEM_PROMPT),
    MessagesPlaceholder(variable_name="messages"),
    HumanMessagePromptTemplate.from_template("{input}")
])

# Create conversation chain
nina_chain = system_prompt | llm

# Initialize Nina (for first run)
def initialize_nina():
    return nina_chain.invoke({
        "input": "",
        "messages": []
    }).content

# Chat with Nina (passing formatted messages)
def chat_with_nina(user_input, raw_messages, stream=False):
    formatted_messages = []
    for msg in raw_messages:
        if msg["role"] == "user":
            formatted_messages.append(HumanMessage(content=msg["content"]))
        else:
            formatted_messages.append(AIMessage(content=msg["content"]))

    if stream:
        # Streaming response (yields tokens)
        response = nina_chain.stream({
            "input": user_input,
            "messages": formatted_messages
        })
        for chunk in response:
            yield chunk.content if hasattr(chunk, "content") else ""
    else:
        # Normal full response
        return nina_chain.invoke({
            "input": user_input,
            "messages": formatted_messages
        }).content
