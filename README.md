<h1><img src="ICON.png" height="50" style="vertical-align: bottom">&emsp;
  $$\color{#ffcc55}\Huge\textbf{Emoji App}$$
</h1>


A **Python desktop app** to browse, copy, and generate emojis!  
Quickly grab your favorite emojis, see their colon-style names, and even generate PNGs from a list.

---

## ✨ Features

- 🖼️ **Emoji Grid** – Scrollable interface to browse all emojis.  
- 📋 **Clipboard Copy** – Click any emoji to copy it as a Unicode character.  
- 🏷️ **Emoji Names** – See the colon-style name (e.g., `:smile:`) in the status bar.  
- 🖌️ **Emoji PNG Generator** – Convert emoji characters from a text list into images ([`make_emojis.py`](make_emojis.py)).  

---

## 🛠️ Dependencies

### 📦 Packages 
> | Name      | Version        | Purpose                           |
> |-------------|---------------|----------------------------------|
> | tkinter     | system default| GUI framework                    |
> | Pillow      | 9.6.0         | Image handling                   |
> | pyperclip   | 1.8.2         | Clipboard integration            |
> | emoji       | 2.6.0         | Emoji parsing and conversion     |
> | pilmoji     | 1.2.0         | Render emojis onto images        |
> | regex       | 2025.11.21    | Advanced Unicode regex support   |

> [!WARNING]
> Versions are recommended; newer versions may not work.

### 🧰 System Tools
> | Name | Version | Purpose |
> |---|---|---|
> | `python` | 3.7.*x*+ | You need Python to run `.py` files. |

---

## 📂 Project Structure

| Name | Description |
|--|--|
|[`main.py`](main.py)|  Launches emoji app GUI. |      
|[`make_emojis.py`](make_emojis.py) | Run this to configure `main.py` to use the emojis in `emojis.txt`. |  
|[`emojis.txt`](emojis.txt)| Put any emojis you want in this file, then run `make_emojis.py` to configure the app to use them. |   
|[`images/`](images)| When `make_emojis.py` is run, the output files are stored in here.    |
|[`LICENSE`](LICENSE)| It's a license 🤓. What did you think it did? |
|[`README.md`](README.md)| This file, a REAME |


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

