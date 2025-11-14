import tkinter as tk 
from tkinter import messagebox 
import pyttsx3 
import datetime 
import speech_recognition as sr 
import webbrowser 
import wikipedia 
try: 
    main = pyttsx3.init('sapi5') 
    voices = main.getProperty('voices') 
    main.setProperty('voice', voices[1].id) 
except Exception as e: 
    messagebox.showerror("Error", f"Error initializing pyttsx3: {e}") 
    exit() 
 
def speak(audio): 
    output_text.insert(tk.END, f"Bot: {audio}\n")  
    output_text.see(tk.END)   
    main.say(audio) 
    main.runAndWait() 
 
def wishme(): 
    hour = int(datetime.datetime.now().hour) 
    if hour >= 0 and hour <= 12: 
        return "Hello, good morning sir!" 
    elif hour >= 12 and hour <= 18: 
 
 
        return "Hello, good afternoon sir!" 
    else: 
        return "Hello, good evening sir!" 
 
def take(): 
    r = sr.Recognizer() 
    try: 
        with sr.Microphone() as source: 
            output_text.insert(tk.END, "Listening...\n") 
            output_text.see(tk.END) 
            speak("Listening...") 
            audio = r.listen(source, timeout=16, phrase_time_limit=6) 
            query = r.recognize_google(audio, language="en-IN") 
            output_text.insert(tk.END, f"You: {query}\n") 
            output_text.see(tk.END) 
            return query.lower() 
    except sr.UnknownValueError: 
        speak("Sorry, I didn't catch that. Please try again.") 
        return "" 
    except sr.RequestError as e: 
        speak(f"Sorry, I couldn't reach the Google Speech Recognition service.") 
        return "" 
    except Exception as e: 
        speak(f"An error occurred.") 
        return "" 
     
def search_wikipedia(query): 
    try: 
        speak(f"Searching {query} in wikipedia") 

 
        result = wikipedia.summary(query, sentences=5) 
        speak(result)  # Assuming speak() is your text-to-speech function 
    except wikipedia.exceptions.DisambiguationError as e: 
        speak(f"Multiple results found: {e.options[:3]}. Please specify.") 
    except wikipedia.exceptions.PageError: 
        speak("No matching Wikipedia page found.") 
 
def handle_command(command): 
    output_text.insert(tk.END, f"Processing command: {command}\n")   
    output_text.see(tk.END) 
    speak(f"Processing command: {command}") 
     
    sites = { 
        "spotify": "https://open.spotify.com", 
        "vs code": "https://vscode.dev/", 
        "youtube": "https://www.youtube.com", 
        "chrome": "https://www.google.com", 
        "whatsapp": "https://web.whatsapp.com", 
        "ubter": "https://ubter.in/", 
        "polytechnic": "https://klproorkee.co.in/", 
        "syllabus": "https://www.irdtuttarakhand.org.in/ubter/" 
    } 
     
    for key in sites: 
        if key in command: 
            webbrowser.open(sites[key]) 
            speak(f"Opening {key}...") 
            return 
     

 
    if "exit" in command or "quit" in command: 
        speak("Goodbye! Have a nice day.") 
        root.destroy() 
                 
    elif "question" in command: 
        query = command.replace("question", "").strip() 
        if query: 
            search_wikipedia(query) 
        else: 
            speak("Please specify what you want to search on Wikipedia.") 
        return 
     
    else: 
        search_url = f"https://www.google.com/search?q={command}" 
        webbrowser.open(search_url) 
        print(f"Showing search results in Google for: {command}") 
        speak(f"Showing search results in Google for: {command}") 
 
def start_listening(): 
    output_text.delete("1.0", tk.END) 
    a = wishme() 
    speak(a) 
    speak("I am your personal AI bot, how can I assist you?") 
    query = take() 
    if query: 
        handle_command(query) 
         
         
 
root = tk.Tk() 
root.title("Voice Assistant") 
root.configure(bg="#16213e") 
title_label = tk.Label(root, text="Voice Assistant", font=("Arial", 18), fg="white", 
bg="#16213e") 
title_label.pack(pady=10) 
command_text = """Input Suggestion 
1. Spotify 
2. Visual Studio Code 
3. YouTube 
4. Chrome 
5. Notepad 
6. WhatsApp 
7. Polytechnic 
8. Syllabus 
""" 
command_label = tk.Label(root, text=command_text, font=("Arial", 15), fg="blue", 
bg="#16213e", justify="left") 
command_label.pack(pady=10) 
output_text = tk.Text(root, height=15, width=50, bg="black", fg="red", font=("Arial", 12)) 
output_text.pack(pady=5) 
start_btn = tk.Button(root,text=" 🎤 ",font=("Arial", 18),bg="red",fg="blue",padx=50,pady=5,command=start_listening)
start_btn.pack(pady=10) 
root.mainloop()