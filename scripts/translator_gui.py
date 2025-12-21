#!/c/Users/lh185009/AppData/Local/Programs/Python/Python312/python

import tkinter as tk
from tkinter import ttk
from googletrans import Translator

translator = Translator()
delay_ms = 250
job = None

# Map full names to codes
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

def schedule_translate(event=None):
    global job
    if job is not None:
        root.after_cancel(job)
    job = root.after(delay_ms, translate_text)

def translate_text(event=None):
    src_text = input_box.get("1.0", tk.END).strip()
    target_lang_name = lang_var.get()
    target_lang_code = LANGUAGES.get(target_lang_name, "en")
    if src_text:
        try:
            result = translator.translate(src_text, dest=target_lang_code)
            output_box.delete("1.0", tk.END)
            output_box.insert(tk.END, result.text)
        except Exception as e:
            output_box.delete("1.0", tk.END)
            output_box.insert(tk.END, f"Translation error: {e}")

# Main window
root = tk.Tk()
root.title("EZ Translator         version:2025-12-19")
root.geometry("800x400")
root.configure(bg="lightgreen")  # set background color

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)

# Left input box
tk.Label(root, text="Input Text For Traslation", bg="lightgreen").grid(row=0, column=0, padx=10, pady=5, sticky="w")
input_box = tk.Text(root, wrap="word")
input_box.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
input_box.bind("<KeyRelease>", schedule_translate)

# Right side frame
frame_right = tk.Frame(root, bg="lightgreen")
frame_right.grid(row=0, column=1, rowspan=2, sticky="nsew", padx=10, pady=5)
frame_right.columnconfigure(0, weight=1)
frame_right.rowconfigure(1, weight=1)

tk.Label(frame_right, text="Select Target Language", bg="lightgreen").grid(row=0, column=0, sticky="w")

lang_var = tk.StringVar(value="English")
lang_combo = ttk.Combobox(frame_right, textvariable=lang_var, state="readonly")
lang_combo['values'] = list(LANGUAGES.keys())
lang_combo.grid(row=0, column=1, sticky="ew")
lang_combo.bind("<<ComboboxSelected>>", translate_text)

output_box = tk.Text(frame_right, wrap="word")
output_box.grid(row=1, column=0, columnspan=2, sticky="nsew")

root.mainloop()

