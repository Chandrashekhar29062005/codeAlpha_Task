from googletrans import Translator
import tkinter as tk
from tkinter import ttk, messagebox

# Initialize translator
translator = Translator()

# Function to translate
def translate_text():
    src = src_lang.get()
    dest = dest_lang.get()
    text = input_text.get("1.0", "end-1c")
    if not text.strip():
        messagebox.showwarning("Warning", "Please enter some text.")
        return
    try:
        translated = translator.translate(text, src=src, dest=dest)
        output_text.delete("1.0", "end")
        output_text.insert("end", translated.text)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("500x400")

# Dropdowns
langs = ['en', 'es', 'fr', 'de', 'ta', 'hi', 'te', 'ml', 'zh-cn', 'ja']
src_lang = ttk.Combobox(root, values=langs, width=10)
src_lang.set('en')
src_lang.pack(pady=5)

dest_lang = ttk.Combobox(root, values=langs, width=10)
dest_lang.set('es')
dest_lang.pack(pady=5)

# Text fields
input_text = tk.Text(root, height=6, width=50)
input_text.pack(pady=5)

translate_btn = tk.Button(root, text="Translate", command=translate_text)
translate_btn.pack(pady=5)

output_text = tk.Text(root, height=6, width=50)
output_text.pack(pady=5)

root.mainloop()