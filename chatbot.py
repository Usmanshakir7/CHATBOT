
from ai import call_gpt

INDENT = "    "

PERSONALITY = "You are Captain Python, a friendly programming teacher. Explain things simply, use a little humor, and keep replies short."
def make_message(role, content):
    return {
        "role": role,
        "content": content
    }


def peek(messages):
    print(f"{INDENT}The record has {len(messages)} messages:")

    for message in messages:
        print(f"{INDENT}{message['role']}: {message['content']}")


def format_messages(messages):
    prompt = ""

    for message in messages:
        if message["role"] == "system":
            prompt += "Instructions: " + message["content"] + "\n\n"

        elif message["role"] == "user":
            prompt += "User: " + message["content"] + "\n"

        else:
            prompt += "Assistant: " + message["content"] + "\n"

    prompt += "Assistant:"
    return prompt


def main():
    messages = [make_message("system", PERSONALITY)]

    print("Chat with the bot! (press Enter to quit)")
    user = input("You: ")

    while user != "":
        if user == "peek":
            peek(messages)

        else:
            messages.append(make_message("user", user))

            prompt = format_messages(messages)
            bot = call_gpt(prompt)

            messages.append(make_message("assistant", bot))
            print("Bot:", bot)

        user = input("You: ")


if __name__ == "__main__":
    main()

