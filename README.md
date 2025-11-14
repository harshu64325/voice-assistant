# 🎤 AI Voice Assistant (Python)

A Python-based desktop **Voice Assistant** that listens to your speech, performs tasks, opens applications/websites, searches Google or Wikipedia, and responds using text-to-speech — all inside a clean Tkinter GUI.

---

## 🚀 Features

### 🔊 Voice Interaction
- Real-time speech recognition  
- Responds with natural TTS using **pyttsx3 (sapi5 engine)**  

### 🔍 Smart Search
- Search anything on **Google**  
- Search topics on **Wikipedia** (with fallback logic)  
- Reads summaries with voice output  

### 🌐 Quick Commands  
Open apps/websites instantly using voice:

| Command | Action |
|--------|---------|
| **Spotify** | Opens Spotify |
| **VS Code / Visual Studio Code** | Opens VS Code |
| **YouTube** | Opens YouTube |
| **Chrome** | Opens Google |
| **WhatsApp** | Opens WhatsApp Web |
| **Polytechnic** | Opens college site |
| **Syllabus** | Opens syllabus site |

### 🖥 GUI Application
- Built with **Tkinter**  
- Clean dark mode layout  
- Input suggestions panel  
- Scrollable live output box  
- Shows bot and user logs  

---

## 🛠 Tech Stack

- **Python**
- **Tkinter** – GUI  
- **SpeechRecognition** – Voice input  
- **pyttsx3** – Text-to-speech  
- **Wikipedia API**  
- **webbrowser**  
- **datetime**  

---

## 📦 Installation

### 1️⃣ Clone the Repository
```sh

cd voice-assistant

Install dependencies:
pip install pyttsx3 SpeechRecognition wikipedia PyAudio


If PyAudio fails:
pip install pipwin
pipwin install pyaudio
## ▶️ Run the App
python main.py
