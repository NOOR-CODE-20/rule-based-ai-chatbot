# 🤖 Rule-Based AI Chatbot

A simple **Rule-Based AI Chatbot** developed in Python as part of **DecodeLabs Artificial Intelligence Project 1**.

The chatbot uses predefined rules, dictionaries, and control-flow logic to understand user inputs and provide appropriate responses.

## 🎯 Project Objective

The main objective of this project is to build a basic chatbot that can:

* Handle greetings
* Handle goodbye and exit commands
* Respond to predefined user inputs
* Use rule-based decision-making
* Run continuously until the user exits

## 🛠️ Technologies Used

* **Python 3**
* Python Dictionaries
* `if-else` statements
* `while` loop
* `for` loop
* String methods

## ✨ Features

### 1. Greeting Intent

The chatbot recognizes:

* `hello`
* `hi`
* `hey`
* `salam`
* `assalam o alaikum`

### 2. Goodbye Intent

The chatbot can exit when the user enters:

* `bye`
* `goodbye`
* `exit`
* `quit`

### 3. Name Intent

The chatbot responds to questions such as:

* `what is your name`
* `who are you`
* `tell me your name`

### 4. How Are You Intent

It recognizes:

* `how are you`
* `how are you doing`
* `are you fine`

### 5. Capabilities Intent

The chatbot can answer:

* `what can you do`
* `help me`
* `what are your features`

### 6. Thanks Intent

It recognizes:

* `thank you`
* `thanks`
* `thankyou`

### 7. Age Intent

It recognizes:

* `how old are you`
* `what is your age`

## 🧹 Whitespace & Case Handling

The chatbot uses:

```python
user_input = user_input.strip().lower()
```

This allows it to handle extra spaces and different capitalization.

For example:

```text
HELLO
  hello
Hello
   HELLO
```

are all treated as:

```text
hello
```

## 🧠 How It Works

The chatbot follows a simple rule-based process:

```text
User Input
     ↓
Remove Extra Spaces
     ↓
Convert Input to Lowercase
     ↓
Check Intent Dictionary
     ↓
Find Matching Intent
     ↓
Generate Response
     ↓
Continue Conversation
```

If no matching intent is found, the chatbot provides a fallback response:

```text
Sorry, I don't understand that.
```

## 📁 Project Structure

```text
rule-based-ai-chatbot/
│
├── chatbot.py
├── README.md
```

## ▶️ How to Run

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Open the Project Folder

```bash
cd rule-based-ai-chatbot
```

### Step 3: Run the Chatbot

```bash
python chatbot.py
```

## 💬 Example Conversation

```text
🤖 AI Bot: Hello! I am your Rule-Based AI Chatbot.
Type 'bye' or 'exit' to stop.

You: hello
Bot: Hello! How can I help you?

You: what is your name
Bot: My name is AI Bot. I am a rule-based chatbot.

You: THANK YOU
Bot: You're welcome! 😊

You: xyz
Bot: Sorry, I don't understand that.

You: bye
Bot: Goodbye! Have a nice day.
```

## 📌 Current Intents

| # | Intent       | Example Input     |
| - | ------------ | ----------------- |
| 1 | Greeting     | hello             |
| 2 | Goodbye      | bye               |
| 3 | Name         | what is your name |
| 4 | How Are You  | how are you       |
| 5 | Capabilities | what can you do   |
| 6 | Thanks       | thank you         |
| 7 | Age          | how old are you   |

## 🚀 Future Improvements

Possible improvements include:

* Add more intents
* Support more variations of user questions
* Add multiple responses for each intent
* Improve fallback responses
* Add a chatbot personality
* Add a graphical user interface
* Add more advanced natural-language processing

## 👩‍💻 Project

**Artificial Intelligence — Project 1**

**Project:** Rule-Based AI Chatbot
**Organization:** DecodeLabs
**Batch:** 2026
