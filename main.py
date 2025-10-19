import tkinter as tk
import hashlib

def convert_text():
    text = entry.get()
    if not text.strip():
        result_label.config(text="Please enter some text.")
        return
    hashed = hashlib.sha256(text.encode('utf-8')).hexdigest()
    result_label.config(text=hashed)

def copy_to_clipboard():
    hash_text = result_label.cget("text")
    if not hash_text.strip():
        status_label.config(text="Nothing to copy.")
        return
    root.clipboard_clear()
    root.clipboard_append(hash_text)
    root.update()
    status_label.config(text="Hash copied to clipboard!")

root = tk.Tk()
root.title("Text to SHA-256 Converter")
root.geometry("600x200")
root.resizable(False, False)

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(expand=True, fill="both")

label = tk.Label(frame, text="Enter text:", font=("Arial", 12))
label.pack(anchor="w")

entry = tk.Entry(frame, width=70, font=("Arial", 11))
entry.pack(pady=5)

convert_button = tk.Button(frame, text="Convert", command=convert_text, bg="#4A90E2", fg="white", font=("Arial", 11, "bold"))
convert_button.pack(pady=5)

result_label = tk.Label(frame, text="", wraplength=550, justify="left", font=("Courier", 10))
result_label.pack(pady=10)

copy_button = tk.Button(frame, text="Copy Hash", command=copy_to_clipboard, font=("Arial", 10))
copy_button.pack()

status_label = tk.Label(frame, text="", font=("Arial", 9), fg="green")
status_label.pack(pady=5)

root.mainloop()