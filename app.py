import os
import requests
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "linguaai-secret-key")

LANGUAGE_OPTIONS = [
    ("auto", "Detect Language"),
    ("en", "English"),
    ("es", "Spanish"),
    ("fr", "French"),
    ("de", "German"),
    ("hi", "Hindi"),
    ("ar", "Arabic"),
    ("ja", "Japanese"),
    ("ko", "Korean"),
    ("pt", "Portuguese"),
    ("it", "Italian"),
    ("ru", "Russian"),
    ("zh-cn", "Chinese (Simplified)"),
    ("zh-tw", "Chinese (Traditional)"),
]


def translate_text(text, source_lang, target_lang):
    if not text or not text.strip():
        raise ValueError("Please enter text to translate.")

    source_lang = source_lang or "auto"
    target_lang = target_lang or "en"

    try:
        response = requests.get(
            "https://translate.googleapis.com/translate_a/single",
            params={
                "client": "gtx",
                "sl": source_lang,
                "tl": target_lang,
                "dt": "t",
                "q": text,
            },
            timeout=10,
        )
        response.raise_for_status()
        payload = response.json()

        translated_parts = []
        if isinstance(payload, list) and payload:
            if isinstance(payload[0], list):
                for item in payload[0]:
                    if isinstance(item, list) and item:
                        translated_parts.append(item[0] or "")
            elif isinstance(payload[0], str):
                translated_parts.append(payload[0])

        translated_text = "".join(translated_parts)
        detected_language = payload[2] if len(payload) > 2 else source_lang
        return translated_text, detected_language, ""
    except Exception as exc:
        return text, source_lang, f"Translation service is temporarily unavailable: {exc}"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/translator", methods=["GET", "POST"])
def translator():
    source_lang = request.form.get("source_language", "auto")
    target_lang = request.form.get("target_language", "en")
    input_text = request.form.get("text", "")
    translated_text = ""
    message = ""
    detected_lang = ""

    if request.method == "POST":
        translated_text, detected_lang, message = translate_text(input_text, source_lang, target_lang)

    return render_template(
        "translator.html",
        language_options=LANGUAGE_OPTIONS,
        source_lang=source_lang,
        target_lang=target_lang,
        input_text=input_text,
        translated_text=translated_text,
        message=message,
        detected_lang=detected_lang,
    )


@app.route("/api/translate", methods=["POST"])
def api_translate():
    data = request.get_json(silent=True) or {}
    text = (data.get("text") or "").strip()
    source_lang = data.get("source_language", "auto")
    target_lang = data.get("target_language", "en")

    if not text:
        return jsonify({"translated_text": "", "error": "Please enter text to translate."}), 400

    translated_text, detected_lang, message = translate_text(text, source_lang, target_lang)
    return jsonify({
        "translated_text": translated_text,
        "detected_language": detected_lang,
        "message": message,
    })


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
