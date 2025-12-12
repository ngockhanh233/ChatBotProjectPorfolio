import tkinter as tk
from tkinter import scrolledtext
from chat_logic import get_answer
import threading

class ChatApp:
    def __init__(self, root):
        root.title("Chatbox AI - Offline")
        root.geometry("550x600")

        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Segoe UI", 11))
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.chat_area.configure(state="disabled")

        self.entry = tk.Entry(root, font=("Segoe UI", 12))
        self.entry.pack(padx=10, pady=10, fill=tk.X)
        self.entry.bind("<Return>", self.send)

        self.send_btn = tk.Button(root, text="Gửi", font=("Segoe UI", 11),
                                  command=lambda: self.send(None))
        self.send_btn.pack(padx=10, pady=5)

    def send(self, event):
        user_text = self.entry.get().strip()
        if not user_text:
            return
        self.entry.delete(0, tk.END)
        self.add_chat("Bạn: " + user_text)
        threading.Thread(target=self.reply, args=(user_text,), daemon=True).start()

    def reply(self, text):
        answer = get_answer(text)
        self.add_chat("AI: " + answer + "\n")

    def add_chat(self, text):
        self.chat_area.configure(state="normal")
        self.chat_area.insert(tk.END, text + "\n")
        self.chat_area.configure(state="disabled")
        self.chat_area.see(tk.END)
