# 🤖 Python AI Chatbot

A simple command-line AI chatbot built with Python as part of my learning journey in **Stanford Code in Place**.

This project uses GPT to generate responses, remembers previous messages during a conversation, and supports customizable AI personalities.

## 🚀 Features

- **AI-Powered Chat:** Communicate with GPT through the terminal.
- **Conversation Memory:** Maintains chat history so the bot can respond using previous messages.
- **Custom Personality:** Uses a system message to define the bot's personality and response style.
- **Peek Command:** Type `peek` to view the saved conversation history.
- **Interactive Chat:** Continue chatting until you press Enter without typing anything.

## 🛠️ Technologies Used

- Python 3
- GPT through Stanford Code in Place's `ai` module
- Python lists and dictionaries
- Functions, loops, and conditional statements

## ⚙️ How It Works

1. The user enters a message.
2. The program stores the message in a conversation history list.
3. The conversation history is formatted into a single prompt.
4. The prompt is sent to GPT using `call_gpt()`.
5. GPT generates a response.
6. The response is displayed and added to the conversation history.

This process continues until the user presses Enter.

## 💻 Example

```text
Chat with the bot! (press Enter to quit)

You: Hello!
Bot: Hey there! How can I help?

You: My name is Sam.
Bot: Nice to meet you, Sam!

You: What's my name?
Bot: Your name is Sam!

You:
```

*AI-generated responses may vary.*

## 🔍 Peek Command

The `peek` command displays the conversation history.

```text
You: peek

    The record has 5 messages:
    system: You are Captain Python...
    user: Hello!
    assistant: Hey there! How can I help?
    user: My name is Sam.
    assistant: Nice to meet you, Sam!
```

The system message is included in the stored history, but is not displayed during normal chatting.

## 📂 Project Structure

```text
Python-AI-Chatbot/
│
├── main.py
└── README.md
```

The project uses an `ai` module provided by the Stanford Code in Place learning environment.

## ▶️ Running the Project

This project was developed using the **Stanford Code in Place Python environment**.

1. Open the project in the Code in Place editor.
2. Ensure the course-provided `ai` module is available.
3. Run `main.py`.
4. Start chatting with the bot.

**Note:** The `ai` module is not part of standard Python. Running this project locally in VS Code requires a compatible implementation of `call_gpt()`.

## 📚 What I Learned

Through this project, I practiced:

- Working with Python functions
- Using lists and dictionaries
- Building interactive programs with loops
- Managing conversation history
- Formatting prompts for AI models
- Understanding system messages and AI personalities
- Reusing functions to build larger applications

## 🔮 Future Improvements

- Add multiple selectable chatbot personalities.
- Save conversation history to a file.
- Add a graphical user interface.
- Support loading previous conversations.
- Integrate a standalone AI API for local execution.

## 🎓 Acknowledgment

Built as a learning project during **Stanford Code in Place**, an introductory programming course offered by Stanford University.

## 👨‍💻 Author

**Usman Shakir**

BS Data Science Undergraduate

[LinkedIn](https://www.linkedin.com/in/usman-shakir7/) | [GitHub](https://github.com/Usmanshakir7)
