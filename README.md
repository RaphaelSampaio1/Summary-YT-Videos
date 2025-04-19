# Summary-YT-Videos

```markdown
# 🎥 YouTube Video Summarizer with ChatGPT & GUI

This project allows you to **extract and summarize transcripts from YouTube videos** using AI, all through an elegant **desktop GUI built with CustomTkinter**.

> Built with: `Python`, `youtube-transcript-api`, `g4f`, `customtkinter`.

---

## 🚀 Features

- 📥 Extract transcripts from YouTube videos
- 🧠 Summarize content using AI (via `g4f`)
- 🌐 Translate if needed
- 🪟 Beautiful GUI with `CustomTkinter`
- 📦 Exported as `.exe` for Windows (no need for Python)

---

## 🖼️ Preview

> *(insert a screenshot here if available)*  
> Ex: `assets/gui_screenshot.png`

---

## 📦 Installation

### 🔧 Requirements

- Python 3.11+ (recommended: 3.12 or 3.13)
- Install dependencies:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install youtube-transcript-api customtkinter g4f
```

---

## 🧠 How It Works

1. You paste a YouTube video link
2. The app fetches its transcript (subtitles)
3. The text is sent to an AI model (via g4f)
4. It returns a summarized version instantly

---

## 🧪 Running the App

```bash
python app.py
```

---

## 🪄 Create a `.exe` File (Windows Only)

### Step-by-step:

1. Install PyInstaller:

```bash
pip install pyinstaller
```

2. From your project folder, run:

```bash
pyinstaller --onefile --windowed app.py
```

3. The `.exe` will be in the `/dist` folder:
   ```
   dist/
   └── app.exe
   ```

> Optional: Add an icon  
```bash
pyinstaller --onefile --windowed --icon=icon.ico app.py
```

---

## 📁 File Structure

```
Summary_yt_videos/
├── app.py
├── README.md
├── requirements.txt
├── /dist/
│   └── app.exe
└── icon.ico (optional)
```

---

## 💡 Built With

- [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api)
- [g4f](https://github.com/xtekky/gpt4free)
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- Python 3.13

---

## 🙋‍♂️ Author

Made with ❤️ by [Raphael Sampaio](https://sampaiodev.com)

---
