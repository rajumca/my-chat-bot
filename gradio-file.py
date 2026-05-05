import gradio as gr
import json
from typing import List, Tuple, Dict, Any
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage


llm = ChatOpenAI(
    model="gpt-oss:120b-cloud", #qwen2.5-coder:7b
    base_url="http://localhost:11434/v1",
    api_key="ollama", # Required but ignored
    temperature=0.7
)


from typing import List, Tuple
import gradio as gr
messages=[
    SystemMessage(content="You are a helpful assistant")
]
def echo_chatbot(message: str, history: List[Tuple[str, str]]) -> str:
    """A simple echo chatbot for testing."""
    messages.append(HumanMessage(content=message))
    response = llm.invoke(input=messages)
    messages.append(SystemMessage(content=response.content))
    return str(response.content)
    # return f"You said: {message}"

# Create interface
demo_echo = gr.ChatInterface(
    fn=echo_chatbot,
    title="Echo Chatbot",
    description="A simple chatbot that echoes your messages.",
    examples=[
        "Hello!",
        "How are you?",
        "Tell me about restaurants."
    ]
)

print("Basic chatbot interface created!")
print("To launch, run: demo_echo.launch()")

if __name__ == '__main__':
    demo_echo.launch()