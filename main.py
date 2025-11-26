#!/usr/bin/env python
"""Emoji Copier - copy emoji PNGs to clipboard as actual emoji characters
and show colon-style name in status"""

from tkinter import *
import pyperclip as pyp
from PIL import Image, ImageTk
import os
import emoji
import platform

# --- Clipboard copy function ---
def copy_symbol(emoji_char, emoji_name, status_label):
    """Copies the actual emoji character to clipboard and shows colon-style name"""
    if emoji_char:
        pyp.copy(emoji_char)
        status_label.set(f'{emoji_name} copied to clipboard')
    else:
        status_label.set("Failed to copy: invalid emoji")

# --- Scrollable canvas helper ---
def on_frame_configure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

# --- Mouse wheel scrolling ---
def _on_mousewheel(event):
    if platform.system() == 'Windows':
        canvas.yview_scroll(-1 * int(event.delta / 120), "units")
    elif platform.system() == 'Darwin':
        canvas.yview_scroll(-1 * int(event.delta), "units")
    else:  # Linux uses Button-4/5 events
        canvas.yview_scroll(-1 * int(event.delta), "units")

# --- Main Tkinter setup ---
root = Tk()
root.title("Emoji Copier")
root.resizable(width=False, height=True)
root.maxsize(height=500, width=365)
root.configure(bg='lightgrey')

path = os.path.dirname(os.path.abspath(__file__))
icon = Image.open(path + "/ICON.png")
icon = ImageTk.PhotoImage(icon)
root.iconphoto(True, icon)

status_text = StringVar()
status_text.set("Click an emoji to copy")

status_label = Label(root, textvariable=status_text, font=('Times 15'), wraplength=320,
                     foreground='blue')
status_label.pack(pady=10)

# --- Loading label ---
loading_text = StringVar()
loading_text.set("Loading emojis...")
loading_label = Label(root, textvariable=loading_text, font=('Times 12'), fg='green')
loading_label.pack(pady=5)

# --- Scrollable area ---
container = Frame(root)
container.pack(fill=BOTH, expand=True, pady=2, padx=2)

canvas = Canvas(container, background='lightyellow')
scrollbar = Scrollbar(container, orient='vertical', command=canvas.yview)
scrollable_frame = Frame(canvas, background='lightyellow')

canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.config(command=canvas.yview)

scrollbar.pack(side=RIGHT, fill=Y, padx=2)
canvas.pack(side=LEFT, fill=BOTH, expand=True, padx=5)

canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
scrollable_frame.bind("<Configure>", lambda e: on_frame_configure(canvas))

# --- Bind mouse wheel events ---
if platform.system() == 'Linux':
    canvas.bind_all("<Button-4>", lambda e: canvas.yview_scroll(-1, "units"))
    canvas.bind_all("<Button-5>", lambda e: canvas.yview_scroll(1, "units"))
else:
    canvas.bind_all("<MouseWheel>", _on_mousewheel)

# --- Load all PNGs in current directory ---
path = os.path.dirname(os.path.abspath(__file__)) + "/emojis"
png_files = [f"{path}/{f}" for f in os.listdir(path) if f.lower().endswith('.png')]
num_files = len(png_files)
photo_refs = []  # keep references to PhotoImage

# --- Layout parameters ---
button_size = 50
padding = 5
max_columns = 5  # number of buttons per row

# --- Function to load images incrementally to show progress ---
def load_emojis():
    y = 0
    x = 0
    for idx, filename in enumerate(png_files, start=1):
        # Load image and resize
        img = Image.open(filename)
        img.thumbnail((button_size, button_size))
        photo = ImageTk.PhotoImage(img)
        photo_refs.append(photo)  # keep reference

        # Convert filename to emoji character
        name = os.path.splitext(os.path.basename(filename))[0]
        try:
            emoji_char = emoji.emojize(f":{name}:", language='alias')
        except Exception:
            emoji_char = ""

        # Create button
        button = Button(scrollable_frame, image=photo,
                        command=lambda e=emoji_char, n=name: copy_symbol(e, f":{n.split('/')[-1]}:", status_text),
                        width=button_size, height=button_size,
                        activebackground='grey')
        button.grid(row=y, column=x, padx=padding, pady=padding)

        x += 1
        if x >= max_columns:
            x = 0
            y += 1

        # Update loading progress
        loading_text.set(f"Loading emojis... ({idx}/{num_files})█")
        root.update_idletasks()

    loading_text.set(f"Loaded {num_files} emojis!")
    root.after(1000, lambda: loading_text.set(""))

# --- Start loading emojis ---
root.after(100, load_emojis)  # schedule loading after window appears

root.mainloop()

#todo: add loading █. add hover text.