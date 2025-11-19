import gradio
from groq import Groq
# Initialize Groq client
client = Groq(
    api_key="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",
)
# Initialize system message list
def initialize_messages():
    return [
        {
            "role": "system",
            "content": """You are a Football information assistant with strong
            knowledge about football rules, players, teams, formats, records,
            match updates, and history. Answer everything in simple and clear English."""
        }
    ]

# Global message list
messages_prmt = initialize_messages()

# Chatbot function
def customLLMBot(user_input, history):
    global messages_prmt

    # Add user message
    messages_prmt.append({"role": "user", "content": user_input})

    # Get response from model
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages_prmt
    )

    # Extract assistant response
    LLM_reply = response.choices[0].message.content

    # Add reply to message history
    messages_prmt.append({"role": "assistant", "content": LLM_reply})

    return LLM_reply


# ----------- GRADIO INTERFACE -----------
iface = gradio.ChatInterface(
    customLLMBot,
    chatbot=gradio.Chatbot(height=300),
    textbox=gradio.Textbox(placeholder="Ask me anything about football"),
    title="Football Info ChatBot",
    description="Your football assistant for rules, players, records, matches & more.",
    theme="soft",
    examples=[
        "Who is the God of football?",
        "Which country hosted the FIFA World Cup in 2022?",
        "What is the primary objective of the game in football?"
    ]
)

iface.launch(share=True)