# My Chat Bot

A simple Gradio based chatbot built with LangChain and Ollama.

## Overview

This project provides a minimal example of a conversational assistant using:
- **Gradio** for the web UI.
- **LangChain**'s `ChatOpenAI` wrapper to talk to a local Ollama server (`http://localhost:11434/v1`).
- A basic message history that stores system and human messages.

The `gradio-file.py` script creates a `gr.ChatInterface` that echoes the LLM's response.

## Prerequisites

- Python 3.12 (or compatible version).
- [Ollama](https://ollama.com/) installed and running with a model (e.g., `gemma2`, `llama3.1`).

## Setup

```bash
# Clone the repository (if not already)
git clone <repo-url>
cd my-chat-bot

# Create a virtual environment and activate it
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Running the Bot

```bash
python gradio-file.py
```

The script will print instructions and launch the Gradio UI. Open the shown URL in your browser.

## Customisation

- Change the system prompt on line 19 of `gradio-file.py`.
- Adjust the model name, temperature, or other `ChatOpenAI` parameters.
- Add more sophisticated message handling or integrate external tools.

## License

This example is provided for educational purposes. Feel free to adapt it for your own projects.