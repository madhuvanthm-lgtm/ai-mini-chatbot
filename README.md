# AI Mini Chatbot

A friendly chatbot that answers your questions quickly and effectively, built with [vLLM](https://github.com/vllm-project/vllm) for fast, efficient LLM inference.

## Features

- Simple command-line chat interface
- Remembers conversation history for context-aware responses
- Fast inference powered by vLLM
- Easy to customize with different models and response settings

## Requirements

- A CUDA-capable GPU with sufficient VRAM
- Python 3.9+

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

If using a gated model (e.g. Meta's Llama models), log in to Hugging Face first:

```bash
huggingface-cli login
```

## Usage

Run the chatbot:

```bash
python basic_chatbot.py
```

Type your questions and get responses. Type `exit` or `quit` to end the session.

## Example

```
You: What is the capital of France?
Bot: The capital of France is Paris.

You: Tell me one interesting fact about it.
Bot: The Eiffel Tower was originally intended to be a temporary structure...
```

## How it works

- `SamplingParams(max_tokens=200)` controls how long each response can be
- The `conversation` list stores the full chat history, so the bot remembers earlier context
- `llm.chat()` sends the conversation to the model and returns a generated response

## Customization

Swap the model in `basic_chatbot.py`:

```python
llm = LLM(model="meta-llama/Llama-3.1-8B-Instruct")
```

Adjust response length or creativity by changing `SamplingParams`:

```python
sampling_params = SamplingParams(max_tokens=200, temperature=0.7, top_p=0.9)
```

## Model tested

- `meta-llama/Llama-3.1-8B-Instruct`
