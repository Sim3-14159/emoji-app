# 😄 Emoji App 🎨

A **Python desktop app** to browse, copy, and generate emojis!  
Quickly grab your favorite emojis, see their colon-style names, and even generate PNGs from a list.

---

## ✨ Features

- 🖼️ **Emoji Grid** – Scrollable interface to browse all emojis.  
- 📋 **Clipboard Copy** – Click any emoji to copy it as a Unicode character.  
- 🏷️ **Emoji Names** – See the colon-style name (e.g., `:smile:`) in the status bar.  
- 🖌️ **Emoji PNG Generator** – Convert emoji characters from a text list into images (`make_emojis.py`).  

---

## 🛠️ Dependencies

| Package      | Version        | Purpose                           |
|-------------|---------------|----------------------------------|
| Python      | 3.7+          | Core language                    |
| tkinter     | system default| GUI framework                    |
| Pillow      | 9.6.0         | Image handling                   |
| pyperclip   | 1.8.2         | Clipboard integration            |
| emoji       | 2.6.0         | Emoji parsing and conversion     |
| pilmoji     | 1.2.0         | Render emojis onto images        |
| regex       | 2025.11.21    | Advanced Unicode regex support   |

> ⚠️ Versions are recommended; newer versions should work but may require testing.

---

## 📂 Project Structure

```

emoji-app/
│
├─ main.py           # Main GUI application
├─ make_emojis.py    # Generates PNG images from emojis.txt
├─ emojis.txt        # Concatenated list of emojis for PNG generation
├─ images/           # Generated PNG emoji images
└─ README.md         # Project overview

````

---

## 🚀 Usage

1. **Run the app**:

```bash
python main.py
````

2. **Generate PNG emojis**:

```bash
python make_emojis.py
```

Generated images will appear in the `images/` folder.

---

## 💡 Notes

* Works on **Windows, macOS, and Linux**.
* The app automatically keeps your emoji images organized.
* Ideal for developers, designers, or anyone who loves emojis! 🎉

