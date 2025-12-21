#!/c/Users/lh185009/AppData/Local/Programs/Python/Python312/python

import tkinter as tk
from tkinter import ttk
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import tempfile
import os

# -----------------------------
# Globals & Config
# -----------------------------
translator = Translator()
DELAY_MS = 250
scheduled_job = None
dark_mode = False

LANGUAGES = {
    "Arabic": "ar",
    "Chinese (Simplified)": "zh-cn",
    "Chinese (Traditional)": "zh-tw",
    "English": "en",
    "French": "fr",
    "German": "de",
    "Japanese": "ja",
    "Korean": "ko",
    "Spanish": "es",
    "Russian": "ru"
}

# -----------------------------
# Translation Logic
# -----------------------------
def schedule_translation(event=None):
    global scheduled_job
    if scheduled_job is not None:
        root.after_cancel(scheduled_job)
    scheduled_job = root.after(DELAY_MS, translate_text)

def translate_text(event=None):
    src_text = input_box.get("1.0", tk.END).strip()
    target_lang = LANGUAGES.get(lang_var.get(), "en")

    if not src_text:
        output_box.delete("1.0", tk.END)
        return

    try:
        result = translator.translate(src_text, dest=target_lang)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, result.text)
    except Exception as e:
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, f"Translation error: {e}")

# -----------------------------
# Text-to-Speech (gTTS)
# -----------------------------
def speak_output():
    text = output_box.get("1.0", tk.END).strip()
    if not text:
        return

    lang_code = LANGUAGES.get(lang_var.get(), "en")

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            temp_path = fp.name

        tts = gTTS(text=text, lang=lang_code)
        tts.save(temp_path)
        playsound(temp_path)

    except Exception as e:
        print(f"TTS error: {e}")

    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

# -----------------------------
# Dark Mode Toggle
# -----------------------------
def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode

    if dark_mode:
        bg = "#1e1e1e"
        fg = "white"
        left_bg = "#2b2b2b"
        right_bg = "#2b2b2b"
        toolbar_bg = "#333333"
    else:
        bg = "#e8f4fc"
        fg = "black"
        left_bg = "#d9f7e8"
        right_bg = "#fce8e8"
        toolbar_bg = "#cfe2ff"

    root.configure(bg=bg)
    toolbar.configure(bg=toolbar_bg)
    left_frame.configure(bg=left_bg)
    right_frame.configure(bg=right_bg)

    input_box.configure(bg=left_bg, fg=fg, insertbackground=fg)
    output_box.configure(bg=right_bg, fg=fg, insertbackground=fg)

    status_bar.configure(bg=bg, fg=fg)

# -----------------------------
# UI Setup
# -----------------------------
root = tk.Tk()
root.title("EZ Translator (Pro Edition)")
root.geometry("1100x600")
root.configure(bg="#e8f4fc")

# Toolbar
toolbar = tk.Frame(root, bg="#cfe2ff", padx=10, pady=5)
toolbar.pack(fill="x")

ttk.Button(toolbar, text="🌙 Dark Mode", command=toggle_dark_mode).pack(side="left", padx=5)

# Main layout
main_frame = tk.Frame(root, bg="#e8f4fc")
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
main_frame.rowconfigure(0, weight=1)

# Left Pane
left_frame = tk.Frame(main_frame, bg="#d9f7e8", relief="solid", borderwidth=2, padx=10, pady=10)
left_frame.grid(row=0, column=0, sticky="nsew")

tk.Label(left_frame, text="Input Text", bg="#d9f7e8", font=("Segoe UI", 11, "bold")).pack(anchor="w")

input_box = tk.Text(left_frame, wrap="word", font=("Segoe UI", 11), height=20, bg="#ffffff")
input_box.pack(fill="both", expand=True, pady=5)
input_box.bind("<KeyRelease>", schedule_translation)

# Right Pane
right_frame = tk.Frame(main_frame, bg="#fce8e8", relief="solid", borderwidth=2, padx=10, pady=10)
right_frame.grid(row=0, column=1, sticky="nsew")

tk.Label(right_frame, text="Target Language", bg="#fce8e8", font=("Segoe UI", 11, "bold")).pack(anchor="w")

lang_var = tk.StringVar(value="English")
lang_combo = ttk.Combobox(right_frame, textvariable=lang_var, state="readonly",
                          values=list(LANGUAGES.keys()))
lang_combo.pack(fill="x")
lang_combo.bind("<<ComboboxSelected>>", translate_text)

# Read Button
read_btn = ttk.Button(right_frame, text="🔊 Read", command=speak_output)
read_btn.pack(anchor="e", pady=5)

output_box = tk.Text(right_frame, wrap="word", font=("Segoe UI", 11), height=20, bg="#ffffff")
output_box.pack(fill="both", expand=True, pady=5)

# Status Bar
status_var = tk.StringVar(value="Ready")
status_bar = tk.Label(root, textvariable=status_var, anchor="w", pady=5, bg="#e8f4fc")
status_bar.pack(fill="x")

root.mainloop()
