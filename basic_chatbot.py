"""
Basic vLLM chatbot with conversation memory.
Run: python basic_chatbot.py
"""

from vllm import LLM, SamplingParams

# Load the model (swap in whichever model you're using)
llm = LLM(model="meta-llama/Llama-3.1-8B-Instruct")

# Store our conversation history
conversation = []

# Set a reasonable response length
sampling_params = SamplingParams(max_tokens=200)


def main():
    print("Chatbot ready! Type 'exit' or 'quit' to end.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        # Add user message to conversation
        conversation.append({"role": "user", "content": user_input})

        # This is INFERENCE - send to the model and get a response!
        outputs = llm.chat(conversation, sampling_params)
        bot_message = outputs[0].outputs[0].text

        # Add bot's response to conversation so it remembers context
        conversation.append({"role": "assistant", "content": bot_message})

        print(f"Bot: {bot_message}\n")


if __name__ == "__main__":
    main()
