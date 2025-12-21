#!/c/Users/lh185009/AppData/Local/Programs/Python/Python312/python

import customtkinter as ctk
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
        app.after_cancel(scheduled_job)
    scheduled_job = app.after(DELAY_MS, translate_text)

def translate_text(event=None):
    src_text = input_box.get("1.0", "end").strip()
    target_lang = LANGUAGES.get(lang_var.get(), "en")

    if not src_text:
        output_box.delete("1.0", "end")
        status_label.configure(text="Ready")
        return

    status_label.configure(text=f"Translating to {lang_var.get()}...")
    app.update_idletasks()

    try:
        result = translator.translate(src_text, dest=target_lang)
        output_box.delete("1.0", "end")
        output_box.insert("end", result.text)
        status_label.configure(text="Translation complete")
    except Exception as e:
        output_box.delete("1.0", "end")
        output_box.insert("end", f"Translation error: {e}")
        status_label.configure(text="Translation error")

# -----------------------------
# Text-to-Speech
# -----------------------------
def speak_output():
    text = output_box.get("1.0", "end").strip()
    if not text:
        status_label.configure(text="Nothing to read")
        return

    lang_code = LANGUAGES.get(lang_var.get(), "en")
    status_label.configure(text=f"Reading in {lang_var.get()}...")
    app.update_idletasks()

    temp_path = None
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            temp_path = fp.name

        tts = gTTS(text=text, lang=lang_code)
        tts.save(temp_path)
        playsound(temp_path)
        status_label.configure(text="Done")
    except Exception:
        status_label.configure(text="Read‑aloud error")
    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)

# -----------------------------
# Toolbar Buttons
# -----------------------------
def open_settings():
    win = ctk.CTkToplevel(app)
    win.title("Settings")
    win.resizable(True, True)

    ctk.CTkLabel(
        win,
        text="Settings Panel (future expansion)",
        font=("Segoe UI", 14)
    ).pack(padx=20, pady=20)


def open_about():
    win = ctk.CTkToplevel(app)
    win.title("About")
    win.resizable(True, True)

    ctk.CTkLabel(
        win,
        text="EZ Translator\nVersion: 2025-12-21\nThis was created for users who may benefit\nAn example to show how AI can help us realize our imaginations",
        font=("Segoe UI", 14)
    ).pack(padx=20, pady=20)

# -----------------------------
# App Setup
# -----------------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("EZ Translator           (Version: 2025-12-21)")
app.geometry("1100x650")
app.minsize(900, 550)

# -----------------------------
# Electric Blue Palette
# -----------------------------
BLUE = "#3b82f6"          # Electric blue
BLUE_HOVER = "#60a5fa"    # Lighter electric blue
BLUE_DARK = "#1e293b"     # Dark navy panel
BLUE_BG = "#0f172a"       # Deep navy background

app.configure(fg_color=BLUE_BG)

# -----------------------------
# Toolbar (Full-width, minimal)
# -----------------------------
toolbar = ctk.CTkFrame(app, height=50, corner_radius=0, fg_color=BLUE_DARK)
toolbar.pack(fill="x")

settings_btn = ctk.CTkButton(
    toolbar, text="⚙️ Settings", width=90,
    fg_color=BLUE, hover_color=BLUE_HOVER,
    command=open_settings
)
settings_btn.pack(side="left", padx=10, pady=10)

about_btn = ctk.CTkButton(
    toolbar, text="ℹ️ About", width=90,
    fg_color=BLUE, hover_color=BLUE_HOVER,
    command=open_about
)
about_btn.pack(side="left", padx=10)

# -----------------------------
# Main Content Area
# -----------------------------
content = ctk.CTkFrame(app, fg_color=BLUE_BG)
content.pack(fill="both", expand=True, padx=10, pady=10)

content.grid_columnconfigure(0, weight=1)
content.grid_columnconfigure(1, weight=1)
content.grid_rowconfigure(0, weight=1)

# -----------------------------
# Left Panel (Input)
# -----------------------------
left_panel = ctk.CTkFrame(content, corner_radius=15, fg_color=BLUE_DARK)
left_panel.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

ctk.CTkLabel(left_panel, text="Input Text", font=("Segoe UI", 14, "bold")).pack(anchor="w", padx=10, pady=10)

input_box = ctk.CTkTextbox(left_panel, font=("Segoe UI", 13), fg_color="#111827")
input_box.pack(fill="both", expand=True, padx=10, pady=10)
input_box.bind("<KeyRelease>", schedule_translation)

# -----------------------------
# Right Panel (Output)
# -----------------------------
right_panel = ctk.CTkFrame(content, corner_radius=15, fg_color=BLUE_DARK)
right_panel.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

ctk.CTkLabel(right_panel, text="Translation Output", font=("Segoe UI", 14, "bold")).pack(anchor="w", padx=10, pady=10)

# Language selector row
lang_row = ctk.CTkFrame(right_panel, fg_color="transparent")
lang_row.pack(fill="x", padx=10)

ctk.CTkLabel(lang_row, text="Target Language:", font=("Segoe UI", 12)).pack(side="left", padx=5)

lang_var = ctk.StringVar(value="English")
lang_menu = ctk.CTkOptionMenu(
    lang_row, values=list(LANGUAGES.keys()), variable=lang_var,
    fg_color=BLUE, button_color=BLUE, button_hover_color=BLUE_HOVER,
    command=lambda _: translate_text()
)
lang_menu.pack(side="left", padx=5)

read_btn = ctk.CTkButton(
    lang_row, text="🔊 Read", width=80,
    fg_color=BLUE, hover_color=BLUE_HOVER,
    command=speak_output
)
read_btn.pack(side="right", padx=5)

output_box = ctk.CTkTextbox(right_panel, font=("Segoe UI", 13), fg_color="#111827")
output_box.pack(fill="both", expand=True, padx=10, pady=10)

# -----------------------------
# Status Bar
# -----------------------------
status_label = ctk.CTkLabel(app, text="Ready", anchor="w", height=25, fg_color=BLUE_BG)
status_label.pack(fill="x", padx=10, pady=(0, 10))

app.mainloop()