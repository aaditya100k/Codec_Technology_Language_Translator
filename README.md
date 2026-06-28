# LinguaAI Translator

A responsive AI language translator web app built with Flask and Python. It includes a polished UI for home, translator, about, and contact pages, plus backend translation support, copy-to-clipboard, text-to-speech, and language swap features.

## Features
- Home, Translator, About, and Contact pages
- Flask-based backend with translation routes
- Responsive modern UI
- Copy text action
- Text-to-speech support
- Swap language feature

## Project Structure
- app.py - Flask application entry point
- templates/ - HTML templates for the pages
- static/ - CSS and JavaScript assets
- requirements.txt - Python dependencies

## Setup
1. Open PowerShell in the project folder.
2. Create and activate a virtual environment (optional but recommended):
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

## Run the App
```powershell
cd "C:\Users\HP\OneDrive\Desktop\Codec_Technology_language-translator"
C:\Users\HP\OneDrive\Desktop\Codec_Technology_language-translator\.venv\Scripts\python.exe app.py
```

Then open:
```text
http://127.0.0.1:5000/
```

## Notes
- The translation feature uses a public Google Translate endpoint.
- For production deployment, use a proper WSGI server such as Gunicorn.
