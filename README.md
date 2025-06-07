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
ai-voice-cooking-assistant/
│
├── main.py # Main app controller
├── voice_input.py # Handles microphone input + STT
├── voice_output.py # TTS responses
├── recipe_manager.py # Search, fetch, and parse recipes
├── cooking_assistant.py # Cooking logic, NLP commands
├── utils/
│ ├── timer.py # Timer management
│ └── converter.py # Unit conversions
├── assets/ # Recipe samples, sound files
├── requirements.txt
└── README.md

## 📌 Usage Example

> 👤 **You:** “Find me a pasta recipe.”  
> 🤖 **Assistant:** “Found ‘Garlic Cream Pasta’. Let’s begin.”  
> 🤖 **Assistant:** “Step 1: Boil water. Say ‘next’ when ready.”  
> 👤 **You:** “Next.”  
> 🤖 **Assistant:** “Step 2: Add pasta and cook for 10 minutes. Timer started.”

---

## 📅 Roadmap

- [x] Voice Input & Output  
- [ ] Recipe Search Integration  
- [ ] Step-by-step Cooking Flow  
- [ ] Unit Conversion and Timers  
- [ ] Smart NLP Query Engine  
- [ ] Personalization & Memory

---

## ## 📁 Project Structure (Planned)
## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Microphone + Speaker
- API keys (if using Spoonacular / ElevenLabs)


---

## 📄 License

MIT License. See `LICENSE` for details.

---

## 🙋‍♀️ Creator

Made with ❤️ by **ShravaniJ** — AI/ML Engineer
