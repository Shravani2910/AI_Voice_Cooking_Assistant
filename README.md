# AI_Voice_Cooking_Assistant

# 🍳 AI Voice Cooking Assistant

An intelligent voice-powered cooking assistant that helps users find recipes, follow step-by-step cooking instructions, convert units, and manage kitchen tasks — all hands-free using voice input and output.

---

## 🎯 Project Goal

To build a voice-controlled AI assistant that makes cooking easier and more interactive by:
- Finding and recommending recipes
- Reading instructions aloud, step-by-step
- Answering cooking-related queries
- Setting timers and handling conversions

---

## ✨ Features

- 🎙️ Voice Input (Speech-to-Text)
- 🗣️ Voice Output (Text-to-Speech)
- 🍲 Recipe Search & Parsing
- 🔁 Step-by-Step Cooking Guidance
- ⏱️ Timer Management
- 📏 Unit Conversion
- 🧠 Smart Queries (e.g., "substitute for eggs", "what’s 200g in cups?")

---

## 🧰 Tech Stack

| Feature             | Technology                            |
|---------------------|----------------------------------------|
| Voice Input         | Whisper API / SpeechRecognition        |
| Voice Output        | pyttsx3 / Google TTS / ElevenLabs      |
| Backend             | Python + FastAPI                       |
| Interface           | Streamlit                              |
| NLP & Logic         | LangChain + LLM (OpenRouter/Groq)      |
| Data                | Spoonacular API / Web Scraping         |
| Memory              | ChromaDB / SQLite                      |

---

## 📁 Project Structure (Planned)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Microphone + Speaker
- API keys (if using Spoonacular / ElevenLabs)

### Installation

```bash
git clone https://github.com/yourusername/ai-voice-cooking-assistant.git
cd ai-voice-cooking-assistant
pip install -r requirements.txt
python main.py


### 📌 Usage Example

👤 You: “Find me a pasta recipe.”
🤖 Assistant: “Found ‘Garlic Cream Pasta’. Let’s begin.”
🤖 Assistant: “Step 1: Boil water. Say ‘next’ when ready.”
👤 You: “Next.”
🤖 Assistant: “Step 2: Add pasta and cook for 10 minutes. Timer started.”

📅 Roadmap
 Voice Input & Output

 Recipe Search Integration

 Step-by-step Cooking Flow

 Unit Conversion and Timers

 Smart NLP Query Engine

 Personalization & Memory

🤝 Contributing
Pull requests and ideas are welcome! For major changes, please open an issue first to discuss what you would like to change.

📄 License
MIT License. See LICENSE for details.

🙋‍♀️ Creator
Made with ❤️ by ShravaniJ — powered by Python & AI.

yaml
Copy
Edit

---

Let me know if you want me to:
- Create the full folder structure locally.
- Generate `requirements.txt`.
- Write the first script (`voice_input.py`) using Whisper or `SpeechRecognition`.

Ready when you are!
